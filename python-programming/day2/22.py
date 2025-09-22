#perfect number
def perf(n):
    sum=0
    org=n
    for i in range(1,n):
        if (n%i==0):
            sum+=i
    if (sum==org):
        print("Perfect number")
    else:
        print("Not perfect")

n=int(input())
perf(n)