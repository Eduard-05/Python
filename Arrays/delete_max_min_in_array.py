array = []
i = 0
array_size = 0
array_max = None
array_min = None

print("enter array size: ")

array_size = int(input())

while i < array_size:
    
    print("enter the number: ")
    array.append(int(input()))
    i += 1

i = 0
array_max = array[1]
array_min = array[1]

while i < array_size:

    if array[i] > array_max:
        array_max = array[i]
    i += 1

i = 0

while i < array_size:

    if array[i] < array_min:
        array_min = array[i]
    i += 1

i = 0

while i < array_size:
    if array_min == array[i] or array_max == array[i]:
        array.pop(i)
        # array_size віднімаємо, бо довжина масиву змінилася після вирізання елементу. змінну і віднімаємо, щоби індекс не попадав на число, яке ще не було перевірене іфом
        array_size -= 1
        i -= 1
    i += 1

print("array min: ", array_min)
print("array max: ", array_max)

print("cut array: ", *array)