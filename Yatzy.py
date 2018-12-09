"""
YATZY!!!!!!!!!!
Summan av första delen
Andra delens poängsystem
Bot-spelare
pygame
se över funktionen roll
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
        self.first_section_options = {'ettor':True,'tvåor':True,'treor':True,
                                      'fyror':True,'femmor':True,'sexor':True}
        self.second_section_options = {'ett par':True,'två par':True,'triss':True,
                                       'fyrtal':True,'liten stege':True,
                                       'stor stege':True,'kåk':True,'chans':True,
                                       'yatzy':True}
        
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
        # rolled_dice = [1,2,2,6,6]
        # dictionary = {1:1, 2:2, 3:0, 4:0, 5:0, 6:2}
        #Kvar att fixa: två par, chans
        combos = {}
        full = False
        house = False
        full_house = {}
        two_pairs = []
        for key in dictionary:
            if dictionary[key] == 5:
                print('Yatzy!') #ta bort
                combos.update({'Yatzy':50})
            if dictionary[key] == 4:
                combos.update({'fyrtal':4*key})
            if dictionary[key] == 3:
                combos.update({'tretal':3*key})
                full = True
                full_house.update({3:key})
            if dictionary[key] == 2:
                two_pairs.append(key)
                house = True
                full_house.update({2: key})
                combos.update({'ett par' + ' %s' %key + ':or': 2 * key})
        if full == True and house == True:
            combos.update({'kåk':3*full_house[3]+2*full_house[2]})
        if len(two_pairs) == 2:
            combos.update({'två par': 2*(two_pairs[0]+two_pairs[1])})
        if len(two_pairs) == 3:
            pass
        ladder = ScoreBoard.check_for_ladders(dictionary)
        if ladder == True:
            combos.update(ladder)
        return combos

    def check_for_ladders(self, dictionary):
        ladder = {}
        small_ladder = {1:1, 2:1, 3:1, 4:1, 5:1, 6:0}
        big_ladder = {1:0, 2:1, 3:1, 4:1, 5:1, 6:1}
        if dictionary == small_ladder:
            ladder.update({'liten stege':15})
        elif dictionary == big_ladder:
            ladder.update({'stor stege':20})
        return ladder


def roll_die():
    '''
    Den här funktionen slår en tärning och returnerar tärningskastets värde.
    '''
    die_roll = randint(1, 6)
    #print ('Det blev en %d' % die_roll)
    return die_roll

def roll(n):
    '''
    Kallar på funktionen die_roll n gånger och lagrar kasten i en lista.
    '''
    dice_rolls = []
    print ('Kastar tärningar...')
    sleep(1)
    for x in range(n):
        die_roll = roll_die()
        dice_rolls.append(die_roll)
    dice_rolls.sort() #ska tas bort/flyttas
    print('Resultatet av tärningskastet blev: ' + " ".join([str(x) for x in dice_rolls])) #ska tas bort/flyttas
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
        my_dice = dice_rolls + saved_dice
        my_dice.sort()
        saved_dice = []
        print('Dina tärningar: ' + " ".join([str(x) for x in my_dice]))
        user_input = input('Vilka tärningar vill du spara? ')
        if user_input == 'X':
            return 5, []
        else:
            dice_number = list(user_input)
            for number in dice_number:
                index = int(number)
                saved_dice.append(my_dice[index-1])
            return (5-len(saved_dice)), saved_dice

def turn(player):
    '''
    Går igenom de funktioner som ska ske under en spelares tur. Alla tärningar 
    kastas, spelaren kan välja att spara några och kasta om resten upp till 
    två gånger, funktionen retunerar en lista med de tärningskast spelaren 
    fick den här turen.
    '''
    dice_to_roll = 5
    rolls_left = 3
    saved_dice = []
    while rolls_left >= 1 and dice_to_roll != 0:
        dice_rolls = roll(dice_to_roll)
        dice_to_roll, saved_dice = save_dice(dice_rolls, saved_dice, rolls_left)
        rolls_left -= 1 
    saved_dice.sort()
    print('\nDina tärningar den här omgången: ' + " ".join([str(x) for x in (saved_dice)]))
    return saved_dice

def scratch(player):
    for key in player.first_section_options:
        if player.first_section_options[key] == True:
            print(key)
    user_choice = input('Vad vill du stryka? ')
    for key in player.first_section_options:
        if user_choice == key:
            player.first_section_options[key] = False

def which_combo(scoring_options, player):
    if len(scoring_options) > 0:
        print('\nDina valmöjligheter är:')
        print('Skriv in X för att stryka något')
        for key in scoring_options:
            print(key, '\t', str(scoring_options[key]) + ' poäng')
        user_choice = input('Vad vill du lägga dina tärningar som? ')
        if user_choice == 'X':
            scratch(player)
        else:
            for key in scoring_options:
                if user_choice == key:
                    player.add_points(scoring_options[key], player)
                    player.first_section_options[key] = False
    else:
        print('Du måste stryka något')
        scratch(player)
        '''
        for key in player.first_section_options:
            if player.first_section_options[key] == True:
                print(key)
        user_choice = input('Vad vill du stryka? ')
        for key in player.first_section_options:
            if user_choice == key:
                player.first_section_options[key] = False
                '''

def open_combos(dice_dict, player, scoreboard):
    # rolled_dice = [1,2,2,6,6]
    # dice_dict = {1:1, 2:2, 3:0, 4:0, 5:0, 6:2}
    open_first_combos = {}
    first_combos = scoreboard.first_section(dice_dict)
    for key in first_combos:
        if player.first_section_options[key] == True:
            open_first_combos.update({key:first_combos[key]})
    return open_first_combos
    open_second_combos = {}
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
    for n in range(1,7):
        number_of_each_dice[n] = count_dice(dice, n)
    scoring_options = open_combos(number_of_each_dice, player, scoreboard)
    which_combo(scoring_options, player)

def play_first_round(player, scoreboard):
    rolled_dice = turn(player) #rolled_dice = [1,1,1,1,1] #rolled_dice = [1,2,2,6,6]
    score(rolled_dice, player, scoreboard)
    print('%ss total poäng: %s\n' % (player.name, player.points))

def first_round(player1, player2, scoreboard1, scoreboard2):
    for x in range(0,6):
        print('%ss tur!' % player1.name)
        play_first_round(player1, scoreboard1)
        print('%ss tur!' % player2.name)
        play_first_round(player2, scoreboard2)
    print('%s: %s poäng' % (player1.name, player1.points))
    print('%s: %s poäng' % (player2.name, player2.points))
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
    player1 = Player('Emmelie')
    scoreboard1 = ScoreBoard(player1)
    player2 = Player('Hanna')
    scoreboard2 = ScoreBoard(player2)
    first_round(player1, player2, scoreboard1, scoreboard2)

main()
'''
#test av score
player1 = Player('Kajsa')
scoreboard1 = ScoreBoard(player1)
rolled_dice = [1,2,2,6,6]
score(rolled_dice, player1, scoreboard1)
print('%ss total poäng: %s\n' % (player1.name, player1.points))

'''

