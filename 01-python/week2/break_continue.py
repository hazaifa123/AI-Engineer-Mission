while True:
    no = int(input("enter a number:"))
    if no == 0:
        break
    print(f"no:{no}")
    ## progam 2 
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)    