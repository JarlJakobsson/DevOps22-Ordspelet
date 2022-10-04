from players import Player, Guess_man, Secret_man
from constants import rules_text

def player_guess_game():
    secret_man = Secret_man()
    secret_man.create_secret()
    running = True
    
    while running:
        clues = secret_man.give_clues(input("Enter your guess: ").lower())
        if clues == (0,5):
            running = False

def bot_guess_game():
    guess_man = Guess_man()
    player = Player()
    secret_word = input(rules_text).lower()
    if len(secret_word) != 5:
        input("Word not allowed. Press enter to continue...")
        bot_guess_game()
    else:
        running = True
        guess_counter = 0

        while running:
            guess = guess_man.make_guess()
            if guess == "":
                break
            guess_counter += 1
            print(f"*** the secret word is {secret_word} ***")
            clues = player.give_clues()
            guess_man.calculate(guess, clues[0], clues[1])

            if secret_word not in guess_man.word_list:
                print("*** secret word removed ***")

def bot_game():
    secret_man = Secret_man()
    guess_man = Guess_man()
    secret_man.create_secret()
    running = True

    while running:
        guess = guess_man.make_guess()
        if guess == "":
            running = False
        print(f"*** The secret word is {secret_man.secret_word}. ***")
        clues = secret_man.give_clues(guess)
        if clues == (0,5):
            break
        guess_man.calculate(guess, clues[0], clues[1])

if __name__ == "__main__":
    bot_game()
