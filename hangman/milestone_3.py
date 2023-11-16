import random

word_list = ['Apple', 'Watermelon', 'Banana', 'Grape', 'Peach']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word.lower():
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a letter!: ")
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            check_guess(guess) 
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")       

ask_for_input()