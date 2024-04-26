number = None
digits = 0

number = int(input("Enter the number: "))

while number <= -1 or number >= 1:
    number = number / 10
    digits += 1

print("The amount of digits the number has: ", digits)
