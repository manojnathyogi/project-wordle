### DO NOT MODIFY ###
import sys
from modules import print_in_color
guess = str(sys.argv[1]).upper()
required_letters = sys.argv[2].split(',')
### DO NOT MODIFY ###

# Write code below so that it checks if the user's guess contains
# ALL of the required letters using the variables guess and `required_letters` 
# (you don't need to set these variables). Assume `required_letters`
# is a list. You should print 'The guess is valid!' if it does and an empty string, "", otherwise.
for char in required_letters:
  does_guess_contain_required_letter = char in guess
  if not does_guess_contain_required_letter:
    break

if does_guess_contain_required_letter:
  print('The guess is valid!')
else:
  print('') 