import random

random_number = random.randint(1, 100)
i = 0

while i < 11:
    my_num = int(input())
    if my_num > random_number:
        print("Too high!")
    elif my_num < random_number:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
    if i == 9:
        print("You lost. Want to play again?")
        ask = input()
        if ask.lower() in ['ok', 'y', 'yes']:
            i = -1
            random_number = random.randint(1, 100)
        else:
            break 
    i += 1

    