### DO NOT MODIFY ###
import sys
from modules import print_in_color
secret_word = str(sys.argv[1]).upper()
guess = str(sys.argv[2]).upper()
### DO NOT MODIFY ###

### Solution goes below here #####

# Create an expression that will compare `secret_word` and `guess` and print all of
# the letters in `guess` using the correct colors. Your solution from the last parts
# will be helpful here.

for index in range(0, len(guess)):
  shoud_print_first_letter_green = secret_word[index] == guess[index] # COPY YOUR CODE FROM THE GREEN EXERCISE
  shoud_print_first_letter_red = secret_word[index] != guess[index]  # COPY YOUR CODE FROM THE RED EXERCISE
  if shoud_print_first_letter_green:
    print_in_color(guess[index], 'green')
  elif shoud_print_first_letter_red: 
    if guess[index] in secret_word:
      print_in_color(guess[index], 'yellow')
    else:
      print_in_color(guess[index], 'red')
