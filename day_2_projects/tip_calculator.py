print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# total = (bill / people) * (tip / int(100))
total = (bill * (tip / int(100) ) +bill) / people
print(f"Each person should pay: ${round(total, 2)}")