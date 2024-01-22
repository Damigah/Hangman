# Project Title: Hangman

# Table of Contents

1. Description
   - 1.1 About This Project
   - 1.2 The Aim of The Project
   - 1.3 What I have learnt
2. Installation Instructions
3. Usage Instructions
4. File Structure of The Project
5. My Progression Through Each Milestone

## 1. Description
### 1.1 About This Project
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### 1.2 The Aim of The Project
The aim of this project is to showcase my programming skills by using the Hangman game as an example. 

### 1.3 What I have learnt
- Programming Class and Methods in Python
- Executing control flow statements
- Git command line
 
## 2. Installation Instructions
1. I clone the GitHub repository: `git clone https://github.com/Damigah/Hangman.git` in the destination of my machine using Visual Studio Code.
2. I connect to the remote repository on GitHub: `git remote add origin https://github.com/Damigah/Hangman.git`
3. I move the Python files into the same destination the git repository is in the file explorer.
4. I check the if the files are there by using the `ls` commmand in the terminal on Visual Studio Code.
6. I will add the files by using `git add Python_file.py` to be staged.
7. I will check if the files I want are staged by typing `git status` to see the files that I had added are there.
8. If the files that I wanted are staged, I will commit the files using `git commit -m "The message"` with the message stating what I changed.
9. When everything is ready, I will use the command `git push` to move my files from my local repository to my remote repository.
10. I go on my GitHub repository to see that the files that I pushed are in the location I want it to be. 

## 3. Usage Instructions
When the script is running, the user is asked to guess the letter of the randomised word. The user have 5 tries to guess correctly. 

## 4. File Structure of The Project
- README.md
- hangman
   - Milestone_2.py
   - Milestone_3.py
   - Milestone_4.py
   - Milestone_5.py

## 5. My Progression Through Each Milestone
### Milestone_2.py
   - This is where I build my **foundation** on creating the hangman project by creating a list of fruits and ramdomising the words while telling the user to enter a letter to see if it will ramdomise the fruit in the word list.
### Milestone_3.py
   - I check to see if the guess is in the word using a **while loop** and to create it all in a function to run the checks.
### Milestone_4.py
   - I added **2 functions** named **check_guess** and **ask_for_input**. I define what happens if the letter is in the word then define what happens if the letter is not in the word.
### Milestone_5.py
   - Finally, I add a **play_game** function to **break** the game whenever the user wins or loses the game based on how many letters guessed in the word or if the user lives runs out.
