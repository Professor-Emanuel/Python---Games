import random
from random import randint
# playes_name = 'Manuel'
# player_attack = 10
# player_health = 16
# health = 100

# player = ['Manuel', 10, 16, 100]
game_running = True
game_results = []

def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def game_ends(winner_name):
    print(f'{winner_name} won the game')

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'Manuel', 'attack': 10, 'heal':16, 'health': 100}
    #print(calculate_monster_attack())
    monster = {'name': 'Max', 'attack_min': 9, 'attack_max': 16, 'health': 100}

    print('---' * 7)
    print("Enter player name:")
    player['name'] = input()
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health.')
    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False 
        print('---' * 7)
        print("Please select an action")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit")
        print("4) Show results")

        player_choice = input()
        # print(type(player_choice))

        if player_choice == '1':
            print("Attack")
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True

            else:
                #monster_attack = randint(monster['attack_min'], monster['attack_max'])
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max']) #- monster_attack
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            print('Heal player')
            player['health'] = player['health'] + player['heal']

            #monster_attack = randint(monster['attack_min'], monster['attack_max'])
            player['health'] = player['health'] -calculate_monster_attack(monster['attack_min'], monster['attack_max']) #- monster_attack
            if player['health'] <= 0:
                monster_won = True
                
        elif player_choice == '3':
            new_round = False
            game_running = False
        elif player_choice == '4':
            for player_stat in game_results:
                print(player_stat)
                #print(game_results)

        else:
            print("Invalid input")
        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left.')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left.')
        
        elif player_won:
            game_ends(player['name'])
            round_result = {'name':player['name'], 'health':player['health'], 'rounds':counter}
            game_results.append(round_result)
            #print(game_results)
            #print(round_result)
            #print(player['name'] + ' won.')
            new_round = False

        elif monster_won == True:
            game_ends(monster['name'])
            round_result = {'name':monster['name'], 'health':monster['health'], 'rounds':counter}
            game_results.append(round_result)
            #print(game_results)
            #print(round_result)
            #print(monster['name'] + ' won.')
            new_round = False
        #if player['health'] <= 0 or monster['health'] <= 0 :
            #game_running = False
        # print(player['name'])

