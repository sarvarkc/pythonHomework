def factors(num):
    for x in range(num):
        if num%(x+1)==0:
            print(x+1, "is factor of", num)

factors(int(input("Enter a positive integer: ")))