#sum of digits
def sumofdigits(n):
    count=0
    while n>0:
        count+=n%10
        n=n//10
    print(count)

n=int(input())
sumofdigits(n)