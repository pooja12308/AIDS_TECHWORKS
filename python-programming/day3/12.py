<<<<<<< HEAD
#program to find total no of alphabets , digits or special characters in a string
def alpha(str):
    acount=0
    for i in str:
        if(i.isalpha()):
            acount+=1
    print(f"total alphabets : {acount}")

def digit(str):
    dcount=0
    for i in str:
        if (i.isdigit()):
            dcount+=1
    print(f"Total no of digits : {dcount}")

def specialchar(str):
    scount=0
    for i in str:
        if ((i.isalpha()==False) and (i.isdigit()==False)):
           scount+=1
    print(f"Total no of special characters : {scount}")

str=input("Enter string : ")
alpha(str)
digit(str)
=======
#program to find total no of alphabets , digits or special characters in a string
def alpha(str):
    acount=0
    for i in str:
        if(i.isalpha()):
            acount+=1
    print(f"total alphabets : {acount}")

def digit(str):
    dcount=0
    for i in str:
        if (i.isdigit()):
            dcount+=1
    print(f"Total no of digits : {dcount}")

def specialchar(str):
    scount=0
    for i in str:
        if ((i.isalpha()==False) and (i.isdigit()==False)):
           scount+=1
    print(f"Total no of special characters : {scount}")

str=input("Enter string : ")
alpha(str)
digit(str)
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
specialchar(str)