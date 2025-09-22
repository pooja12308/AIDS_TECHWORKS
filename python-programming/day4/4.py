<<<<<<< HEAD
'''You are asked to design a simple Payment System that can handle different payment methods.
Requirements:
Create a base class Payment with a method pay(amount).
Create three child classes that override the pay(amount) method:
CashPayment → print "Paid ₹<amount> in cash"
CardPayment → print "Paid ₹<amount> using credit/debit card"
UPIPayment → print "Paid ₹<amount> using UPI"
Task:
Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
Loop through them and call pay(1000).
Each object should print a different message.'''

class payment:
    def pay(self,amount):
        pass
class cashpayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} in cash")

class cardpayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")

class UPIpayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")

list=[cashpayment(),cardpayment(),UPIpayment()]
for type in list:
=======
'''You are asked to design a simple Payment System that can handle different payment methods.
Requirements:
Create a base class Payment with a method pay(amount).
Create three child classes that override the pay(amount) method:
CashPayment → print "Paid ₹<amount> in cash"
CardPayment → print "Paid ₹<amount> using credit/debit card"
UPIPayment → print "Paid ₹<amount> using UPI"
Task:
Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
Loop through them and call pay(1000).
Each object should print a different message.'''

class payment:
    def pay(self,amount):
        pass
class cashpayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} in cash")

class cardpayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")

class UPIpayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")

list=[cashpayment(),cardpayment(),UPIpayment()]
for type in list:
>>>>>>> d283d138443d18f417b8952a56da15ce85d46d2b
    type.pay(1000)