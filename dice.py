"""
YATZY!!!!!!!!!!
"""

from random import randint
from time import sleep

class Player():
    
    def __init__(self, name):
        self.name = name
        
    def points(self):
        pass
    
    def rolls_left(self):
        pass

def roll_dice():
    '''
    Den här funktionen slår en tärning och returnerar tärningskastets värde
    '''
    dice_roll = randint(1, 6)
    print ('Rolling dice...')
    sleep(1)
    print ('The die roll is a %d' % dice_roll)
    return dice_roll

def re_roll(n):
    '''
    Kallar på funktionen dice_roll n gånger
    '''
    pass

def save_dice(lista):
    '''
    Lagrar tärninskasten i en lista, ska också fråga spelaren vilka 
    tärningar som ska sparas och kalla på roll_dice för att kasta om
    resterande tärningar
    '''
    pass

def score(tärningskast):
    '''
    Håller koll på hur mycket poäng spelaren har
    '''
    pass

def main():
    '''
    Kallar bara på andra funktioner
    '''
    pass

main()