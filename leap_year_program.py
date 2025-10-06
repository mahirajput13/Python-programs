#checking if the entered year is leap or not
year = int(input("Enter any year to check if it is leap or not : "))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
   print("Leap Year")
else:
    print("Not Leap Year")
