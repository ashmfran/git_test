"""
Author: Ashley Francis
Date written: 02/17/2025
Assignment: Module 05 Programming Assignment Part II
This program is designed to define a function that generates a
random number in the range from 1 to 100. The program will prompt the user
to input a number to guess what the number is. If the user enters a number
that is too high the program will output a message 'too high, try again'.
If the user enters a number that is too low the program will output the
message 'too low, try again'. If the user enters the correct number the program
will output a message congratulating the user.
"""

import random

def guessing_game():
    random_number = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > random_number:
            print("Too high, try again.")
        elif guess < random_number:
            print("Too low, try again.")
        else:
            print("Congratulations! You've guessed the number.")
            random_number = random.randint(1, 100)

guessing_game()
