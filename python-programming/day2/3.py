#student grades
def grading(marks):
    if(marks>40):
        print("Pass...Grade printed below")
        if(marks<50):
            print("C")
        elif (marks>51 and marks <70):
            print("B")
        elif(marks>71 and marks<80):
            print("A")
        elif(marks>80):
            print("Distinction")
    else:
        print("Fail")
marks=int(input("Enter student marks"))
grading(marks)