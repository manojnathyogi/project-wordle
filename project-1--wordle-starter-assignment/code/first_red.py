### DO NOT MODIFY ###
import sys
from modules import print_in_color
secret_word = str(sys.argv[1]).upper()
guess = str(sys.argv[2]).upper()
### DO NOT MODIFY ###
### Solution goes below here #####

# Create an expression that will determine if your program should print the first letter in red to the screen, based on the variables `secret_word` and `guess` (you don't need to set these variables). 
# Store that expression in `shoud_print_first_letter_red`. 

shoud_print_first_letter_red = (secret_word[0] != guess[0]) # REPLACE THIS CODE 

if shoud_print_first_letter_red: 
  # Replace this line so it prints the first letter in red using the print_in_color function
  # pass
  print_in_color(guess[0], 'red')
