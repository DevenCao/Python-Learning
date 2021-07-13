'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

1.Keep the game going until the user types “exit”
2.Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

from random import randint

print("【* Guess Number *】 \nGiven a number within 1-9, try to guess it(Type 'exit' to quit any time)")

play = True

while play:
    goal = randint(1, 9)
    count = 0
    while play:
        guess = input("Enter your  guess: ").lower()
        if guess == "exit":
            play = False
            break
        if not guess.isdigit():
            print("Enter a digit 1-9")
            continue
        count += 1
        guess = int(guess)
        if guess == goal:
            print("You got it! Your total guesses is %d"%count)
            if input("Type 'exit' to quit or any to continue").lower() == "exit":
                play = False
            break
        elif guess < goal:
            print("Your guess less than goal")
        else:
            print("Your guess more than goal")
