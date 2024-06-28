from random import randrange
array = [3, 2, 8, 1, 7, 9, 4, 6, 5]
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand1 = None
rand2 = None
iterations = 0

while array != sorted_array:
    iterations += 1
    rand1 = randrange(len(array))
    rand2 = randrange(len(array))
    array[rand1], array[rand2] = array[rand2], array[rand1]

print(array)
print("number of iterations = ", iterations)
