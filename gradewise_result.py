#defining result of students as follows
# if percentage btwn 90 to 100 print grade a, 80 to 90 print grade b, 70 to 80 print c grade otherwise print grade d
per = float(input("Enter the marks of the student : "))
if per >= 90 and per <= 100:
    print("Grade : A ")
elif per >= 80 and per <= 90:
    print("Grade : B ")
elif per >= 70 and per <= 80:
    print("Grade : C ")
else:
    print("Grade : D ")