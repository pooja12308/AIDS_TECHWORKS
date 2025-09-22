#program that inputs any character and checks whether its alphabet,digit or special character
def check(n):
    if n.isalpha():
        print("Alphabet")
    elif n.isnumeric():
        print("Number")
    elif n in {"!","@","$","%","^","&","*","(",")","*","/","-","+"}:
        print("Special character")
n=input()
check(n)