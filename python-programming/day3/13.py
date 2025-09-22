<<<<<<< HEAD
#program to count total vowels and consonants in a string

def voco_count(str):
    vcount=0
    ccount=0
    ocount=0
    v_l=['a','e','i','o','u','A','E','I','O','U']
    for i in str:
        if(i.isalpha()):
            if i in v_l:
                vcount+=1
            else:
                ccount+=1
        else:
            ocount+=1
    print(f"Total no of vowels : {vcount}")
    print(f"Total no of consonants : {ccount}")

str=input("Enter string : ")
=======
#program to count total vowels and consonants in a string

def voco_count(str):
    vcount=0
    ccount=0
    ocount=0
    v_l=['a','e','i','o','u','A','E','I','O','U']
    for i in str:
        if(i.isalpha()):
            if i in v_l:
                vcount+=1
            else:
                ccount+=1
        else:
            ocount+=1
    print(f"Total no of vowels : {vcount}")
    print(f"Total no of consonants : {ccount}")

str=input("Enter string : ")
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
voco_count(str)