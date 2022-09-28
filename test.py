# check if word is correct
# else
# loop through evry letter
# if exists
# check if letter correct position
# correct_pos_list.append l
# else
# correct_letter_list.append l

from os import remove
from random import randint
from weakref import WeakValueDictionary
import constants

raw_list = []


total_guesses = 0


with open("words.txt", encoding="utf8") as f:
    for line in f.readlines():
        raw_list.append(line.replace("\n", ""))  ## slice away \n


# def player_guess():

#     secret_word = "qwert"  # word_list[randint(0, len(word_list))]
#     guess_counter = 0
#     winner = False
#     correct_letter_list = []
#     correct_pos_list = []
#     correct_print = ["_", "_", "_", "_", "_"]

#     while not winner:
#         guess = input("Enter your guess: ").lower()
#         guess_counter += 1
#         print(f"You have made {guess_counter} guesses.")
#         if len(guess) != 5:
#             pass

#         elif guess == secret_word:
#             winner = True
#             print("You won")

#         else:
#             for letter in guess:
#                 if letter in secret_word:
#                     if secret_word.index(letter) is guess.index(letter):
#                         if (letter, guess.index(letter)) in correct_pos_list:
#                             pass

#                         else:
#                             correct_pos_list.append((letter, guess.index(letter)))
#                             correct_print[guess.index(letter)] = letter
#                     elif letter in correct_letter_list:
#                         pass
#                     else:
#                         correct_letter_list.append(letter)

#             try:
#                 correct_letter_list.remove[correct_letter_list.index[letter]]
#             except:
#                 pass

#             print(
#                 f"""
#                 Wrong position:     {" ".join(correct_letter_list)}

#                                     {" ".join(correct_print)}

#             """
#             )


def bot_guess(word_list):
    # try:
    my_secret = input(constants.rules)
    if len(my_secret) != 5:
        input("word not allowed. Press enter to continue...")
        bot_guess()

    guess = word_list[randint(0, len(word_list) - 1)]

    if guess == my_secret:
        print("\nYou lost in 1 guess, pick a better secret word next time.")

    else:
        potential_words_list = []

        winning = True
        while winning:
            guess = word_list[randint(0, len(word_list) - 1)]
            print(my_secret)
            correct_but_wrong = int(
                input(
                    f"Bot: Is the word '{guess}'?\n\n How many letters are correct but on the wrong position?: "
                )
            )
            correct_and_right = int(
                input("\n How many letters are correct and on the correct position?: ")
            )

            if correct_but_wrong == 0:
                for word in word_list:
                    for letter in guess:
                        if correct_and_right > 0:
                            if guess.index(letter) is word.index(letter):
                                if word not in potential_words_list:
                                    print(f"*** 1 * ADDING WORD {word} ***")
                                    potential_words_list.append(word)
                            elif letter not in word:
                                if word not in potential_words_list:
                                    print(f"*** 2 * ADDING WORD {word} ***")
                                    potential_words_list.append(word)

            elif correct_but_wrong > 0:
                for word in word_list:
                    num_matches = 0
                    for letter in guess:
                        if letter in word:
                            num_matches += 1
                            if (
                                word not in potential_words_list
                                and num_matches >= correct_but_wrong
                            ):
                                if correct_and_right == 0:
                                    if guess.index(letter) != word.index(letter):
                                        print(
                                            f"*** 3 * ADDING WORD {word} matches = {num_matches} ***"
                                        )
                                        potential_words_list.append(word)
                                else:
                                    print(
                                        f"*** 4 * ADDING WORD {word} matches = {num_matches} ***"
                                    )
                                    potential_words_list.append(word)

            print(len(potential_words_list))
            word_list = potential_words_list
            if guess in word_list:
                word_list.remove(guess)

            potential_words_list = []


bot_guess(raw_list)


# for word in word_list:
#     for letter in guess:
#         if letter in word:
#             if word in potential_words_list:
#                 pass
#             else:
#                 potential_words_list.append(word)
