#mathematical table
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
        i=i+1
        
n=int(input())
table(n)