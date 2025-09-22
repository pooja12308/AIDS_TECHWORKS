#sum of factorials of digits=original number
def fact(n):
    while n>0:
        if n>1:
            return n*fact(n-1)
        else:
            return 1
def facsum(n):
    l=[]
    org=n
    sum=0
    while n>0:
        no=n%10
        l.append(no)
        n=n//10
    for i in l:
        sum+=fact(i)
    if sum == org:
        print("Strong")
    else:
        print("Not strong")

n=int(input())
facsum(n)