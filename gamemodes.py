from players import Player, Guess_man, Secret_man, highscore
from constants import rules_text


def player_guess_game():
    secret_man = Secret_man()
    secret_man.create_secret()
    running = True
    
    while running:
        print("\nType help to see commands: ")
        clues = secret_man.give_clues(input("\nEnter your guess: ").lower()) # Calls give_clues() from secret_man and takes input as arg, saves the returned value as clues
        if clues == False:
            highscore.total_guesses += secret_man.guess_counter
            break
        if clues == (0,5): # If clues are (0,5) it means 5 letters are on the correct positon and the game is over
            highscore.update_highscore(secret_man.guess_counter)
            break

def bot_guess_game():
    guess_man = Guess_man()
    guess_man.clear_guess_list() # Clears the guess_list to have a fresh list for each game.
    player = Player()
    secret_word = input(rules_text).lower()
    if len(secret_word) != 5: # Game checks if secret_word is allowed.
        input("Word not allowed. Press enter to continue...")
        bot_guess_game()
    else:
        running = True
        while running:
            guess = guess_man.make_guess() # Calls make_guess() from guess_man and saves it as guess.
            if guess == "": # If Guess man doesn't have any words left in word_list it will return ""
                highscore.total_guesses += player.guess_counter
                break
            print(f"*** the secret word is {secret_word} ***") # Game tells the user the secret word so it's easier to give clues.
            clues = player.give_clues()
            if clues == (0,5):
                highscore.update_highscore(player.guess_counter)
                break
            guess_man.calculate(guess, clues[0], clues[1]) # Calls calculate from guess_man and takes guess, clues element 0 and clues element 1 as args.

            if secret_word not in guess_man.word_list: # Userfriendly hint if typed in incorrect clues or a word that doesn't exist in word_list.
                print("*** secret word removed or not in word list ***")

def bot_game():
    secret_man = Secret_man()
    guess_man = Guess_man()
    secret_man.create_secret() # Calls create_secret() from secret_man to make him create secret_word
    running = True

    while running:
        guess = guess_man.make_guess() # Calls make_guess() from guess_man and saves it as guess.
        print(f"*** The secret word is {secret_man.secret_word}. ***") # Game tells user the secret word to help following the game.
        clues = secret_man.give_clues(guess)
        if clues == (0,5): # If clues are 0,5 it means 5 letters are on the correct position.
            highscore.update_highscore(secret_man.guess_counter)
            guess_man.win_msg()
            break
        guess_man.calculate(guess, clues[0], clues[1])

def load_game():
    secret_man = Secret_man()
    running = secret_man.load_secret(input("\nEnter the filename you want to load: "))
    
    while running:
        print('Type "help" to see commands.')
        clues = secret_man.give_clues(input("\nEnter your guess: ").lower()) # Calls give_clues() from secret_man and takes input as arg, saves the returned value as clues
        if clues == False:
            highscore.total_guesses += secret_man.guess_counter
            break
        if clues == (0,5): # If clues are (0,5) it means 5 letters are on the correct positon and the game is over
            highscore.correct_guesses += 1
            highscore.total_guesses += secret_man.guess_counter
            break
