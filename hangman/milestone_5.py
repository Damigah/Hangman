import random

class Hangman:
    '''
    A class for Hangman

    Attributes:
        word (str): The word to be guessed that would be randomised.
        word_guessed (list): A list for the word to be guessed, also showcasing missing letters as underscores.
        num_letters (int): The number of unique letters in word.
        num_lives (int): The number of lives the player has.
        word_list (list): A list of words to be ramdomised.
        list_of_guesses (list): A list of letters that are already guessed.
    '''
    def __init__(self, word_list, num_lives = 5):
        '''
        A magic method for the Hangman class.
        
        Parameters:
            word_list (list): The list of words to choose from.
            num_lives (int): The number of lives the player starts with.
        '''
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        It will check if the letter is in the ramdomised word which it updates the game.
        
        Parameters:
            guess (str): The letter guessed by the user.
        '''
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if self.word.lower()[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            if guess not in self.list_of_guesses:
                self.list_of_guesses.append(guess)
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word. Try again.")
                if self.num_lives >= 1:
                    print(f"You have {self.num_lives} lives left.")
                    print(self.list_of_guesses)
            else:
                print("You already tried that letter!")
                print(self.list_of_guesses)

    def ask_for_input(self):
        """
        It will asks the user to enter a letter until the random word is guessed.
        """
        while True:
            guess = input("Please enter a letter!: ")
            if len(guess) == 1 and guess.isalpha():
                self.word_guessed
                self.check_guess(guess)
                break 
            else:
                print("Invalid letter. Please enter a single alphabetical character.")

def play_game(word_list):
    """
    This function is used to start the Hangman game.
    
    Parameters:
        word_list (list): A list of words to be ramdomised.
        num_lives (int): The number of lives the player has.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You have {game.num_lives} lives, Game Over!")
            break
        elif game.num_letters > 0:
            game.ask_for_input() 
        else:
            print('Congratulations. You won the game!')
            break

if __name__ == "__main__":
    word_list = ['Apple', 'Watermelon', 'Banana', 'Grape', 'Peach'] 
    play_game(word_list)