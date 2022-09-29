
from random import randint
import constants

class Guess_man():
    pass
class Secret_man():
    pass

Player_A = Guess_man()
Player_B = Secret_man()


raw_list = []

total_guesses = 0

def win_func(secret_word):
    print("Bot: You have bested me.")
    teach_bot = input("Bot: Please teach me the word:\n Do you want to teach the bot? Y/N: ")
    if teach_bot == "y" or "Y":
        add_word(secret_word)

with open("words.txt", encoding="utf8") as f:
    for line in f.readlines():
        raw_list.append(line.replace("\n", ""))  ## slice away \n

def add_word(new_word):
    with open("words.txt", "a", encoding="utf8") as f:
        f.writelines(new_word)

def player_guess():

    secret_word = "qwert"  # word_list[randint(0, len(word_list))]
    guess_counter = 0
    winning = False
    wrong_pos_list = []
    correct_pos_list = []

    while not winning:
        guess = input("Enter your guess: ").lower()
        guess_counter += 1
        if len(guess) != 5:
            print(f"Your guess doesn't even have 5 letters.")
            print(f"You have made {guess_counter} guesses.\n")
            pass

        elif guess == secret_word:
            print("You won")
            break

        else:
            for letter in guess:
                if letter in secret_word:
                    if secret_word.find(letter) is guess.find(letter):
                        if (letter, guess.index(letter)) in correct_pos_list:
                            pass
                        else:
                            correct_pos_list.append((letter, guess.find(letter)))
                    elif letter in wrong_pos_list:
                        pass
                    else:
                        wrong_pos_list.append(letter)

            try:
                wrong_pos_list.remove[wrong_pos_list.index(letter)]
            except:
                pass
            print(f"You have made {guess_counter} guesses.\n")
            print(f"{len(wrong_pos_list)} letters are correct but on the wrong poition")
            print(f"{len(correct_pos_list)} letters are on the correct position")

def bot_guess(word_list):
    secret_word = input(constants.rules)
    if len(secret_word) != 5:
        input("word not allowed. Press enter to continue...")
        bot_guess(word_list)
    else:
        potential_words_list = []
        winning = True
        guess_counter = 0
        while winning:
            try:
                guess = word_list[randint(0, len(word_list) - 1)]
                guess_counter += 1
            except:
                win_func(secret_word)
                break

            print(secret_word)
            wrong_pos = int(input(f"Bot: Is the word '{guess}'?\n\n How many letters are correct but on the wrong position?: "))
            correct_pos = int(input("\n How many letters are correct and on the correct position?: "))   

            if correct_pos == 5:
                print("Bot: EZ\n --- You lost ---")
                break

            for word in word_list:
                num_matches = 0
                pos_match = 0
                for letter in guess:
                    if guess.find(letter) == word.find(letter):
                        pos_match += 1
                    elif letter in word:
                        num_matches += 1
                    if num_matches == wrong_pos and pos_match == correct_pos and word not in potential_words_list:
                                print(f"*** ADDING {word} ***")
                                potential_words_list.append(word)
                    if not num_matches == wrong_pos and not pos_match == correct_pos:
                        try:
                            potential_words_list.remove(word)
                        except:
                            pass
            
            print(len(potential_words_list))
            print(f"Bot have made {guess_counter} guesses.")
            word_list = potential_words_list
            if guess in word_list:
                word_list.remove(guess)

            potential_words_list = []


# bot_guess(raw_list)



# for word in word_list:
#     for letter in guess:
#         if letter in word:
#             if word in potential_words_list:
#                 pass
#             else:
#                 potential_words_list.append(word)
bot_guess(raw_list)