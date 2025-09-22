<<<<<<< HEAD
#displaying second largest number in list
def larg_fn():
    n=int(input("Enter no of elements"))
    l=[]
    for i in range(n):
        element=input()
        l.append(element)
    print(f"list : {l}")
    l.sort(reverse=True)
    print("second largest element in the list is ")
    print(l[1])

=======
#displaying second largest number in list
def larg_fn():
    n=int(input("Enter no of elements"))
    l=[]
    for i in range(n):
        element=input()
        l.append(element)
    print(f"list : {l}")
    l.sort(reverse=True)
    print("second largest element in the list is ")
    print(l[1])

>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
larg_fn()