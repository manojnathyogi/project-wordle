from get_guess_fn import get_guess                 #
from is_game_over_fn import is_game_over           #
from modules import print_in_color                 #
from print_guess_fn import print_guess             #
####################################################
number_of_tries = 6 # total number of tries of the game
secret_word = input('Enter the secret word: ') # take the secret word as input
guess = input('Enter your guess: ') # take the guess as input
tries_left = 5
wordle_control = is_game_over(secret_word, guess, tries_left) # see if the guess and secret word matches to find whether to continue or not
while wordle_control == False: # if the guess do not match
  required_letters = print_guess(secret_word, guess)  # prints the letters in color and create the list of GREEN and YELLOW required letters
  guess = get_guess(required_letters) # retake guess and check if it is valid using the created function
  tries_left -= 1 # decrement tries
  wordle_control = is_game_over(secret_word, guess, tries_left) # check if guess matches and if game is over
