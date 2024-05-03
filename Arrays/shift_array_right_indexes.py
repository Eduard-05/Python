array = [1, 4, 3, 7, 5, 2, 3]

for i in range(len(array) - 1, -1, -1):
    print(i)
    array[i] = array[i - 1]

array[0] = 0
print(array)
