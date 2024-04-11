array = []
array_size = 0
array_max = None
array_min = None
amount_of_maximums = 0
amount_of_minimums = 0
zeros = 0
i = 0

print("Enter array size: ")
array_size = int(input())

while i < array_size:
    
    print("enter the number: ")
    array.append(int(input()))
    i += 1

i = 0

while i < array_size:

    if array_max == None or array_max < array[i]:
        amount_of_maximums = 1

    if array_max == None or array_max < array[i]:
        array_max = array[i]
        amount_of_maximums += 1

    i += 1

i = 0

while i < array_size:

    if array_min == None or array_min > array[i]:
        amount_of_minimums = 1

    if array_min == None or array_min > array[i]:
        array_min = array[i]
        amount_of_minimums += 1

    i += 1

i = 0

while i < array_size:
    if array[i] == 0:
        zeros += 1
    i += 1

print("amount of minimums: ", amount_of_minimums)
print("amount of maximums: ", amount_of_maximums)
print("ammount of zeros: ", zeros)