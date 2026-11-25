for number in range(1, 6):        # Outer loop — 1 se 5 tak
    print(f"Table of {number}:")  # Table ka heading
    for i in range(1, 11):        # Inner loop — 1 se 10 tak
        product = number * i
        print(f"{number} x {i} = {product}")
    print()                       # Har table ke baad khali line
    # program 2
    for i in range(1, 6):
     for j in range(i):
        print("*", end="")
    print()