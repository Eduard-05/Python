array = [5, 7, 1, 3, 8, 9, 2, 4, 6]
sorted_array = []
is_sorted = False

def flip (fixed_element_index = None, array2 = []):
    flipped_array = []
    for j in range(fixed_element_index + 1):
        for i in range(fixed_element_index, -1, -1):
            flipped_array.append(array2[i])
        array2[j] = flipped_array[j]
    return array2

while len(array) != 0:
    min_value = min(array)
    min_value_index = array.index(min_value)
    if min_value_index == 0:
        sorted_array.append(min_value)
        array.pop(min_value_index)
    else:
        flip(min_value_index, array)

print(sorted_array)
