
#exception - division by 0
def div(a,b):
    try :
        res=a/b
        print(f"Division of {a} by {b} is : {res}")
    except Exception as e:
        print("A number cannot be divided by zero")
        print(e)

print("Enter two numbers to find their divsion")
a=int(input())
b=int(input())
