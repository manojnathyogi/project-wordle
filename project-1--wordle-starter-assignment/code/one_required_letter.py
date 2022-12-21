### DO NOT MODIFY ###
import sys
from modules import print_in_color
guess = str(sys.argv[1]).upper()
required_letters = sys.argv[2].split()
### DO NOT MODIFY ###

# Modify the condition below so that it checks if the user's guess contains
# the required letter using the variables `guess` and `required_letters` 
# (you don't need to set these variables). Assume required_letters
# is a list that only has one element

does_guess_contain_required_letter = required_letters[0] in guess # REPLACE THIS WITH YOUR CONDITION



### DO NOT MODIFY BELOW ###
if does_guess_contain_required_letter:
  print('The guess is valid!')
else:
  print('')
### DO NOT MODIFY ### 