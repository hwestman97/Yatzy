"""
YATZY!!!!!!!!!!
"""

from random import randint
from time import sleep

class Player():
    '''
    Skapar ett objekt, spelare, som håller koll på poäng och spelkortet.
    '''
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.first_section_options = {'ettor':True,'tvåor':True,'treor':True,'fyror':True,'femmor':True,'sexor':True}
        
    def add_points(self, new_points, player):
        player.points += new_points
        
    def show_options(self, player):
        list_of_options = []
        for key in player.first_section_options:
            if player.first_section_options[key] == True:
                list_of_options.append(key)
        return list_of_options

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
            combos.update({'liten stege':15})
        elif dictionary == big_ladder:
            print('Du fick en stor stege!')
            combos.update({'stor stege':20})
        return combos

def roll_die():
    '''
    Den här funktionen slår en tärning och returnerar tärningskastets värde.
    '''
    die_roll = randint(1, 6)
    #print ('Kastar tärningen...')
    #sleep(1)
    #print ('Det blev en %d' % die_roll)
    return die_roll

def roll(n):
    '''
    Kallar på funktionen dice_roll n gånger och lagrar kasten i en lista.
    '''
    dice_rolls = []
    for x in range(n):
        die_roll = roll_die()
        dice_rolls.append(die_roll)
    dice_rolls.sort()
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
    saved_dice.sort()
    print('\nDina tärningar den här omgången: ' + " ".join([str(x) for x in (saved_dice)]))
    return saved_dice

def which_combo(scoring_options, player):
    if len(scoring_options) > 0:
        print('\nDina valmöjligheter är:')
        for key in scoring_options:
            print(key, '\t', str(scoring_options[key]) + ' poäng')
        user_choice = input('Vad vill du lägga dina tärningar som? ')
        for key in scoring_options:
            if user_choice == key:
                player.add_points(scoring_options[key], player)
                player.first_section_options[key] = False
    else: 
        print('Du måste stryka något')
        for key in player.first_section_options:
            if player.first_section_options[key] == True:
                print(key)
        user_choice = input('Vad vill du stryka? ')
        for key in player.first_section_options:
            if user_choice == key:
                player.first_section_options[key] = False

def open_combos(dice_dict, player, scoreboard):
    open_first_combos = {}
    first_combos = scoreboard.first_section(dice_dict)
    for key in first_combos:
        if player.first_section_options[key] == True:
            open_first_combos.update({key:first_combos[key]})
    return open_first_combos
    #second_combos = scoreboard.second_section(dice_dict)

def count_dice(dice, n):
    '''
    Räknar hur många tärningar av sorten n spelaren fick under sin tur.
    '''
    how_many = 0
    for x in dice:
        if x == n:
            how_many += 1
    return how_many

def score(dice, player, scoreboard):
    '''
    Ska kalla på alla funktioner som behövs för att beräkna poängen för en tur.
    '''
    number_of_each_dice = {}
    for n in range(0,6):
        number_of_each_dice[n] = count_dice(dice, n)
    scoring_options = open_combos(number_of_each_dice, player, scoreboard)
    which_combo(scoring_options, player)

def play_first_round(player, scoreboard):
    rolled_dice = turn(player) #rolled_dice = [1,1,1,1,1] #rolled_dice = [1,2,2,1,1]
    score(rolled_dice, player, scoreboard)
    print('%s total poäng: %s' % (player.name, player.points))

def first_round(player1, player2, scoreboard1, scoreboard2):
    #for x in range(0,3):
    play_first_round(player1, scoreboard1)
    play_first_round(player2, scoreboard2)
    print(player1.first_section_options)
    print(player2.first_section_options)
    '''
    lst1 = player1.show_options(player1)
    lst2 = player2.show_options(player2)
    print(len(lst1), len(lst2))
    '''
    if player1.points > player2.points:
        print('%s vann!' % player1.name)
    elif player1.points < player2.points:
        print('%s vann!' % player2.name)
    elif player1.points == player2.points:
        print('Det blev lika')

def main():
    '''
    Kallar bara på andra funktioner.
    '''
    player1 = Player('Kajsa')
    scoreboard1 = ScoreBoard(player1)
    player2 = Player('Hanna')
    scoreboard2 = ScoreBoard(player2)
    first_round(player1, player2, scoreboard1, scoreboard2)

main()
