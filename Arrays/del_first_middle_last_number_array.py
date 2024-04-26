array = []
length_of_array = 0
element = 0

length_of_array = int(input("Enter the lenght of array: "))

for element in range(length_of_array):
    array.append(int(input("Enter the number: ")))

array.pop(length_of_array - 1)
array.pop(round(length_of_array / 2))
array.pop(0)

print(array)
