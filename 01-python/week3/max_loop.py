marks = [80, 75, 90, 65, 85]
maximum = marks[0]

for mark in marks:
    if mark > maximum:
        maximum = mark

print("Maximum:", maximum)