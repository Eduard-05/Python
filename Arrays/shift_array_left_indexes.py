array = [1, 4, 3, 7, 5, 2, 3]

for i in range(len(array) - 1):
    array[i] = array[i + 1]

array[len(array) - 1] = 0
print(array)
