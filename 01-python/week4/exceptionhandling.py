try:
    no = int(input("enter a number"))
    no2 = int(input("enter a number"))
    result = no / no2
    print(result)
except ZeroDivisionError:
    print("Bhai, zero se divide nahi kar sakte!")