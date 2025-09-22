# Armstrong number check
def arm(n):
    original = n 
    l = []
    sum = 0  
    while n > 0:
        no = n % 10
        l.append(no)
        n = n // 10    
    for i in l:
        sum +=i ** 3    
    if sum == original:
        print("Yes, Armstrong Number")
    else:
        print("No, Not Armstrong")

n = int(input("Enter a number: "))
arm(n)
