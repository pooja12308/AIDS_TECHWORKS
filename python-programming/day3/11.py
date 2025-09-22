<<<<<<< HEAD
#find length of given string using loops

def length(str):
    count=0
    for i in str:
        count+=1
    print(count)

str=input("Enter string")
length(str)

def compare(str1,str2):
    if (str1==str2):
        print("Same strings")
    else:
        print("Different Strings")
str1=input("Enter first string")
str2=input("Enter second string")
compare(str1,str2)

def concatenate(str1,str2):
    return str1+str2
str1=input("Enter string 1")
str2=input("Enter string 2")
=======
#find length of given string using loops

def length(str):
    count=0
    for i in str:
        count+=1
    print(count)

str=input("Enter string")
length(str)

def compare(str1,str2):
    if (str1==str2):
        print("Same strings")
    else:
        print("Different Strings")
str1=input("Enter first string")
str2=input("Enter second string")
compare(str1,str2)

def concatenate(str1,str2):
    return str1+str2
str1=input("Enter string 1")
str2=input("Enter string 2")
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
print(f"concatenated strings : {concatenate(str1,str2)}")