#sum of natural numbers
def sumofn(n):
    i=1
    s=0
    while i<=n:
        s+=i
        i=i+1
    print(s)
n=int(input())
sumofn(n)