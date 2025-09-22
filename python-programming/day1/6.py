
n = int(input("Enter number of students: "))
s_num = [0] * n
s_name = [""] * n
m1 = [0] * n
m2 = [0] * n
m3 = [0] * n
tot = [0] * n
avg = [0.0] * n
for i in range(n):
    s_num[i] = int(input("Enter student number: "))
    s_name[i] = input("Enter student name: ")
    m1[i] = int(input("Enter marks for M1: "))
    m2[i] = int(input("Enter marks for M2: "))
    m3[i] = int(input("Enter marks for M3: "))
    tot[i] = m1[i] + m2[i] + m3[i]
    avg[i] = tot[i] / 3.0
for i in range(n):
    print("Student", i + 1)
    print("Number:", s_num[i])
    print("Name:", s_name[i])
    print("M1:", m1[i])
    print("M2:", m2[i])
    print("M3:", m3[i])
    print("Total:", tot[i])
    print("Average: {:.2f}".format(avg[i]))
    print()