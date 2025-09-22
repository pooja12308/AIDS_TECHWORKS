# Printing number in words
def numprint(n):
    nums = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
    l = []
    while n > 0:
        no = n % 10
        l.append(no)
        n = n // 10
    l.reverse()
    
    for i in range(len(l)):
        print(nums[l[i]], end=" ")
        
n = int(input("Enter a number: "))
numprint(n)
