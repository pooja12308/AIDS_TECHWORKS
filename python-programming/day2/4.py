#current bill
def bill(t):
    if(t>1 and t<50):
        cbill=t*3.80
        print(cbill)
    elif(t>51 and t<100):
        cbill=(50*3.80)+(t-50)*4.20
        print(cbill)
    elif(t>101 and t<200):
        cbill=(50*3.80)+(t-50)*5.10
        print(cbill)
    elif(t>201 and t<300):
        cbill=(50*3.80)+(t-50)*6.30
        print(cbill)
    elif(t>300):
        cbill=(50*3.80)+(t-50)*7.50
        print(cbill)
t=int(input())
bill(t)