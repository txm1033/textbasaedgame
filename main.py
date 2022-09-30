from PIL import Image

list_of_items = {1: 'knife', 2: 'gun', 3: 'ammo', 4: 'Map', 5: 'Red Key', 6: 'Blue Key'}


def store_items(items):
    items = {'test', 'test2'}
    return items


def directions_to_go():
    player_location = 'Lobby'
    player_location = input('Enter where you like to go. Remember you must find the map first to be able to'
                            'display it. You are currently in the Lobby')

    rooms = {
        'Lobby': {'West': 'Secretary Office', 'East': 'East Hallway', 'North': "Press Room", 'Item': 'knife'},
        'Secretary Office': {'South': 'Closest', 'West': 'West Hallway', 'East': 'Lobby', 'North': 'Conference Room'
                             },
        'Closet': {'East': 'Secretary Office', 'Item': 'Gun'},
        'West Hallway': {'North-East': 'Break Room', 'East': 'Secretary Office', 'Item': 'Ammo'},
        'Conference Room': {'South': 'Break Room', 'Item': 'Blue Key', 'West': 'West Hallway', 'East': 'Press Room'},
        'Press Room': {'South': 'Lobby', 'West': 'Conference Room', 'Enemy': 'Zombie 1'},
        'East Hallway': {'East': 'East Office', 'South West': 'Lobby'}
    }
    for location in rooms:
        if location == 'Lobby':
            print(rooms[location])
            if 'Item' in 'Lobby':
                print(f'You obtained ')
    return player_location


def display_map():
    user_input = input('Please type Map to display the map')
    current_inventory = store_items(user_input)
    for items in current_inventory:
        while True:
            if user_input not in items:
                print('hmm...I can\'t seem to find this item in your inventory',end="")
                break
            else:
                if 'Map' in list_of_items.values() and user_input == 'Map':
                    try:
                        im = Image.open("map/map.png")
                        im.show()
                    except IOError:
                        print('It seems we are having issues opening this file, try again later.')
                else:
                    print('Invalid input, please try again')


def intro_display():
    global user_name
    while True:
        user_name = input('State your name?\n')
        if user_name.isalpha():
            'Please enter a-z characters only'
            print(f'Hello,Agent {user_name} welcome to Mission 1: Escape the Police Station')
            # time.sleep(3)
            print('My name is Dexter and I am here to guide you on your mission\n'
                  'You are currently at J Edgar Hoover building and one of your coworkers have turned into a zombie\n'
                  'I managed to save you by injecting you with an antidote and giving you an ear piece so I can guide\n'
                  'you out of the police station. Just listen to everything I tell you and you will be fine.')
            # time.sleep(5)
            print('You have 3 objectives: \n\t'
                  'Collect 6 items in the map\n\t'
                  'Kill zombies\n\t'
                  'Escape\n')
            # time.sleep(3)
            print('You will need to find the following\t')
            for items in list_of_items.values():
                print('\t', items)

            print('If you run into any zombies before you have collected a knife or gun with ammo you will DIE.')
            break
        else:
            print('Uh-Oh, it seems you entered something other than letters, please try again or you will be eaten! '
                  'This '
                  'is\n '
                  'a matter of urgency')


if __name__ == '__main__':
    # playAgain = int(input('Would you like to play Operation Escape Route 1 for yes or 0 for no\n'))
    # while True:
    #     try:
    #         if playAgain == 1:
    #             intro_display()
    #             display_map()
    #             break
    #         elif playAgain == 0:
    #             print('Thanks for playing, Goodbye.')
    #             break
    #     except ValueError:
    #         print('Please enter valid input!')

    display_map()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
