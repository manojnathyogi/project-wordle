### DO NOT MODIFY ###
import sys
from modules import print_in_color
secret_word = str(sys.argv[1]).upper()
guess = str(sys.argv[2]).upper()
### DO NOT MODIFY ###
# Create an expression that will determine if your program should print the first letter in yellow to the screen, based on the variables `secret_word` and `guess` (you don't need to set these variables). 

shoud_print_first_letter_green = secret_word[0] == guess[0] # COPY YOUR CODE FROM THE GREEN EXERCISE
shoud_print_first_letter_red = secret_word[0] != guess[0]  # COPY YOUR CODE FROM THE RED EXERCISE
if shoud_print_first_letter_green:
  print_in_color(guess[0], 'green')
elif shoud_print_first_letter_red: 
  if guess[0] in secret_word:
    print_in_color(guess[0], 'yellow')
  else:
    print_in_color(guess[0], 'red')
  
### Add your code here to correctly print the first letter as yellow 

