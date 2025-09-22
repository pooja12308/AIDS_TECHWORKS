<<<<<<< HEAD
#program to search and count all occurrences of a character in a given string

def occur(str,ch):
    chcount=0
    pos=[]
    for i in range(len(str)):
        if str[i]==ch:
            chcount+=1
            pos.append(i)
            print(f"{str[i]} : at {pos} : {chcount}")
str=input("Enter string")
ch=input("Enter character")
=======
#program to search and count all occurrences of a character in a given string

def occur(str,ch):
    chcount=0
    pos=[]
    for i in range(len(str)):
        if str[i]==ch:
            chcount+=1
            pos.append(i)
            print(f"{str[i]} : at {pos} : {chcount}")
str=input("Enter string")
ch=input("Enter character")
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
occur(str,ch)