#first and last digit
def firstlast(n):
        l=n%10
        n=n//10
        print(l)
        while n>0:
            f=n%10
            n=n//10
        print(f)
firstlast(2345)
        