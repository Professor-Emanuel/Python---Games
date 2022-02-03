    print("Please select an action")
    print("1) Attack")
    print("2) Heal")

    player_choice = input()
    # print(type(player_choice))

    if player_choice == '1':
        print("Attack")
        monster['health'] = monster['health'] - player['attack']
        player['health'] = player['health'] - monster['attack']
        print(monster['health'])
        print(player['health'])
    elif player_choice == '2':
        print('Heal player')
    else:
        print("Invalid input")
    # print(player['name'])