import sys
# from constants import menu_text
# from gamemodes import player_guess_game, bot_guess_game, bot_game
import gamemodes
import constants

class Menu:

    text = '''
        ####### Main Menu #######
        [1] Player guess game 
        [2] Bot guess game    
        [3] Bot game         
        [q] Exit              
        #########################
'''

    def wait_for_user(self):
        if self.keep_going:
            input("\nPress Enter to continue...")

    def user_choice(self):
        return input("Enter your choice: ")
    
    def menu_commands(self, choice):
        if choice ==  "1":
            gamemodes.player_guess_game()

        elif choice == "2":
            gamemodes.bot_guess_game()

        elif choice == "3":
            gamemodes.bot_game()

        elif choice == "q" or "Q":
            self.keep_going = False

    def start_menu(self):
        self.keep_going = True
        while self.keep_going:
            print(Menu.text)
            choice = self.user_choice()
            #choice = input("\nEnter your choice: ")
            self.menu_commands(choice)
            self.wait_for_user()
