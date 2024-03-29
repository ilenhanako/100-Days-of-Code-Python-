print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

# there are two approaches, note how intuitive the variables are named
# using the random function, thereafter rounding to 2 decimal places
# you will see the numeric two just before the closing parenthesis

# long form
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# short form
final_amount = round(bill * (1 + tip / 100) / people, 2)

print(f"Each person should pay: ${final_amount}")