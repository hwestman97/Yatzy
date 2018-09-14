"""This program is a game, a pair of dice are rolled, the computer adds the
value of the dice and asks the user to guess the value, if the user is correct
she/he wins, otherwise the computer wins."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Guess the value of the dice: "))
  return guess

def check(number_of_sides):
    max_val = number_of_sides*2
    print ('The maximum value of the dice roll is %d' %(max_val))
    guess = get_user_guess()
    if guess > max_val:
      print ('Too high! Guess again')
      guess = check(number_of_sides)
      return guess
    else:
      return guess

def roll_dice(number_of_sides):
    guess = check(number_of_sides)
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    print ('Rolling dice...')
    sleep(2)
    print ('The first roll is a %d' % first_roll)
    sleep(1)
    print ('The second roll is a %d' % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print ('The total of the dice roll is %d' % total_roll)
    print ('Result...')
    sleep(1)
    if guess == total_roll:
      print ('You win! Congratulations!')
    else:
      print ('You lost! Sorry.')
    
roll_dice(6)

