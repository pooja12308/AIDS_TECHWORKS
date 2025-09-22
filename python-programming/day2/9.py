#prime or not
def primecheck(n):
    count=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                count+=1
        if count>=1:
            print("Not prime")
        else:
            print("prime")
    else:
        print("error")
n=int(input())
primecheck(n)