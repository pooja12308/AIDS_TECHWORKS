
#program to find simple interest and total amount
p=int(input("Enter principal amount"))
t=eval(input("Enter time period in years"))
rate=int(input("Enter rate"))
si=(p*t*rate)/100
total_amt=p+si
print(total_amt)
