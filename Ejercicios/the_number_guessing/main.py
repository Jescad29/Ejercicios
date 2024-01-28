import random
from art import logo
import os


def the_number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")

    def random_number():
        """Choose a number from 1 to 100"""
        return random.randint(1, 100)
    chosen_random_number = random_number()
    print(chosen_random_number)

    lives = 5
    difficulty_game = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty_game == "easy":
        lives += 5
        # print(f"You have {lives} attempts remaining to guess the number.")
    choice_continue = True
    while choice_continue:
        choice_number = int(input("make a guess: "))

        if choice_number == chosen_random_number:
            print(
                f"The number is {chosen_random_number}, you guessed the number you win!!!")
            choice_continue = False
        elif lives == 0:
            print(
                f"The number is {chosen_random_number}, you've run out of guesses, you lose. ")
            choice_continue = False
        elif choice_number != chosen_random_number:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
            if choice_number > chosen_random_number:
                print("Too high")
            elif chosen_random_number > choice_number:
                print("Too low")

    if input("Do you want to play again? types 'yes' or 'no' to exit") == "yes":
        os.system("cls")
        the_number_guessing_game()


the_number_guessing_game()
