min_num = None
max_num = None
a = 1
inMin = 0
inMax = 0
num_of_inputs = 0

while a != 0:

    if min_num == None or min_num > a:
        min_num = a
        inMin = num_of_inputs

    if max_num == None or max_num < a:
        max_num = a
        inMax = num_of_inputs

    a = int(input())
    num_of_inputs += 1


print("min = ", min_num)
print("index of min = ", inMin)
print("max = ", max_num)
print("index of max = ", inMax)
