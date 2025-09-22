#checking if given number is even or odd
def check_even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
res=check_even_odd(7)
print(res)

#Negative/positive
def negpos(n):
    if(n<0):
        return "Negative"
    else:
        return "positive"
print(negpos(-9))

#divisible by 5&11
def div511(n):
    if(n%5==0 and n%11==0):
        return True
    else:
        return False
res=div511(110)
if(res==True):
    print("Yes")
else:
    print("No")