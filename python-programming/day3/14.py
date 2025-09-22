<<<<<<< HEAD
#write program to count total no of words in a string 

def totwords(str):
    wcount=1
    for i in str:
        if i==" ":
            wcount+=1
    print(wcount)

str=input("Enter string : ")
totwords(str)

stri=input("Enter string to find words using split()")
words=stri.split()
=======
#write program to count total no of words in a string 

def totwords(str):
    wcount=1
    for i in str:
        if i==" ":
            wcount+=1
    print(wcount)

str=input("Enter string : ")
totwords(str)

stri=input("Enter string to find words using split()")
words=stri.split()
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
print(len(words))