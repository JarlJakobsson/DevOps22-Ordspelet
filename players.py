from random import randint
import os

class Mans():
    # Initiates itself with self.word_list from words.txt
    def __init__(self):
        self.word_list = []
        with open("words.txt", "r", encoding="utf8") as f:
            for line in f.readlines():
                self.word_list.append(line.replace("\n", ""))  ## removes \n

class Guess_man(Mans):
  
    guess_list = []

    def win_msg(self):
        print("Guess man: EZ, I win :)")

    def clear_guess_list(self):
        self.guess_list = []

    def control_word(self, new_word):
        # Checks if any letter is used more than once
        letter_count = 0
        for letter in new_word:
            if new_word.count(letter) > 1:
                letter_count =+ 1
        if letter_count > 1:
            print("\nGuess man: The word uses some letters more than once.")
            return

        # Self.guess_list have guesses and clues in a tuple. Loops through every guess and compares its result with the clues given.
        for t in self.guess_list:
            num_matches = 0
            pos_match = 0
            for letter in t[0]:
                if t[0].find(letter) == new_word.find(letter):
                    pos_match += 1
                elif letter in new_word:
                    num_matches += 1

            # If atleast one clues doesn't match the control check, Guess_man sais the player cheated.
            if num_matches != t[1] or pos_match != t[2]:
                print(f"\n\nGuess man: '{t[0]}' doesn't have {t[1]} correct letters on wrong position and {t[2]} letters on correct position! Cheater!")
                return

        self.add_word(new_word)
        print("*** Adding word ***")

    def lose_func(self): # Function for when bot loeses
        print("Guess man: You have bested me.")
        teach_bot = input("Guess man: Please teach me the word.\n\nDo you want to teach the bot? Y/N: ")
        if teach_bot == "y" or teach_bot == "Y":
            new_word = input("\nGuess man: Tell me the word again: ").lower()
            self.control_word(new_word)        

    def add_word(self, new_word): # Function to append new word to words.txt
       with open("words.txt", "a", encoding="utf8") as f:
           f.writelines(f"{new_word}\n")

    def make_guess(self):
        if len(self.word_list) > 0: # Checks if Guess_man still have words in its word_list
            input(f"Guess man: Thinking... I'm choosing between {self.word_list}.\n I have {len(self.word_list)} Potential words.\n\nPress Enter key to continue\n")
            guess = self.word_list[randint(0, len(self.word_list))-1]
            print(f"Guess man: Is the word '{guess}'?")
            return guess
        else: # If no words in word_list calls the lose_func
            self.lose_func()
            return ""

    def calculate(self, guess, wrong_pos, correct_pos):
        potential_word_list = [] # Makes sure potential_word_list is empty
        self.guess_list.append((guess, wrong_pos, correct_pos))

        if correct_pos == 5: # Checks win
                print("\nGuess man: EZ, I win :)")
        
        if guess in potential_word_list: # Removes the guess from the word_list
            self.word_list.remove(guess)

# Loops through every word in the word list and every letter in the guess, if letter is in word and on same position as guess, ads a pos_match counter, else ads a num_matches counter
# Checks if the counters match the clues given and if the word is not already in the potential_word_list. If passes it appends the word to potential_word_list
        for word in self.word_list: 
                    num_matches = 0
                    pos_match = 0
                    for letter in guess:
                        if guess.find(letter) == word.find(letter):
                            pos_match += 1
                        elif letter in word:
                            num_matches += 1
                    if num_matches == wrong_pos and pos_match == correct_pos and word not in potential_word_list:
                        potential_word_list.append(word)
                        
        self.word_list = potential_word_list # Replaces word_list with potential_word_list

class Secret_man(Mans):

    guess_counter = 0
    secret_word = ""

    def tell_guesses(self):
        print(f"Secret man: You have made {self.guess_counter} guesses.\n")  

    def create_secret(self):
        self.secret_word = self.word_list[randint(0, len(self.word_list)-1)]
        print("Secret man: Okay, I'm thinking of a word.")
        return self.secret_word

    def give_clues(self, guess):
        self.guess = guess

        if self.guess == "help": # Incase you need help
            print(f"\n*** The secret word is {self.secret_word} ***")

        elif self.guess == "quit": # Option to give up
            print("*** Returning to Main menu *** ")
            return False

        elif len(self.guess) != 5: # Controls the guess have 5 letters
            self.guess_counter += 1
            print("Secret man: Your guess needs to be 5 letters. Try again.")
            self.tell_guesses()
        else:
            wrong_pos_list = []
            correct_pos_list = []
            self.guess_counter += 1

            for letter in guess: # Loops through every letter in the guess
                if letter in self.secret_word: # Checks if the letter exists in secret_word
                    if (self.secret_word.find(letter) == guess.find(letter) and letter not in correct_pos_list): # Checks if any letter is on the same position and not already in correct_pos_list
                        correct_pos_list.append(letter)
                        if letter in wrong_pos_list: # Checks if the letter is in wrong pos list
                            wrong_pos_list.remove(letter)
                    elif letter not in wrong_pos_list: # Checks if the letter is not already in wrong_pos_list
                        wrong_pos_list.append(letter)

            if (len(wrong_pos_list), len(correct_pos_list)) == (0,5): # 0,5 means 0 wrong pos and 5 correct pos = guesser won
                print(f"\n****** Secret man: You won! ******\nThe correct word was {self.secret_word} and you got it in {self.guess_counter} guesses.\n")
                return (len(wrong_pos_list), len(correct_pos_list))

            else:    
                print(f"\nSecret man: {len(wrong_pos_list)} letters are correct but on the wrong poistion, and {len(correct_pos_list)} letters are on the correct position.")
                self.tell_guesses()               
                return (len(wrong_pos_list),len(correct_pos_list)) # Returns lenght of wrong_wrong post list and correct_pos_list as a tuple

class Player(Secret_man): # Player gets the guess_counter and secret_word holder from Secret_man

    def give_clues(self):
        try:
            wrong_pos = int(input("\nHow many letters are correct, but on wrong position?: "))
            correct_pos = int(input("\nHow many letters are on the correct position?: "))
            self.guess_counter += 1
            print(f"Guess man have made {self.guess_counter} guesses.")
            print(f"Guess man made a new record with only {self.guess_counter} guesses!")
            return (wrong_pos, correct_pos) # Returns a tuple with clues
        except:
            print("You have to enter a number.")
            return self.give_clues() # If invalid input it will re-run give_clues() 

class Highscore():
    # Initiates itself with temp_list from highscore.txt
    def __init__(self):
        temp_list = []
        try:
            with open("highscore.txt", "x") as f: # Tries to create highscore.txt
                pass
        except:
            pass

        empty_check = os.path.getsize("highscore.txt") ## Googled "how to check if a file is empty python" and found https://www.adamsmith.haus/python/answers/how-to-check-if-a-file-is-empty-in-python
        if empty_check != 0:
            with open("highscore.txt", "r") as f:
                for line in f.readlines():
                    temp_list.append(line.replace("\n", ""))

            self.total_guesses = int(temp_list[0])
            self.fastest_win = int(temp_list[1])
            self.correct_guesses = int(temp_list[2])

        else: # Incase highscore.txt is empty
            self.total_guesses = 0
            self.fastest_win = 9999
            self.correct_guesses = 0


    def send_score(self):
        with open("highscore.txt", "w") as f: # Writes over highscore.txt to update new highscore
            f.write(f"{self.total_guesses}\n{self.fastest_win}\n{self.correct_guesses}\n")

    def print_record(self):
        if self.correct_guesses == 0:
            print("\nThere are no correct guesses yet.")
        else:
            print(f"The fastest win is in {self.fastest_win} guesses.")
            print(f"The avrage guesses needed for a win is {self.total_guesses/self.correct_guesses} guesses.")

highscore = Highscore() # Instantiates a Highscore
