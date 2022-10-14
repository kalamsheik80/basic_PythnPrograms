#tip calculator
amount = float(input('Enter the amount of rupees :₹'))
tip_percentage = float(input("Enter the tip_percentage : ")) / 100
tip_total=amount*tip_percentage
print("----------------------------------------------------------------------");
print("The amount you had to give the waiter as a tip amount:₹"+ str(tip_total));
total_amount=amount+tip_total
print("The total amount you need to pay for food :₹"+ str(total_amount));
print("----------------------------------------------------------------------");
