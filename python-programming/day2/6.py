#print n natural numbers
def printing(no):
    it=1
    pr=[]
    while it<=no:
        pr.append(it)
        it=it+1
    print(pr)
no=int(input())
printing(no)

def printalpha():
    al=[]
    for alpha in {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}:
        al.append(alpha)
    print(al)
printalpha()