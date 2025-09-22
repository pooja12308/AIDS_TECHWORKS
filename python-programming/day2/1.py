#Enter day number of the week and we display day
def day(n):
    if n==1:
        print("Sunday")
    elif n==2:
        print("Monday")
    elif n==3:
        print("Tuesday")
    elif n==4:
        print("Wednesday")
    elif n==5:
        print("thursday")
    elif n==6:
        print("Friday")
    elif n==7:
        print("saturday")
    else:
        print("Invalid number")
n=int(input("Enter week day number"))
day(n)