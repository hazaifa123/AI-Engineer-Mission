try:
    with open("diary.txt","r") as file:
        read=file.read()
        print(read)
except FileNotFoundError:
    print("not found")

