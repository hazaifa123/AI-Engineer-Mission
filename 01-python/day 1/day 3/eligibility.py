cgpa = float(input("Enter your CGPA: "))
attendance = int(input("Enter your attendance: "))

if cgpa >= 3.5 and attendance >= 80:
    print("You are eligible for scholarship")
else:
    print("You are not eligible for scholarship")