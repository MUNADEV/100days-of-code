print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))

total_tip = bill * (tip/100)
total_bill = bill + total_tip;
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")