array = []
array_length = 0
deleted_element = 0
ammount_of_numbers = 0

array_length = int(input("Type array length: "))

for element in range(array_length):
    array.append(int(input("Enter the number: ")))

deleted_number = int(input("Which number would you like to delete? "))

for i in range(array_length):
    if array[i] == deleted_number:
        ammount_of_numbers += 1
    print(i)

for k in range(ammount_of_numbers):
    array.remove(deleted_number)

print(array)
