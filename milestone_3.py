# %%
import random # imports random module

class Hangman: # sets up the Hangman class
    
    def __init__(self, word_list, num_lives): # initialises the parameters i.e. what will be selected for each instance of the game

        self.word_list = word_list # every attribute needs to start with self
        self.num_lives = num_lives

        self.word = random.choice(word_list) # chooses a word at random from the list
        self.word_guessed = [",", ",", ",", ",", ",", ","] # list of letters guessed
        self.num_letters = len(set(self.word) - set(self.word_guessed)) # unique number of characters not yet guessed
        self.list_of_guesses = [] # list of guesses

    def check_guess(self, guess): # defines the guess checking function, passing this instance (self) and guess as the arguments
        guess = guess.lower() # turns guess into lowercase
        if guess in self.word: # condition where guess is part of the random word
            print(f"Good guess! {guess} is in the word.") 

            for i, letter in enumerate(self.word): # for each index i, letter is assigned for each character in word
                if letter == guess: # condition where letter in the word is equal to guess character
                    self.word_guessed[i] = guess # splices guess character into word guessed list

            self.num_letters -= 1 # 1 less unique character left

        else:
            self.num_lives -= 1 # lose a life
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        
        self.list_of_guesses.extend(guess) # adds latest guess to the list of guesses

    def ask_for_input(self): # defines the asking for input function, with only self as the argument
        while True: # used to make a continuous loop
            guess = input("Enter a single letter") # asks for user input
            if not len(guess) == 1 or not guess.isalpha(): # checks if input is not 1 character or not from the alphabet
                print("Invalid letter. Please, enter a single alphabetical character.") # outputs error message if guess is invalid
            elif guess in self.list_of_guesses: # checks if input is already in the list of guesses
                print("You already tried that letter.")
            else:
                self.check_guess(guess) # calls the guess checking function, passing guess as the argument
                break

                
# %%    
hangman_game = Hangman(word_list = ["apple", "banana", "pear", "orange", "grape"], num_lives = 5) # creates the hangman_game instance using the Hangman class and the desired word list and number of lives
hangman_game.ask_for_input() # calls the asking for input function using the hangman_game instance
