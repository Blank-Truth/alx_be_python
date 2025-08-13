number = int(input("Enter a number to see its multiplication table:"))
for i in range(11):
    if i == 0:
        continue
    if i <= 10:
        print(f"{number} * {i} = {number * i}")