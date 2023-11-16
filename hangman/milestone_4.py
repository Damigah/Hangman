import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range(len(self.word))]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
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
                self.list_of_guesses.append(guess) #appends to wrong letters into the list of guesses
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word. Try again.")
                if self.num_lives >= 1:
                    print(f"You have {self.num_lives} lives left.")
                else: 
                    self.num_lives == 0
                    print(f"you have {self.num_lives}, Game Over!")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter!: ")
            self.check_guess(guess)
            if len(guess) == 1 and guess.isalpha():
                self.word_guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                print(self.list_of_guesses)
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

word_list = ['Apple', 'Watermelon', 'Banana', 'Grape', 'Peach'] 
hangman = Hangman(word_list)
hangman.ask_for_input()
hangman.check_guess() 