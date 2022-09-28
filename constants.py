rules ="""
            RULES:
            1. The word has to be a swedish word
            2. The word has to be 5 letters
            3. The word can only use a letter once
            4. The word CAN'T be a name
            5. The word CAN'T be a tense or plural of another word

            Enter your secret word
"""

# with open("guesses.txt", "r+") as g:
#     total_guesses = g.read()
#     print(total_guesses)
#     g.write(str(guess_counter))

# print(total_guesses)

def bot_game(world_list):

    winner = True
    potential_words_list = []
    secret_word = player_secret
    print(secret_word)

    while winner:
        
        guess = word_list[randint(0, len(word_list))]
        print(guess)
        print()

        if len(secret_word) != 5:
            pass
        
        elif guess == secret_word:
            winner = False
            print("You lost")
            print()
        
        else:
            for letter in guess:
                if letter in secret_word:
                    if guess.index(letter) == secret_word.index(letter):
                        for word in world_list:
                            if word in potential_words_list:
                                pass

                            elif word.index(letter) == secret_word.index(letter):
                                potential_words_list.append