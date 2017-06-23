# IPDB cheat sheet (see the actual lab below)
# from ipdb import set_trace; set_trace()
# n - next line
# c - continue with the rest of the code
# s - step
# q - quit
# l - list (show more lines of code)

"""
Lab: Guess The Number I

###### Delivery Method: Prompt and Demo

##### Goal

Write a text game in python for a single user to play 'Guess The Number' against the computer.

--------------------

##### Instructions

Here is how to play 'Guess The Number':

1. Display a welcome screen to the user.

1. The Computer chooses a random number between 1 and 2 billion.

1. After the computer chooses a number, the human attempts to guess the computer's secret number in as few guesses as possible. The human:


    - Guessses a number

    - The computer will respond with a message 'too high!' or 'too low!'

    - Repeat until the human guesses the exact number correctly.


1. score is kept like golf: lower is better!


#### Documentation

1. [Python Official: random.randint()](

https://docs.python.org/3/library/random.html)


1. [Python Official: Control Flow Tools](

https://docs.python.org/3/tutorial/controlflow.html)


1. [Python Official: time.sleep()](

https://docs.python.org/3/library/time.html#time.sleep)

#### Advanced

- Use `time.sleep()` to make the computer _think_, and pause momentarily.
- Ask for different difficulty levels by adjusting the maximum number.
- Play multiple rounds, prompting to 'play again?'.


#### Key Concepts

- Random Module
- Flow Control
- Event Loop Pattern
- PEP8
"""

import random
from time import sleep


def guess_number():
    print('Welcome to the game! Guess the number!')
    sleep(1)

    comp = random.randint(0, 100000000)
    # print(comp)

    user = int(input('Enter a number between 0 and 100000000: '))

    print('Computer is picking the number...')
    sleep(1)

    while comp != user:
        if user not in range(0, 100000000):
            print('Invalid input. Try again.')
            user = int(input('Enter a number between 0 and 100000000: '))
        elif comp > user:
            print('Too low!')
            question = str(input('Would you like to try again? (Y/N): ').upper())
            while question == 'Y':
                print(guess_number())
            else:
                print('Game over.')
                break
        elif comp < user:
            print('Too high!')
            question1 = str(input('Would you like to try again? (Y/N): ').upper())
            while question1 == 'Y':
                print(guess_number())
            else:
                print('Game over.')
                break
    else:
        print('Congratulations! You have won! Computer\'s guess was also: {}.'.format(comp))

print(guess_number())