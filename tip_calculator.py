# welcome msg to the user
print("Welcome to the tip calculator")

#asking user to enter the details
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? \n10$, 12$ or 15$\n"))
people = int(input("How many people to split the bill? \n"))

#calculating amount of each person
amount = (bill + tip)/people
print("Each person should pay : ", amount)