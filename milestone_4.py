import random

class Game: 
    '''
    A Hangman game that asks the user for a guess (letter) and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list. 

    Attributes:
    ---------
    word_list: list
        A list of words to be used in the game.
    num_lives: int
        Number of lives the player has.
    word: str
        The word to be guessed picked randomly from the word_list.
    word_guessed: list
        A list of letters guessed.
    num_letters: int
        The number of unique letters in the word that have not been guessed yet.
    list_of_guesses: list
        A list of the letters that have already been tried.

    Methods:
    -------
    check_guess 
        Checks if the guess is in the word. 
    ask_for_input 
        Asks the user for a letter and calls the check_guess method.
    '''

    def __init__(self, word_list, num_lives): 
        '''
        Constructs all the neccessary attributes for the game object.

        Parameters:
        ----------
        word_list: list
        A list of words to be used in the game.
        num_lives: int
            Number of lives the player has.
        '''

        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.word_guessed = list(len(self.word)*"_") 
        self.num_letters = len(set(self.word) - set(self.word_guessed)) 
        self.list_of_guesses = [] 

    def check_guess(self, guess): 
        '''
        Checks if the guess is in the word.
        If it is, the "_" in the word_guessed list is replaced with the guess and
        the number of unique letters left (num_letters) is reduced by 1.
        If it is not, the number of lives (num_lives) is reduced by 1.

        Parameters:
        ----------
        guess: str
            The letter guessed by the user
        '''

        guess = guess.lower()
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.") 

            for i, letter in enumerate(self.word): 
                if letter == guess: 
                    self.word_guessed[i] = guess 

            self.num_letters -= 1 

        else:
            self.num_lives -= 1 
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        
        self.list_of_guesses.extend(guess) # adds latest guess to the list of guesses

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks for 2 things:
        1. If the letter is a single character from the alphabet
        2. If the letter has already been guessed
        The check_guess method is called if both checks are passed.
        '''

        while True: 
            guess = input("Enter a single letter ") 
            if not len(guess) == 1 or not guess.isalpha(): 
                print("Invalid letter. Please, enter a single alphabetical character.") 
            elif guess in self.list_of_guesses: 
                print("You already tried that letter.")
            else:
                self.check_guess(guess)
                break

def play_game():
    '''
    Plays the game and there are checks for 3 things:
    1. If the number of lives is 0 
    - this means the user has lost the game
    2. If the number of lives is not 0 and the unique number of letters left are more than 0
    - this means the user has won the game
    3. If the number of lives is more than 0
    - this means the game is still going and so calls the ask_for_input method
    '''
    
    word_list = ["apple", "banana", "pear", "orange", "grape"]
    game = Game(word_list, 7) 

    while True:
        print(" ".join([str(a) for a in game.word_guessed])) 
        if game.num_lives == 0: 
            print(f"You lost! The correct word was {game.word}.")
            break
        elif game.num_lives != 0 and game.num_letters <= 0: 
            print(f"Well done! The correct word was {game.word}. You have won the game!")
            break
        elif game.num_lives > 0: 
            game.ask_for_input()   

play_game() 


