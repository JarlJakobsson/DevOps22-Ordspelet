from constants import menu_text
from gamemodes import player_guess_game, bot_guess_game, bot_game, load_game
from players import highscore

class Menu:

    def wait_for_user(self):
        if self.keep_going:
            input("\nPress Enter to continue...")

    def user_choice(self):
        return input("Enter your choice: ")
    
    def menu_commands(self, choice):
        if choice ==  "1":
            player_guess_game()

        elif choice == "2":
            bot_guess_game()

        elif choice == "3":
            bot_game()

        elif choice == "4":
            load_game()

        elif choice == "5":
            highscore.print_record()

        elif choice == "q" or choice == "Q":
            highscore.send_score()
            self.keep_going = False

    def start_menu(self):
        self.keep_going = True
        while self.keep_going:
            print(menu_text)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()

