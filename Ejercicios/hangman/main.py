from hangman_art import logo, stages
from hangman_words import word_list
import random
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
lives = 6

for space in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Adivina la letra de la palabra: ").lower()

    if guess in display:
        print(stages[lives])
        print(f"Haz adivinado!!! {guess} ")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            # print(f"La letra {guess} si se encuentra en la palabra")
            display[position] = letter

    print(display)
    if guess not in chosen_word:
        print("No has adivinado la letra")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")
        elif lives != 0:
            print(f"Te quedan { lives} vidas")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Usted gana")

    print(stages[lives])
