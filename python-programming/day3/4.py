<<<<<<< HEAD
def count_eo():
    n = int(input("Enter no of elements: "))
    l = []
    ecount = 0
    ocount = 0
    zcount = 0
    
    for i in range(n):
        element = int(input())
        l.append(element)
    
    for num in l:
        if num == 0:
            zcount += 1
        elif num % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    
    print(f"No of evens: {ecount}")
    print(f"No of odds: {ocount}")
    print(f"No of zeros: {zcount}")

count_eo()
=======
def count_eo():
    n = int(input("Enter no of elements: "))
    l = []
    ecount = 0
    ocount = 0
    zcount = 0
    
    for i in range(n):
        element = int(input())
        l.append(element)
    
    for num in l:
        if num == 0:
            zcount += 1
        elif num % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    
    print(f"No of evens: {ecount}")
    print(f"No of odds: {ocount}")
    print(f"No of zeros: {zcount}")

count_eo()
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
