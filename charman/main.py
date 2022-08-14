# imports:

import random

# create a list of words:
word_list = ["dog", "train", "sky"]

# pick a random words:
random_word = random.choice(word_list)
print(random_word)

# fill the lenght with _ :
hidden_world = []
for x in random_word:
    hidden_world += '_'

print(hidden_world)
# while still have life points, or the word still has _:
