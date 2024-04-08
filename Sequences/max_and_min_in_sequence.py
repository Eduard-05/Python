min_num = None
max_num = None
a = 1

while a != 0:
    a = int(input())

    if min_num == None or min_num > a:
        min_num = a

    if max_num == None or max_num < a:
        max_num = a

print("min = ", min_num)
print("max = ", max_num)
