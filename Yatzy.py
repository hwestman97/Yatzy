"""
YATZY!!!!!!!!!!
"""

from random import randint
from time import sleep

class Player():
    '''
    Skapar ett objekt, spelar, som håller koll på poäng och spelkortet.
    '''
    points = 0
    
    def __init__(self, name):
        self.name = name
        
    def add_points(self, new_points):
        Player.points += new_points

class ScoreBoard():
    '''
    Här definieras alla kombinationer av tärningar som ger poäng, varje spelare 
    har sitt eget spelkort där tagna kombinationer kryssas av.
    '''
    def __init__(self, player):
        self.player = player
    
    def first_section(self, dictionary):
        combos = {}
        names = ['ettor', 'tvåor', 'treor', 'fyror', 'femmor', 'sexor']
        for key in dictionary:
            points = dictionary[key]*key
            if points > 0:
                combos.update({names[key-1]:points})
        return combos
        
    def second_section(self, dictionary):
        small_ladder = {1:1, 2:1, 3:1, 4:1, 5:1, 6:0}
        big_ladder = {1:0, 2:1, 3:1, 4:1, 5:1, 6:1}
        combos = {}
        for key in dictionary:
            if dictionary[key] == 5:
                print('Yatzy!')
                combos.update({'Yatzy':50})
        if dictionary == small_ladder:
            print('Du fick en liten stege!')
            combos.update({'small ladder':15})
        elif dictionary == big_ladder:
            print('Du fick en stor stege!')
            combos.update({'big ladder':20})
        return combos

def roll_dice():
    '''
    Den här funktionen slår en tärning och returnerar tärningskastets värde.
    '''
    dice_roll = randint(1, 6)
    #print ('Kastar tärningen...')
    #sleep(1)
    #print ('Det blev en %d' % dice_roll)
    return dice_roll

def roll(n):
    '''
    Kallar på funktionen dice_roll n gånger och lagrar kasten i en lista.
    '''
    dice_rolls = []
    for x in range(n):
        dice_roll = roll_dice()
        dice_rolls.append(dice_roll)
    print('Resultatet av tärningskastet blev: ' + " ".join([str(x) for x in dice_rolls]))
    return dice_rolls

def save_dice(dice_rolls, saved_dice, n):
    '''
    Frågar spelaren vilka tärningar som ska sparas och lägger till dem i en 
    separat lista, retunerar hur många tärningar som ska kastas om och 
    listan med sparade tärningar.
    '''
    if n == 1:
        for number in dice_rolls:
            saved_dice.append(number)
        return 0, saved_dice
    else:
        user_input = input('Vilka tärningar vill du spara? ')
        if user_input == 'X':
            return len(dice_rolls), saved_dice
        else:
            dice_number = list(user_input)
            for number in dice_number:
                index = int(number)
                saved_dice.append(dice_rolls[index-1])
            saved_dice.sort()
            print('Dina sparade tärningar: ' + " ".join([str(x) for x in saved_dice]))
            return (len(dice_rolls)-len(dice_number)), saved_dice

def turn(player):
    '''
    Går igenom de funktioner som ska ske under en spelares tur. Alla tärningar 
    kastas, spelaren kan välja att spara några och kasta om resten upp till 
    två gånger, funktionen retunerar en lista med de tärningskast spelaren 
    fick den här turen.
    '''
    rolls = 5
    rolls_left = 3
    saved_dice = []
    while rolls_left >= 1 and rolls != 0:
        dice_rolls = roll(rolls)
        rolls, saved_dice = save_dice(dice_rolls, saved_dice, rolls_left)
        rolls_left -= 1 
    print('\nDina tärningar den här omgången: ' + " ".join([str(x) for x in (saved_dice)]))
    return saved_dice

def score(dice, player, scoreboard):
    '''
    Ska kalla på alla funktioner som behövs för att beräkna poängen för en tur.
    '''
    number_of_each_dice = {}
    for n in range(1,7):
        number_of_each_dice[n] = count_dice(dice, n)
    which_combo(number_of_each_dice, player, scoreboard)

def which_combo(dice_dict, player, scoreboard):
    combos = {}
    first_combos = scoreboard.first_section(dice_dict)
    second_combos = scoreboard.second_section(dice_dict)
    combos.update(first_combos)
    print(combos)

def count_dice(dice, n):
    '''
    Räknar hur många tärningar av sorten n spelaren fick under sin tur.
    '''
    how_many = 0
    for x in dice:
        if x == n:
            how_many += 1
    return how_many

def main():
    '''
    Kallar bara på andra funktioner.
    '''
    player1 = Player('Kajsa')
    scoreboard1 = ScoreBoard(player1)
    rolled_dice = turn(player1)
    #rolled_dice = [1,1,1,1,1]
    score(rolled_dice, player1, scoreboard1)

main()
