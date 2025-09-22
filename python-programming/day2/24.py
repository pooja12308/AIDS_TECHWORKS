#finding all primefactors
def primecheck(n):
    for i in range(2,n):
        c=0
        if n%i==0:
            c+=1
            if c>=1:
                return False
            else:
                return True
def pfactors(n):
    for i in range (1,n+1):
        if n%i==0:
            if primecheck(i):
                print(i)

n=int(input())
pfactors(n)