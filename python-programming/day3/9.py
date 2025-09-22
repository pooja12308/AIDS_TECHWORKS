<<<<<<< HEAD
'''You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart
 
Cart Operations:
1. Add Product
2. Remove Product
3. Search Product
4. Display Cart
5. Count Products
6. Exit
 
Enter choice: 1
Enter product to add: Laptop
Product 'Laptop' added to cart.
 
Enter choice: 1
Enter product to add: Phone
Product 'Phone' added to cart.
 
Enter choice: 4
Cart: ['Laptop', 'Phone']
 
Enter choice: 3
Enter product to search: Phone
Yes, 'Phone' is in the cart.
 
Enter choice: 5
Total products in cart: 2 '''

def cart():
    l=[]
    print("Cart Operations:1. Add Product\t2. Remove Product\t3. Search Product\t4. Display Cart\t5. Count Products\t6. Sort the cart items alphabetically\t7. Clear the cart\t8. Exit\n")
    while True:
        ch=int(input("Enter choice : "))
        if ch==1:
            item=input("enter product to add : ")
            l.append(item)
            print(f"product {item} added to the cart")
        elif ch==2:
            item=input("enter product to remove : ")
            if item in l:
                l.remove(item)
                print(f"product {item} removed from the cart")
            else:
                print(f"product {item} is not present in the cart")
        elif ch==3:
            item=input("Enter product to search : ")
            if item in l:
                print(f"yes,{item} is present in the cart")
            else:
                print(f"no,{item} is not present in the cart")
        elif ch==4:
            print(f"Cart : {l}")
        elif ch==5:
            print(f"No of products in cart : {len(l)}")
        elif ch==6:
            print(f"Alphabetically Sorted cart  : {sorted(l)}")
        elif ch==7:
            l.clear()
            print(f"Cleared cart : {l}")
        elif ch==8:
            exit(0)
        else:
            print("Enter proper operation")
cart()

=======
'''You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart
 
Cart Operations:
1. Add Product
2. Remove Product
3. Search Product
4. Display Cart
5. Count Products
6. Exit
 
Enter choice: 1
Enter product to add: Laptop
Product 'Laptop' added to cart.
 
Enter choice: 1
Enter product to add: Phone
Product 'Phone' added to cart.
 
Enter choice: 4
Cart: ['Laptop', 'Phone']
 
Enter choice: 3
Enter product to search: Phone
Yes, 'Phone' is in the cart.
 
Enter choice: 5
Total products in cart: 2 '''

def cart():
    l=[]
    print("Cart Operations:1. Add Product\t2. Remove Product\t3. Search Product\t4. Display Cart\t5. Count Products\t6. Sort the cart items alphabetically\t7. Clear the cart\t8. Exit\n")
    while True:
        ch=int(input("Enter choice : "))
        if ch==1:
            item=input("enter product to add : ")
            l.append(item)
            print(f"product {item} added to the cart")
        elif ch==2:
            item=input("enter product to remove : ")
            if item in l:
                l.remove(item)
                print(f"product {item} removed from the cart")
            else:
                print(f"product {item} is not present in the cart")
        elif ch==3:
            item=input("Enter product to search : ")
            if item in l:
                print(f"yes,{item} is present in the cart")
            else:
                print(f"no,{item} is not present in the cart")
        elif ch==4:
            print(f"Cart : {l}")
        elif ch==5:
            print(f"No of products in cart : {len(l)}")
        elif ch==6:
            print(f"Alphabetically Sorted cart  : {sorted(l)}")
        elif ch==7:
            l.clear()
            print(f"Cleared cart : {l}")
        elif ch==8:
            exit(0)
        else:
            print("Enter proper operation")
cart()

>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
