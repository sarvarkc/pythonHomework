list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

final_list = []

for x in list1:
    if x not in list2:
        final_list.append(x)

for x in list2:
    if x not in list1:
        final_list.append(x)

print(final_list)