# Wumpy
# Based on Hunt The Wumpus by Gregory Yob

import sys, random
from objects import *
from texts import *

def assemble_level(map={}):
    level = {}
    for key in map.keys():
        r = Room(key, map.get(key))
        level.update({r.name: r})
    return level

def get_neighbors(ent=Entity, ent_list=[]):
    neighbors = []
    for r_name in ent.location.connections:
        for e in ent_list:
            if e.location.name == r_name:
                neighbors.append(e)
    return neighbors

def invalid_command():
    print(text_invalid)

def show_help():
    print(text_help)

def input_handler(raw_in):
    proc_in = str.upper(raw_in)
    return proc_in

def main():
    # Rooms are arranged as vertices of a dodecahedron
    map = {
        '1': ['2', '5', '8'], #Room 1
        '2': ['1', '3', '10'], #Room 2
        '3': ['2', '4', '12'], #Room 3
        '4': ['3', '5', '14'], #Room 4
        '5': ['1', '4', '6'], #Room 5
        '6': ['5', '7', '15'], #Room 6
        '7': ['6', '8', '17'], #Room 7
        '8': ['1', '7', '9'], #Room 8
        '9': ['8', '10', '18'], #Room 9
        '10': ['2', '9', '11'], #Room 10
        '11': ['10', '12', '19'], #Room 11
        '12': ['3', '11', '13'], #Room 12
        '13': ['12', '14', '20'], #Room 13
        '14': ['4', '13', '15'], #Room 14
        '15': ['6', '14', '16'], #Room 15
        '16': ['15', '17', '20'], #Room 16
        '17': ['7', '16', '18'], #Room 17
        '18': ['9', '17', '19'], #Room 18
        '19': ['11', '18', '20'], #Room 19
        '20': ['13', '16', '19'] #Room 20
    }
    level = assemble_level(map)

    #TODO: Randomize start points
    player_room = level['1']
    wumpus_room = level['20']
    pit1_room = level['5']
    pit2_room = level['6']
    bat1_room = level['7']
    bat2_room = level['8']

    player = Entity(location=player_room)
    wumpus = Entity(location=wumpus_room, message=text_wumpus_msg)
    pit1 = Entity(location=pit1_room, message=text_pit_msg)
    pit2 = Entity(location=pit2_room, message=text_pit_msg)
    bat1 = Entity(location=bat1_room, message=text_bat_msg)
    bat2 = Entity(location=bat2_room, message=text_bat_msg)
    
    hazards = [wumpus, pit1, pit2, bat1, bat2]

    print(text_intro)
    
    while True:
        current_loc = level[player.location.name]
        print(text_roomdesc.format(current_loc.name, current_loc.connections))

        neighbors = get_neighbors(player, hazards)
        if len(neighbors) > 0:
            for n in neighbors:
                print(n.message)
        
        cmd = input_handler(input('> '))

        if cmd == 'QUIT' or cmd == 'Q':
            break
        elif cmd == 'HELP' or cmd == 'H':
            show_help()
        elif cmd == 'MOVE' or cmd == 'M':
            cmd = input_handler(input(text_wheremove))
            if cmd in level.keys():
                #TODO: Make it check the Room object's name instead of level[key]
                newroom = player.move_connected(level[cmd])
                if newroom == False:
                    print(text_nomove)
                else:
                    if newroom.name == pit1.location.name:
                        print(text_pit_fall)
                    elif newroom.name == pit2.location.name:
                        print(text_pit_fall)
                    elif newroom.name == bat1.location.name:
                        print(text_bat_snatch)
                    elif newroom.name == bat2.location.name:
                        print(text_bat_snatch)
                    elif newroom.name == wumpus.location.name:
                        print(text_wumpus_bump)
            else:
                print(text_nosuchroom)
        elif cmd == 'SHOOT' or cmd == 'S':
            cmd = input_handler(input(text_whereshoot))
            if cmd in level.keys():
                if level[cmd].is_connected(player.location):
                    if level[cmd].name == wumpus.location.name:
                        print(text_win)
                        break
                    else:
                        wumpus.move_connected(level[random.choice(wumpus.location.connections)])
                        print(text_arrow_miss)
                else:
                    print(text_noshoot)
            else:
                print(text_nosuchroom)
        else:
            invalid_command()
    
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt as exc:
        sys.stdout.write(str(exc))
        sys.exit(0)