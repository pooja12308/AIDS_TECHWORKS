#find all factors of a number
def factors(n):
    l=[]
    for i in range(1,n+1):
        if(n%i)==0:
            l.append(i)
    print(l)
n=int(input())
factors(n)