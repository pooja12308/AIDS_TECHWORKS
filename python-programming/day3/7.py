<<<<<<< HEAD
#display only unique elements

def uniq(l):
    fl={}
    for element in l:
        if element not in fl:
            fl[element]=1
        else:
            fl[element]+=1
    for k in fl:
        if fl[k]==1:
            print(k)
l=[1,1,2,3,4,5,5,6,6,6,6,7,9]
uniq(l)


def unique(l):
    uniqueset=set()
    for element in l:
        uniqueset.add(element)
    print(uniqueset)
l=[1,1,2,3,4,5,5,6,6,6,6,7,9]
=======
#display only unique elements

def uniq(l):
    fl={}
    for element in l:
        if element not in fl:
            fl[element]=1
        else:
            fl[element]+=1
    for k in fl:
        if fl[k]==1:
            print(k)
l=[1,1,2,3,4,5,5,6,6,6,6,7,9]
uniq(l)


def unique(l):
    uniqueset=set()
    for element in l:
        uniqueset.add(element)
    print(uniqueset)
l=[1,1,2,3,4,5,5,6,6,6,6,7,9]
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
unique(l)