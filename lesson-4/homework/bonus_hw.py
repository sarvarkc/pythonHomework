import random

x = 0
y = 0
choices = ['rock','paper','scissors']

while x<5 or y<5:
    my_choice = input("Choose between rock, paper or scissors: ")
    bot_choice = random.choice(choices)

    if my_choice == 'rock' and bot_choice == 'paper':
        y += 1
        print("Bot won","\nYour score is:", x, "\nBot's score is:", y)
    elif my_choice == 'paper' and bot_choice == 'scissors':
        y += 1
        print("Bot won","\nYour score is:", x, "\nBot's score is:", y)
    elif my_choice == 'scissors' and bot_choice == 'rock':
        y += 1
        print("Bot won","\nYour score is:", x, "\nBot's score is:", y)  
    elif my_choice == bot_choice:
        print("Draw","\nYour score is:", x, "\nBot's score is:", y)
    else:
        x += 1
        print("You won","\nYour score is:", x, "\nBot's score is:", y)

    if x == 5:
        print("You are the winner")
        break
    elif y == 5:
        print("Bot is a winner")
        break