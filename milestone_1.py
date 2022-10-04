# %%
import random
word_list = ["apple", "banana", "pear", "orange", "grape"] # creates the list of fruits
print (word_list)
# %%
word = random.choice(word_list) # chooses a word at random from the list
print (word)
# %%
guess = input("Enter a single letter")
if len(guess) == 1 and guess.isalpha():
    print ("Good guess!")
else: 
    print ("Oops! That is not a valid input.")
print (guess)
# %%
