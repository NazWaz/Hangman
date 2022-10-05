class Hangman:

    def __init__(self, word_list, num_lives):

        self.word_list = word_list
        self.num_lives = num_lives

        import random # imports random module
        word = random.choice(word_list) # chooses a word at random from the list
        word_guessed = [",", ",", ",", ",", ",", ","]
        num_letters = len(set(word) - set(word_guessed)) # unique number of characters not yet guessed
        num_lives = 5 # number of lives
        word_list = ["apple", "banana", "pear", "orange", "grape"] # creates the list of fruits
        list_of_guesses = [] # list of guesses

    