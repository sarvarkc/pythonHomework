def isprime(n):
    nums = []
    for x in range(1, n):
        if x!=1 and x!=n and n % x == 0:
            nums.append(x)
    if len(set(nums)) == 0 and n != 1:
        print(True)
        nums.clear()
    else:
        print(False)
        nums.clear()

isprime(int(input("Enter an integer number: ")))