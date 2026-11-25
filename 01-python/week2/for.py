number = int(input("Enter a number: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")

## program 2 n = int(input("Enter a number: "))

total = 0
line = ""

for i in range(1, n + 1):
    total += i
    if i < n:
        line += f"{i}+"
    else:
        line += f"{i}"

print(f"{line} = {total}")