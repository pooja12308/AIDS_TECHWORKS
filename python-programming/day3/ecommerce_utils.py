<<<<<<< HEAD
'''You are asked to build a simple E-commerce Billing System using Python modules.
Create a module file named ecommerce_utils.py that contains the following functions:
apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
generate_invoice(cart, discount_percent=10, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
Create a main program file named main.py that:
Imports the ecommerce_utils module.
Creates a shopping cart (dictionary) with at least 3 products.
Calls the module functions to generate an invoice.
Expected Output Example:
------ INVOICE ------
Laptop          : ₹55000
Phone           : ₹30000Headphones      : ₹2000
---------------------
Subtotal: ₹87000
After 10% discount: ₹78300.0
After 18% GST: ₹92454.00
---------------------
Thank you for shopping with us!'''

def apply_discount(price,discount_percent):
    discounted_price=price-((discount_percent/100)*price)
    return discounted_price

def add_gst(price,gst_percent=18):
    new_price=price+((gst_percent/100)*price)
    return new_price

def generate_invoice(cart,discount_percent=10,gst_percent=18):
    print("----- INVOICE -----")
    for item in cart:
        print(f"\t{item} : {cart[item]}")
    print("\t----------")
    subtotal=sum(cart.values())
    print(f"\tSubtotal : {subtotal}")
    discountprice=apply_discount(subtotal,discount_percent)
    print(f"\tAfter 10% discount : {discountprice}")
    gstprice=add_gst(discountprice,gst_percent)
    print(f"\tAfter 18% GST : {gstprice}")
    print("\t----------")
    print("Thankyou for shopping with us!")
=======
'''You are asked to build a simple E-commerce Billing System using Python modules.
Create a module file named ecommerce_utils.py that contains the following functions:
apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
generate_invoice(cart, discount_percent=10, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
Create a main program file named main.py that:
Imports the ecommerce_utils module.
Creates a shopping cart (dictionary) with at least 3 products.
Calls the module functions to generate an invoice.
Expected Output Example:
------ INVOICE ------
Laptop          : ₹55000
Phone           : ₹30000Headphones      : ₹2000
---------------------
Subtotal: ₹87000
After 10% discount: ₹78300.0
After 18% GST: ₹92454.00
---------------------
Thank you for shopping with us!'''

def apply_discount(price,discount_percent):
    discounted_price=price-((discount_percent/100)*price)
    return discounted_price

def add_gst(price,gst_percent=18):
    new_price=price+((gst_percent/100)*price)
    return new_price

def generate_invoice(cart,discount_percent=10,gst_percent=18):
    print("----- INVOICE -----")
    for item in cart:
        print(f"\t{item} : {cart[item]}")
    print("\t----------")
    subtotal=sum(cart.values())
    print(f"\tSubtotal : {subtotal}")
    discountprice=apply_discount(subtotal,discount_percent)
    print(f"\tAfter 10% discount : {discountprice}")
    gstprice=add_gst(discountprice,gst_percent)
    print(f"\tAfter 18% GST : {gstprice}")
    print("\t----------")
    print("Thankyou for shopping with us!")
>>>>>>> 42abb7be31d0cacdc1d22869d9377a34cb01a75d
