min_num = None
max_num = None
a = 1
inMin = 0
inMax = 0
num_of_inputs = 0

while a != 0:

    a = int(input())

    if a == 0:
        break

    num_of_inputs += 1

    if min_num == None:
        min_num = a
        inMin = num_of_inputs
    if min_num > a:
        min_num = a
        inMin = num_of_inputs

    if max_num == None:
        max_num = a
        inMax = num_of_inputs
    if max_num < a:
        max_num = a
        inMax = num_of_inputs

print("min = ", min_num)
print("index of min = ", inMin)
print("max = ", max_num)
print("index of max = ", inMax)
