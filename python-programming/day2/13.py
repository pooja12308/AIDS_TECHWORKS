#sum of first and last digit
print(2//10)
def sumfl(n):
    l=n%10
    n=n//10
    while n>0:
        f=n%10
        n=n//10
    add=f+l
    print(add)
n=int(input())
sumfl(n)