import random

# Create a list of my 5 favorite fruits.
word_list = ['Apple', 'Watermelon', 'Banana', 'Grape', 'Peach'] 

# Created the 'random.choice' method while using 'word_list' as a variable in the parentheses.
# This would randomly generate the fruits in the list.
word = random.choice(word_list)

# To print out the random fruit from the list.
print(word)

# The input function is used to print a single letter and assign it to a variable named 'guess'.
guess = input("Please enter a letter!: ")

# This if statement is created to check if the user enters an input that is alphabetical
# and is equal to 1.
if len(guess) == 1 and guess.isalpha():
    # If the criteria is met.
    print("Good guess!")
else:
    # If it does not meet the criteria.
    print("Oops! That is not a valid input.")