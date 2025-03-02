def invest(amount, rate, years):
    for x in range(years):
        amount = round(amount + amount*rate/100,2)
        print("year ", x+1, ": $", amount)
    
invest(int(input("Enter the amout: ")),int(input("Enter the rate: ")),int(input("Enter years: ")))