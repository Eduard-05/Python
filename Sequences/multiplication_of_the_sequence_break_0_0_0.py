a = 1
zero_counter = 0
mult1 = 1
mult2 = 1
prev_zero1 = False
prev_zero2 = False

while zero_counter != 3:

    a = int(input())

    if zero_counter == 2 and a == 0:
        zero_counter += 1
    if zero_counter == 1 and a == 0:
        mult2 = mult1 * 0
        zero_counter += 1
    if a == 0 and zero_counter == 0:
        zero_counter += 1
        mult2 = mult1 * 0

    if a != 0:
        zero_counter = 0
        mult1 = mult1 * mult2 * a

print("multiplication of the row = ", mult1)