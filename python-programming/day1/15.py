
#leapyear
def leap(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
        return True
    else:
        return False
print(leap(2004))

#character is alphabet or not
def alpha(a):
    if a.isalpha():
        return True
    else:
        return False
print(alpha("c"))

#vowel or consonant
def vorc(c):
    if(c in {"a","e","i","o","u"}):
        return "Vowel"
    else:
        return "Consonant"
print(vorc("i"))