min_num = None
max_num = None
min_prev = None
max_prev = None
a = 1
amm_of_min = 0
amm_of_max = 0

while a != 0:

    a = int(input())

    if a == 0:
        break

    if min_num == None:
        min_num = a
        min_prev = a
    if min_num == a and min_prev == a:
        amm_of_min += 1
    if min_num > a:
        min_num = a
        min_prev = a
        amm_of_min = 1

    if max_num == None:
        max_num = a
        
    if max_num == a and max_prev == a:
        amm_of_max += 1
    if max_num < a:
        max_num = a
        max_prev = a
        amm_of_max = 1

print("min = ", min_num)
print("ammount of min numbers = ", amm_of_min)
print("max = ", max_num)
print("ammount of max numbers = ", amm_of_max)
