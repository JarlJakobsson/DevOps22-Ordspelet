    while not winning:
        guess = input("Enter your guess: ").lower()
        guess_counter += 1
        print(f"You have made {guess_counter} guesses.")
        if len(guess) != 5:
            pass

        elif guess == secret_word:
            print("You won")
            break

        else:
            for letter in guess:
                if letter in secret_word:
                    if secret_word.index(letter) is guess.index(letter):
                        if (letter, guess.index(letter)) in correct_pos_list:
                            pass

                        else:
                            correct_pos_list.append((letter, guess.index(letter)))
                            correct_print[guess.index(letter)] = letter
                    elif letter in correct_letter_list:
                        pass
                    else:
                        correct_letter_list.append(letter)

            try:
                correct_letter_list.remove[correct_letter_list.index[letter]]
            except:
                pass

            print(
                f"""
                Wrong position:     {" ".join(correct_letter_list)}

                                    {" ".join(correct_print)}

            """
            )