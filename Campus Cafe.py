
"""
Psuecde:
1) Display the menu
2) Ask the user how many of each item they would like and how much tip they would like to give
3)calculate the plain price witout tax or tip included
4) compute the total amount that has to get paid including tip and tax
5) round all the prices to the nearest cent
6) Display the receipt
"""

"""
Author: Michelle Levy
Date: 09/21/2025
Purpose: This is a cafe where users will initially be given a menu of all the iems in the cafe. The user will put in what they would like to order and then the program will calculate the totals and return the receipt t the user.
"""

#Displays the menu too the user
print("==Campus Cafe===")
print("Coffee: $2.25")
print("Muffin: $2.75")
print("Bagels: $2.50")

#Will ask user how much of each item they would like and how much tip
try:
    number_of_coffees = input("How many coffees?")
    print(f"{number_of_coffees} coffees")
    number_of_muffins = input("How many muffins?")
    print(f"{number_of_muffins} muffins")
    number_of_bagels = input("How many bagels?")
    print(f"{number_of_bagels} bagels")
    tip_percent = input("Enter tip precent (e.g., 10 for 10%):")
    print(f"{tip_percent} percent tip")
except ValueError:
    print("Sorry! Number is incvalid")
    

#Variables for the price of each individual item
coffee_unitprice = 2.25
muffins_unitprice = 2.75
bagels_unitprice = 2.50
tax_rate= 0.08875



"""
given the unit price of each item and the amount of each item the user wants, line_total() will first calculate the line totals of each item by multipling the unit price by how much of it the user wants
and then will add up the line totals.
"""
def line_total(number_of_coffees, number_of_muffins,number_of_bagels, coffee_unitprice, muffins_unitprice, bagels_unitprice):
    coffee_price = int(number_of_coffees)*coffee_unitprice
    muffins_price = int(number_of_muffins)*muffins_unitprice
    bagels_price = int(number_of_bagels)*bagels_unitprice
    return coffee_price, muffins_price, bagels_price
#the total prices the user has to pay for each item 
coffee_price, muffins_price, bagels_price = line_total(number_of_coffees, number_of_muffins,number_of_bagels, coffee_unitprice, muffins_unitprice, bagels_unitprice)
#plain subtotal, adds all the line totals
subtotal= coffee_price+muffins_price+bagels_price

"""
This function calculates the final total including the tax and the tip by first calculating the total and tip, and then adding the tax and tip to the subtotal
"""
def compute_totals(subtotal, tax_rate, tip_percent):
    
    tax = subtotal * tax_rate
    tip = subtotal * (int(tip_percent) / 100)
    total = subtotal + tax + tip
    return tax, tip, total
"""
This function rounds all prices to the nearest cent.
"""
def format_currency(tax,tip,total):
    tax,tip,total=compute_totals(subtotal, tax_rate, tip_percent)
    ntax= round(tax,2)
    ntip= round(tip,2)
    ntotal=round(total,2)
    return ntax,ntip,ntotal
"""'
This function prints out the final receipt that will be diplayed to the user including all of the line totals, tax, tip, and final total
"""
def print_receipt():
    tax,tip,total=compute_totals(subtotal, tax_rate, tip_percent)
    ntax,ntip,ntotal = format_currency(tax,tip,total)
    print("--- Receipt ---")
    print(str(number_of_coffees)+ "xCoffee", "@$2.25=", "$"+ str(coffee_price))
    print(str(number_of_muffins)+ "xMuffins", "@2.75=", "$"+str(muffins_price))
    print(str(number_of_bagels)+ "xBagels", "@2.50=", "$"+str(bagels_price))
    print("Subtotal:", "$"+str(subtotal))
    print("Tax(8.875%):", "$"+str(ntax))
    print("Tip(10%):", "$"+str(ntip))
    print("TOTAL:", "$"+str(ntotal))
    print("Thank you!")



#Calls the function print_receipt()
print_receipt()







