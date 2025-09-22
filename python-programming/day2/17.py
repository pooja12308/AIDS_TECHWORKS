#print all primes between 1 to n

def primeprint(n):
    for i in range(1,n+1):
        count=0
        for j in range(1,n+1):
            if (i%j==0):
                count+=1
        if (count==2):
            print(i)
n=int(input())
primeprint(n)