print("Welcome to the tip calculator.")

amount = float(input("What was the total bill? R"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

amount_split = ((amount*(tip/100)) + amount)/people

print(f"Each person should pay: R{round(amount_split,2)}")