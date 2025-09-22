#factorial
def fact(n):
    while n>0:
        if n>1:
            return n*fact(n-1)
        else:
            return 1
n=int(input())
print(fact(n))
