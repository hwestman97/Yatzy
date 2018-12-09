
from random import randint
from time import sleep

def roll_dice():
    '''
    Den här funktionen slår en tärning och returnerar tärningskastets värde
    '''
    dice_roll = randint(1, 6)
    print ('Rolling dice...')
    sleep(1)
    print ('The die roll is a %d' % dice_roll)
    return dice_roll

roll_dice()
