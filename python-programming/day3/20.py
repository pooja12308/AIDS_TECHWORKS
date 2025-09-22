<<<<<<< HEAD
'''You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup).'''

def library():
    d={}
    print("1.Add a book to the library (Book ID, Title).\t2.Remove a book using Book ID.\t3.Search for a book by Book ID and display the title.\t4.Update the title of a book.\t5.Display all books in the library.\t6.Count the total number of books in the library.\t7.Check if a book title exists in the library")
    while True:
        ch=int(input("Enter choice"))
        if ch==1:
            n=int(input("Enter no of items"))
            for i in range (n):
                k=int(input(f"Enter book no {i} id : "))
                v=input("Enter book name : ")
                d[k]=v
            print(f"Library : {d}")
        elif ch==2:
            id=int(input("Enter bookid"))
            if(id in d.keys()):
                d.pop(id)
                print(f"Book removed, Updated library : {d}")
            else:
                print("Book doesn't exist")
        elif ch==3:
            id=int(input("Enter id of book to search"))
            if (id in d.keys()):
                print(f"Book with id : {id} is {d[id]}")
            else:
                print("Book with such id doesn't exist")
        elif ch==4:
            id=int(input("Enter id of book whose title you want to update"))
            if (id in d.keys()):
                uval=input("Enter update value")
                d[id]=uval
                print(f"Updated library : {d}")
            else:
                print("book with such id doesn't exist")
        elif ch==5:
            print(f"All books in the library : {d.values()}")
        elif ch==6:
            print(f"total no of books in the library are : {len(d.keys())}")
        elif ch==7:
            val=input("Enter book title")
            if val in d.values():
                print(f"Yes, The book with title {val} exists")
            else:
                print("No, such book doesn't exist")
        else:
            exit(0)
=======
'''You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup).'''

def library():
    d={}
    print("1.Add a book to the library (Book ID, Title).\t2.Remove a book using Book ID.\t3.Search for a book by Book ID and display the title.\t4.Update the title of a book.\t5.Display all books in the library.\t6.Count the total number of books in the library.\t7.Check if a book title exists in the library")
    while True:
        ch=int(input("Enter choice"))
        if ch==1:
            n=int(input("Enter no of items"))
            for i in range (n):
                k=int(input(f"Enter book no {i} id : "))
                v=input("Enter book name : ")
                d[k]=v
            print(f"Library : {d}")
        elif ch==2:
            id=int(input("Enter bookid"))
            if(id in d.keys()):
                d.pop(id)
                print(f"Book removed, Updated library : {d}")
            else:
                print("Book doesn't exist")
        elif ch==3:
            id=int(input("Enter id of book to search"))
            if (id in d.keys()):
                print(f"Book with id : {id} is {d[id]}")
            else:
                print("Book with such id doesn't exist")
        elif ch==4:
            id=int(input("Enter id of book whose title you want to update"))
            if (id in d.keys()):
                uval=input("Enter update value")
                d[id]=uval
                print(f"Updated library : {d}")
            else:
                print("book with such id doesn't exist")
        elif ch==5:
            print(f"All books in the library : {d.values()}")
        elif ch==6:
            print(f"total no of books in the library are : {len(d.keys())}")
        elif ch==7:
            val=input("Enter book title")
            if val in d.values():
                print(f"Yes, The book with title {val} exists")
            else:
                print("No, such book doesn't exist")
        else:
            exit(0)
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
library()