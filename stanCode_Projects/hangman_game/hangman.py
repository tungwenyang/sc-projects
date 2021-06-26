"""
File: hangman.py
Name: Claire Yang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is to play hangman game
    """
    play_hangman()


def play_hangman():
    """This function is to play hangman game"""
    question = random_word()
    word_to_guess = word_look_like(question)
    # to reflect as '-' in the console at the beginning of the game
    guesses_left = N_TURNS
    # the number of guess left
    while guesses_left > 0:
        # while loop starts at guesses_left = N_TURNS
        while word_to_guess.find('-') != -1:
            # while still has words not guessed
            word_to_guess = word_to_guess
            guesses_left = guesses_left
            if guesses_left > 0:
                # still has words not guessed, and still has guesses left
                print('The word looks like: ' + str(word_to_guess))
                print('You have ' + str(guesses_left) + ' guesses left.')
                input_ch = get_input()
                if question.find(input_ch) != -1:
                    # guess right
                    ans = ''
                    previous_word_to_guess = word_to_guess
                    for i in range(len(question)):
                        ch = question[i]
                        ch_previous = previous_word_to_guess[i]
                        if ch != input_ch:
                            # keep
                            ans += ch_previous
                        else:
                            # guess right, change
                            ans += input_ch
                    word_to_guess = ans
                    guesses_left = guesses_left
                    print('You are correct!')
                else:
                    # guess wrong
                    guesses_left -= 1
                    print('There is no ' + str(input_ch) + '\'s in the word.')
            else:
                # still has words not guessed, but no left guess
                print('You are completely hung : (')
                print('The world was: ' + str(question))
                word_to_guess = question
                # game is over, to leave the "while word_to_guess.find('-') != -1" loop
        # the words are all guessed
        if guesses_left > 0:
            print('You win!!')
            print('The world was: ' + str(question))
            guesses_left = 0
            # game is over, to leave the "while guesses_left > 0" loop


def word_look_like(question):
    """This function is to convert each character of the question to '-' in the console"""
    ans = ''
    for i in range(len(question)):
        ans += '-'
    return ans


def get_input():
    """
    This function is to get user input until the input is in correct format,
    then convert and return the input in uppercase string
    """
    input_ch = input('Your guess: ')
    if input_ch.isalpha():
        if len(input_ch) == 1:
            input_ch = input_ch.upper()
            return input_ch
        else:
            print('Illegal format.')
            while True:
                input_ch = input('Your guess: ')
                if input_ch.isalpha():
                    if len(input_ch) == 1:
                        input_ch = input_ch.upper()
                        return input_ch
                if not input_ch.isalpha():
                    print('Illegal format.')
                if len(input_ch) != 1:
                    print('Illegal format.')
    else:
        print('Illegal format.')
        while True:
            input_ch = input('Your guess: ')
            if input_ch.isalpha():
                if len(input_ch) == 1:
                    input_ch = input_ch.upper()
                    return input_ch
            if not input_ch.isalpha():
                print('Illegal format.')
            if len(input_ch) != 1:
                print('Illegal format.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
