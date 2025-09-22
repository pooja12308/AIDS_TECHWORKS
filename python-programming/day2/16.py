#printing stars
for i in range(1,6): #rows
    for j in range(1,6): #cols
        if i==j:
            print("$",end=" ")
        elif (i+j==6):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()