# %%
import random
word_list = ["apple", "banana", "pear", "orange", "grape"] # creates the list of fruits
print (word_list) # prints the list of fruits
# %%
word = random.choice(word_list) # chooses a word at random from the list
print (word) # prints random word
# %%
guess = input("Enter a single letter") # asks for user input
if len(guess) == 1 and guess.isalpha(): # checks input is 1 character and from the alphabet
    print ("Good guess!") 
else: 
    print ("Oops! That is not a valid input.")
print (guess) # prints user input