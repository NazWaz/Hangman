# %%
class Hangman:

    def __init__(self, word_list, num_lives):

        self.word_list = word_list
        self.num_lives = num_lives

        import random # imports random module
        word = random.choice(word_list) # chooses a word at random from the list
        word_guessed = [",", ",", ",", ",", ",", ","] # list of letters guessed
        num_letters = len(set(word) - set(word_guessed)) # unique number of characters not yet guessed
        num_lives = 5 # number of lives
        word_list = ["apple", "banana", "pear", "orange", "grape"] # creates the list of fruits
        list_of_guesses = ["a"] # list of guesses

    def check_guess(guess): # defines the guess checking function, passing guess as the argument
        guess = guess.lower() # turns guess into lowercase
        import random # imports random module
  
        if guess in word: # condition where guess is part of the random word
            print(f"Good guess! {guess} is in the word.") 
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(): # defines the asking for input function, with no argument
        while True: # used to make a continuous loop
            guess = input("Enter a single letter") # asks for user input
            if not len(guess) == 1 or not guess.isalpha(): # checks if input is not 1 character or not from the alphabet
                print("Invalid letter. Please, enter a single alphabetical character.") # outputs error message if guess is invalid
            elif guess in list_of_guesses: # checks if input is already in the list of guesses
                print("You already tried that letter.")
            else:
                check_guess(guess) # calls the guess checking function, passing guess as the argument

    ask_for_input() # calls the asking for input function

# %%
ask_for_input() # calls the asking for input function            
    
# %%
