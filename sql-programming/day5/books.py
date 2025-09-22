import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

# Supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# ------------------- MEMBERS -------------------

def add_member(name, email):
    """Register a new member"""
    resp = sb.table("members").insert({"name": name, "email": email}).execute()
    return resp.data

def update_member(member_id, name=None, email=None):
    """Update member info"""
    payload = {}
    if name: payload['name'] = name
    if email: payload['email'] = email
    resp = sb.table("members").update(payload).eq("member_id", member_id).execute()
    return resp.data

def delete_member(member_id):
    """Delete member only if no borrowed books"""
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).is_("return_date", None).execute()
    if borrowed.data:
        return f"Cannot delete: member {member_id} has borrowed books."
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data

def get_member(member_id):
    """Get member details with borrowed books"""
    member = sb.table("members").select("*").eq("member_id", member_id).execute().data
    borrowed = sb.table("borrow_records").select("book_id, borrow_date, return_date").eq("member_id", member_id).execute().data
    return member, borrowed

# ------------------- BOOKS -------------------
def add_book(title, author, category, stock=1):
    """Add a new book"""
    resp = sb.table("books").insert({
        "title": title,
        "author": author,
        "category": category,
        "stock": stock
    }).execute()
    return resp.data

def update_book_stock(book_id, stock):
    """Update stock"""
    resp = sb.table("books").update({"stock": stock}).eq("book_id", book_id).execute()
    return resp.data

def delete_book(book_id):
    """Delete book only if not borrowed"""
    borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
    if borrowed.data:
        return f"Cannot delete: book {book_id} is currently borrowed."
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    return resp.data

def list_books():
    """List all books with availability"""
    books = sb.table("books").select("*").execute().data
    return books

def search_books(keyword):
    """Search by title, author, or category"""
    books = sb.table("books").select("*").or_(
        f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    ).execute().data
    return books

# ------------------- BORROW / RETURN -------------------
def borrow_book(member_id, book_id):
    """Borrow a book in transaction"""
    # Step 1: check stock
    book = sb.table("books").select("*").eq("book_id", book_id).execute().data
    if not book:
        return "Book not found."
    if book[0]['stock'] < 1:
        return "Book not available."

    # Step 2: decrease stock
    try:
        # Decrease stock
        sb.table("books").update({"stock": book[0]['stock'] - 1}).eq("book_id", book_id).execute()
        # Insert borrow record
        sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()
        return f"Book {book_id} borrowed by member {member_id}."
    except Exception as e:
        return f"Error: {e}"

def return_book(member_id, book_id):
    """Return a book in transaction"""
    record = sb.table("borrow_records").select("*").eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute().data
    if not record:
        return "No active borrow record found."
    record_id = record[0]['record_id']

    try:
        # Update return date
        sb.table("borrow_records").update({"return_date": datetime.now().isoformat()}).eq("record_id", record_id).execute()
        # Increase book stock
        book = sb.table("books").select("*").eq("book_id", book_id).execute().data[0]
        sb.table("books").update({"stock": book['stock'] + 1}).eq("book_id", book_id).execute()
        return f"Book {book_id} returned by member {member_id}."
    except Exception as e:
        return f"Error: {e}"

# ------------------- REPORTS -------------------
def top_borrowed_books(limit=5):
    """Top N most borrowed books"""
    query = """
    SELECT b.book_id, b.title, b.author, COUNT(r.record_id) AS borrow_count
    FROM books b
    JOIN borrow_records r ON b.book_id = r.book_id
    GROUP BY b.book_id
    ORDER BY borrow_count DESC
    LIMIT %s;
    """ % limit
    resp = sb.rpc("execute_sql", {"query": query}).execute()  # Or use Supabase SQL editor to create RPC
    return resp.data

def overdue_members(days=14):
    """List members with overdue books"""
    overdue_date = datetime.now() - timedelta(days=days)
    records = sb.table("borrow_records").select("member_id, book_id, borrow_date").is_("return_date", None).lt("borrow_date", overdue_date.isoformat()).execute().data
    return records

def borrowed_count_per_member():
    """Total books borrowed per member"""
    query = """
    SELECT m.member_id, m.name, COUNT(r.record_id) AS total_borrowed
    FROM members m
    LEFT JOIN borrow_records r ON m.member_id = r.member_id
    GROUP BY m.member_id
    ORDER BY total_borrowed DESC;
    """
    resp = sb.rpc("execute_sql", {"query": query}).execute()
    return resp.data

# ------------------- CLI -------------------
def main():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. Reports")
        print("0. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            name = input("Member name: ")
            email = input("Email: ")
            print(add_member(name, email))
        elif choice == "2":
            title = input("Title: ")
            author = input("Author: ")
            category = input("Category: ")
            stock = int(input("Stock: "))
            print(add_book(title, author, category, stock))
        elif choice == "3":
            member_id = int(input("Member ID: "))
            book_id = int(input("Book ID: "))
            print(borrow_book(member_id, book_id))
        elif choice == "4":
            member_id = int(input("Member ID: "))
            book_id = int(input("Book ID: "))
            print(return_book(member_id, book_id))
        elif choice == "5":
            books = list_books()
            for b in books:
                print(b)
        elif choice == "6":
            print("Top borrowed books:", top_borrowed_books())
            print("Overdue members:", overdue_members())
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
