# imports:
import random
from hangman_art import stages, logo
from hangman_words import word_list

# create a list of words:
full_list = word_list

# pick a random words:
random_word = random.choice(full_list)
print(random_word)

# fill the lenght with _ :
hidden_world = []
for x in random_word:
    hidden_world += '_'

print(f"The hidden world is: {hidden_world}")

# while still have life points, or the word still has _:
end_of_game = False
lives = 1

while not end_of_game:
    picked_letter = input("Pick a letter: ")

    # fill the letters in the hidden world (if correct)


