#strong numbers sequence
#sum of factorials of digits=original number
def fact(n):
    while n>0:
        if n>1:
            return n*fact(n-1)
        else:
            return 1
def facseq(n):

    for i in range(1,n+1):
        l=[]
        org=n
        sum=0
        while i>0:
            no=i%10
            l.append(no)
            i=i//10
            for j in l:
                sum+=fact(j)
            if sum == org:
                print(org)

n=int(input())
facseq(n)

.....