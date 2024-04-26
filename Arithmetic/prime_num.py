divider = 0
i = 1

for number in range(101):
    while i <= number:
        if number % i == 0:
            divider += 1
        i += 1
    if divider == 2:
        print(number)
    divider = 0
    i = 1
