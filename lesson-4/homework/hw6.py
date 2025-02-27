nums = []

for x in range(1, 101):
    for y in range(1, x):
        if y!=1 and y!=x and x % y == 0:
            nums.append(y)
    if len(set(nums)) == 0 and x != 1:
        print(x)
        nums.clear()
    else:
        nums.clear()