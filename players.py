from random import randint

raw_list = []

with open("words.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        raw_list.append(line.replace("\n", ""))  ## slice away \n

class Mans():
    def __init__(self):
        self.word_list = raw_list

class Guess_man(Mans):

    def make_guess(self):
        if len(self.word_list) > 0:
            guess = self.word_list[randint(0, len(self.word_list))-1]
            print(f"Guess man: Is the word '{guess}'?")
            return guess
        else:
            print("Guess man: You have bested me.")#win_func()
            return ""

    def calculate(self, guess, wrong_pos, correct_pos):
        potential_word_list = [] # Creates a empty potential_word_ist
        input(f"Guess man: Thinking... I'm choosing between {self.word_list}.\n I have {len(self.word_list)} Potential words.\nPress any key to continue\n")

        if correct_pos == 5: # Checks win
                print("Bot: EZ, I win :)")
        
        if guess in potential_word_list: # Removes the guess from the word_list
            self.word_list.remove(guess)

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

    def create_secret(self):
        self.secret_word = self.word_list[randint(0, len(self.word_list)-1)]
        print("Okay, I'm thinking of a word.")
        return self.secret_word

    def give_clues(self, guess):
        self.guess = guess

        if self.guess == "help": # Incase you need help
            print(f"\n*** The secret word is {self.secret_word} ***")

        elif self.guess == "quit":
            return(0,5)

        elif len(self.guess) != 5: # Controls the guess have 5 letters
            print("Your guess needs 5 letters.")
            self.guess_counter += 1
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
                print(f"{len(wrong_pos_list)} letters are correct but on the wrong poistion, and {len(correct_pos_list)} letters are on the correct position.")
                print(f"You have made {self.guess_counter} guesses.\n")                  
                return (len(wrong_pos_list),len(correct_pos_list)) # Returns lenght of wrong_wrong post list and correct_pos_list as a tuple

class Player(Secret_man): # Player gets the guess_counter and secret_word holder from Secret_man

    def give_clues(self):
        try:
            wrong_pos = int(input("\nHow many letters are correct, but on wrong position?: "))
            correct_pos = int(input("\nHow many letters are on the correct position?: "))
            self.guess_counter += 1
            print(f"Bot have made {self.guess_counter} guesses.")
            return (wrong_pos, correct_pos) # Returns a tuple with clues
        except:
            print("You have to enter a number.")
            return self.give_clues() # If invalid input it will re-run give_clues() 
        

    # def win_func(secret_word):
    #     print("Bot: You have bested me.")
    #     teach_bot = input("Bot: Please teach me the word.\nDo you want to teach the bot? Y/N: ")
    #     if teach_bot == "y" or "Y":
    #         add_word(secret_word)
    #     else:
    #         return

    # def add_word(new_word):
    #    with open("words.txt", "a", encoding="utf8") as f:
    #        f.writelines(new_word)