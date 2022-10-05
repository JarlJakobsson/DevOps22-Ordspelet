from players import Player, Guess_man, Secret_man
from constants import rules_text

def player_guess_game():
    secret_man = Secret_man()
    secret_man.create_secret()
    running = True
    
    while running:
        print('Type "help" to see the secret word\nType "quit" to give up.')
        clues = secret_man.give_clues(input("\nEnter your guess: ").lower())
        if clues == (0,5):
            break

def bot_guess_game():
    guess_man = Guess_man()
    guess_man.clear_guess_list()
    player = Player()
    secret_word = input(rules_text).lower()
    if len(secret_word) != 5: # Game checks if secret_word is allowed.
        input("Word not allowed. Press enter to continue...")
        bot_guess_game()
    else:
        running = True
        while running:
            guess = guess_man.make_guess()
            if guess == "": # If Guess man doesn't have any words left in word_list it will return ""
                break
            print(f"*** the secret word is {secret_word} ***") # Game tells the user the secret word so it's easier to give clues.
            clues = player.give_clues()
            if clues == (0,5):
                break
            guess_man.calculate(guess, clues[0], clues[1])

            if secret_word not in guess_man.word_list:
                print("*** secret word removed or not in word list ***")

def bot_game():
    secret_man = Secret_man()
    guess_man = Guess_man()
    secret_man.create_secret()
    running = True

    while running:
        guess = guess_man.make_guess()
        print(f"*** The secret word is {secret_man.secret_word}. ***") # Game tells user the secret word to help following the game.
        clues = secret_man.give_clues(guess)
        if clues == (0,5): # If clues are 0,5 it means 5 letters are on the correct position.
            guess_man.win_msg()
            break
        guess_man.calculate(guess, clues[0], clues[1])

