a = 1
i = 0
zero_counter = 0
mult0 = 1
mult1 = None
mult2 = 1
prev_zero1 = False
prev_zero2 = False

while zero_counter != 3:

    a = int(input())

    if mult1 == None:
       mult1 = a

    if a == 0:
        if prev_zero2 == True:
            break
        if prev_zero1 == True:
            prev_zero2 == True
            mult2 = mult1 * 0
            zero_counter += 1
        if prev_zero1 == False:
            prev_zero1 = True
            mult2 = mult1 * 0
            zero_counter += 1

    if zero_counter == 3:
        break

    i += 1

    if a != 0:
        zero_counter = 0
        if i == 1:
            mult1 = mult2 * a
        else:
            mult1 = mult1 * mult2 * a

    print("multiplication of the row = ", mult1)
