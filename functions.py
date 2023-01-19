from os import system
from time import sleep
from words import hangman

# function for style printing
def print_words(word):
    for char in word:
        sleep(0.05)
        print(char, end = "", flush = True)

# function for creating a list of correct letters and hint letters
def create_word_hint(word):
    correct_set = set()
    hint_list = list()
    for char in word:
        # correct answers only accept letters while hints accepts symbols.
        if char.isalpha() == True:
            correct_set.add(char)
            hint_list.append("_")
        else:
            hint_list.append(char)
    
    return correct_set, hint_list


# function if the letter's already chosen by the user
def duplicate_letters(ans, set):
    isduplicate = False
    for check_duplicate in set:
        if ans == check_duplicate:
            isduplicate = True
            break

    return isduplicate

# function that updates the hint list if the answer is correct
def update_word_hint(ans, word, list):
    letter_count = 0
    hint_list = list
    for check_letter in range(0, len(word)):
            if ans == word[check_letter]:
                hint_list[check_letter] = ans
                letter_count += 1

    return letter_count, hint_list

# function that checks the validity and correctness of the answer
def check_answer(ans, hint_letter_list, wrong_letter_list, correct_answer_set):
    # check the answer if it's valid (1 letter)
    if ans.isalpha() == 1 and len(ans) == 1:
        # call the function to check if the letter's already chosen by the user
        if duplicate_letters(ans.upper(), hint_letter_list) == True\
        or duplicate_letters(ans.upper(), wrong_letter_list) == True:
            print(f"You already picked {ans.upper()}.")
        else:
            right_answer = False

            # check if the answer is correct by looking for the correct set
            for check_answer in correct_answer_set:
                if ans.upper() == check_answer:
                    right_answer = True
                    break

            return right_answer
            
    else:
        print("You should only choose a letter.")
        return 0

    sleep(3)

# function if the user still wishes to play another game
def continue_playing():
    cont_ans = input("Would you like to play again? (Y/N): ").upper()

    if cont_ans == "N":
        play = False
        print_words("Thank you for playing. Till next time....")
    elif cont_ans == "Y":
        print_words("You sick bastard. You'd rather play a game and risk your friend's life once again.. Fascinating.")
        sleep(3)
        play = True
    else:
        continue_playing()

    system("CLS")
    
    return play

# function that determines the category
def show_category(word, categories):
    for category in range(0, len(categories)):
        if categories[category] == word:
            chosen_category = category
    
    if chosen_category == 0:
        return "PHRASES"
    elif chosen_category == 1:
        return "PLACES"
    else:
        return "MOVIES"


# function if the user's time runs out
def timer_up():
    print("Time's up. Press Enter to continue")

def check_state(word, wrong_count):
    system("CLS")
    if wrong_count == 5:
        print(hangman[5])
        print(f"You lost. You're too dumb to save your friend from being hanged.\nThe word is {word}. I guess HANGING OUT with your friend isn't an option anymore.")
    else:
        print(f"Congratulations! The word is {word}.\nYou managed to save a man from getting hanged.")