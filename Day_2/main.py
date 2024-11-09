print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_with_tip = tip / 100 * bill + bill  
bill_per_person = bill_with_tip / people
total_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${total_amount}")