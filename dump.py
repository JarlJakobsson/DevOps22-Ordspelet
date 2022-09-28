elif wrong_pos > 0:
                for word in word_list:
                    num_matches = 0
                    pos_match = 0
                    for letter in guess:
                        if letter in word and guess.index(letter) != word.index(letter):
                            num_matches += 1
                            if correct_pos > 0:
                                if guess.index(letter) == word.index(letter):
                                    pos_match += 1
                                    if num_matches == wrong_pos and pos_match == correct_pos:


                                            gissning: kamel   current: ksdaf     1 1


                            if (
                                word not in potential_words_list
                                and num_matches == wrong_pos
                            ):
                                if correct_pos == 0:
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
