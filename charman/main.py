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
# print(type(hidden_world[0]))
# while still have life points, or the word still has _:
end_of_game = False
lives = 7
wrong_guess = []

while not end_of_game:
    guess = input("Pick a letter: ").lower()

    # avoid empty guess   
    while len(guess) == 0:
        print("Type a valid value (a-z )\n ")
        guess = input("Pick a letter: ").lower()


    # fill the letters in the hidden world (if correct)
    for index in range(len(random_word)): #counter
        if random_word[index] == guess:
            hidden_world[index] = guess
    
    # for wrong guess: 
    if guess not in random_word:
        wrong_guess += guess
        lives -= 1
        print(f"{stages[lives]}\n")
    print(f"You also tried the following letters: {wrong_guess}\n")        
    print(hidden_world)

    if lives == 0:
        end_of_game = True
        print("YOU DIED\n")   

    if not "_" in hidden_world:
        end_of_game = True
        print("YOU WIN\n")


   

