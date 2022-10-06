# %%
def check_guess(guess): # defines the guess checking function, passing guess as the argument
    guess = guess.lower() # turns guess into lowercase
    import random # imports random module
    word_list = ["apple", "banana", "pear", "orange", "grape"] # creates the list of fruits
    word = random.choice(word_list) # chooses a word at random from the list

    if guess in word: # condition where guess is part of the random word
        print(f"Good guess! {guess} is in the word.") 
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# %%
def ask_for_input(): # defines the asking for input function, with no argument
    while True: # used to make a continuous loop
        guess = input("Enter a single letter") # asks for user input
        if len(guess) == 1 and guess.isalpha(): # checks input is 1 character and from the alphabet
            break #ends while loop
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") # outputs error message if guess is invalid
    check_guess(guess) # calls the guess checking function, passing guess as the argument
    
# %%
ask_for_input() # calls the asking for input function

# %%
