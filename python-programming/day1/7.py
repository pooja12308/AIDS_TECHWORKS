n=int(input("Enter the conxumer number"))
name=input("Enter consumer name")
pread=int(input("Enter present month reading"))
lread=int(input("Enter last month reading"))
total_units=pread-lread
current_bill=total_units*3.80
print(n,"\t")
print(name,"\t")
print(pread,"\t")
print(lread,"\t")
print(total_units,"\t")
print(current_bill,"\t")
      