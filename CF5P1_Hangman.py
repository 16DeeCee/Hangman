from threading import Timer
from time import sleep
from random import choice
from os import system
import words, functions as f

categories = [words.phrases, words.places, words.movies]

play_again = True

# loop if the user still wishes to play another game
while play_again == True:
    print(words.title)
    f.print_words(words.intro)
    sleep(3)

    random_category = choice(categories)
    chosen_word = choice(random_category)

    correct_answer_set, hint_letter_list = f.create_word_hint(chosen_word)
    wrong_letter_list = list()

    # loop breaks if the user has already 3 mistakes or if he got all the correct letters
    while len(wrong_letter_list) < 5 and len(correct_answer_set) != 0:
        system("CLS")
        print(words.hangman[len(wrong_letter_list)])
        print(f"Category: {f.show_category(random_category, categories)}        Wrong Answers: {wrong_letter_list}")
        f.print_words(hint_letter_list)

        #starts the timer and waits for the user to give an answer
        countdown = Timer(10, f.timer_up)
        countdown.start()
        answer = input("\nYou have 10 seconds to answer\nWhich letter would you choose?: ")

        if answer:
            check_right = f.check_answer(answer, hint_letter_list, wrong_letter_list, correct_answer_set)

            # updates the correct or wrong letter list depending on the user's answer
            if check_right == True:
                letter_count, hint_letter_list = f.update_word_hint(answer.upper(), chosen_word, hint_letter_list)
                correct_answer_set.remove(answer.upper())
                print(f"Yooooo! You got {letter_count} {answer.upper()}!")

            elif check_right == False:
                wrong_letter_list.append(answer.upper())
                print(f"*Sigh* You got it wrong! You only have {5 - len(wrong_letter_list)} lives remaining.")
                
            countdown.cancel()
            sleep(3)

        else:
            wrong_letter_list.append("Time's Up")

    # checks if the user is a winner or a loser
    f.check_state(chosen_word, len(wrong_letter_list))

    play_again = f.continue_playing()