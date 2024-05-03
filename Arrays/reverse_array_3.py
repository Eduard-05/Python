array = [1, 4, 3, 7, 5, 2, 3]

for i in range(len(array)//2):
    array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

print(array)
