import os
import random
from game_data import data
from art import logo, vs

# Sacar un personaje de la lista al azar


def random_element():
    """Returns a random element from the 'Data' list"""
    random_choice = random.choice(data)
    return random_choice

# Hacer la comparacion entre quien tiene mas seguidores


def more_followers():
    """Return who has the most followers"""
    if usuario_choice == "A":
        return computer_choice1.get('follower_count')
    if usuario_choice == "B":
        return computer_choice2.get('follower_count')


keep_playing = True
score = 0
print(logo)
while keep_playing:
    computer_choice1 = random_element()
    computer_choice2 = random_element()

    print(
        f"Compare 'A' : {computer_choice1.get('name')}, a {computer_choice1.get('description')}, from {computer_choice1.get('country')}  # {computer_choice1.get('follower_count')}")
    print(vs)
    print(
        f"Compare 'B' : {computer_choice2.get('name')}, a {computer_choice2.get('description')}, from {computer_choice2.get('country')}  # {computer_choice2.get('follower_count')}")
    usuario_choice = input("Who has more followers? Type 'A' or 'B': ")

    # Gana o pierde
    if usuario_choice == 'A' and more_followers() > computer_choice2.get('follower_count'):
        score += 1
        os.system('cls')
        print(f"you're right! Current score: {score}")

    elif usuario_choice == 'B' and more_followers() > computer_choice1.get('follower_count'):
        score += 1
        os.system('cls')
        print(f"you're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        keep_playing = False
