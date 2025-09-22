<<<<<<< HEAD
'''A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses
 — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
Write a Python program that:
Cleans each day's list (normalizes case, removes duplicates).
Prints the total number of unique attendees across all days.
Prints the list of attendees who attended all three days.
Prints the list of attendees who attended exactly one day.
Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
Produces a final report with counts and sorted lists for each of the above outputs.'''
def regs():
    d1=[]
    d2=[]
    d3=[]
    n1=int(input("No of day1 attendees"))
    for i in range(n1):
        email=input(f"email of attendee {i} :")
        d1.append(email.lower())
    s1=set(d1)
    n2=int(input("No of day2 attendees"))
    for i in range(n2):
        email=input(f"email of attendee {i} :")
        d2.append(email.lower())
    s2=set(d2)
    n3=int(input("No of day3 attendees"))
    for i in range(n3):
        email=input(f"email of attendee {i} :")
        d3.append(email.lower())
    s3=set(d3)
    print(f"attendees day1 : {s1}\t day2 : {s2}\t day3 : {s3}\n")
    print(f"Unique attendees : {s1|s2|s3}")
    print(f"Attendees that attended all three days : {s1&s2&s3}")
    one_day= s1-(s2|s3) | s2-(s1|s3) | s3-(s2|s1)
    print(f"attendees who attended exactly one day : {one_day}")
    p1=s1 & s2
    p2=s2 & s3
    p3=s3 & s1
    print(f"Pairwise overlap counts : {len(p1)},{len(p2)},{len(p3)}")
=======
'''A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses
 — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
Write a Python program that:
Cleans each day's list (normalizes case, removes duplicates).
Prints the total number of unique attendees across all days.
Prints the list of attendees who attended all three days.
Prints the list of attendees who attended exactly one day.
Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
Produces a final report with counts and sorted lists for each of the above outputs.'''
def regs():
    d1=[]
    d2=[]
    d3=[]
    n1=int(input("No of day1 attendees"))
    for i in range(n1):
        email=input(f"email of attendee {i} :")
        d1.append(email.lower())
    s1=set(d1)
    n2=int(input("No of day2 attendees"))
    for i in range(n2):
        email=input(f"email of attendee {i} :")
        d2.append(email.lower())
    s2=set(d2)
    n3=int(input("No of day3 attendees"))
    for i in range(n3):
        email=input(f"email of attendee {i} :")
        d3.append(email.lower())
    s3=set(d3)
    print(f"attendees day1 : {s1}\t day2 : {s2}\t day3 : {s3}\n")
    print(f"Unique attendees : {s1|s2|s3}")
    print(f"Attendees that attended all three days : {s1&s2&s3}")
    one_day= s1-(s2|s3) | s2-(s1|s3) | s3-(s2|s1)
    print(f"attendees who attended exactly one day : {one_day}")
    p1=s1 & s2
    p2=s2 & s3
    p3=s3 & s1
    print(f"Pairwise overlap counts : {len(p1)},{len(p2)},{len(p3)}")
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
regs()