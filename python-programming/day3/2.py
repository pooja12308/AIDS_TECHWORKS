<<<<<<< HEAD
#display only negative values in the list

def find_neg():
    n=int(input("Enter no of elements"))
    l=[]
    for i in range(n):
        element=input()
        l.append(element)
    print("Displaying only negative values")
    for i in range(n):
        if(int(l[i])<0):
            print(l[i])

=======
#display only negative values in the list

def find_neg():
    n=int(input("Enter no of elements"))
    l=[]
    for i in range(n):
        element=input()
        l.append(element)
    print("Displaying only negative values")
    for i in range(n):
        if(int(l[i])<0):
            print(l[i])

>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
find_neg()