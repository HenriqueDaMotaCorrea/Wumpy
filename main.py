# Wumpy
# Based on Hunt The Wumpus by Gregory Yob

help_text = """
    HELP: displays available commands and instructions.
    QUIT: exits the game.
"""

intro_text = """
    Welcome to Wumpy!
    Type HELP for instructions.
"""

# Rooms are arranged as vertices of a dodecahedron
map = [
    [2, 5, 8], #Room 1
    [1, 3, 10], #Room 2
    [2, 4, 12], #Room 3
    [3, 5, 14], #Room 4
    [1, 4, 6], #Room 5
    [5, 7, 15], #Room 6
    [6, 8, 17], #Room 7
    [1, 7, 9], #Room 8
    [8, 10, 18], #Room 9
    [2, 9, 11], #Room 10
    [10, 12, 19], #Room 11
    [3, 11, 13], #Room 12
    [12, 14, 20], #Room 13
    [4, 13, 15], #Room 14
    [6, 14, 16], #Room 15
    [15, 17, 20], #Room 16
    [7, 16, 18], #Room 17
    [9, 17, 19], #Room 18
    [11, 18, 20], #Room 19
    [13, 16, 19] #Room 20
]

class Room():
    def __init__(self, id=0, connections=[], messages=[]):
        self.id = id
        self.connections = connections
        self.messages = messages

def assemble_level(map=[]):
    level = []
    for i in range(1, len(map)+1):
        r = Room(i, map[i-1])
        level.append(r)
    return level

def show_help():
    print(help_text)

def quit_game():
    raise SystemExit()

def input_handler(raw_in):
    proc_in = str.upper(raw_in)
    return proc_in

def command_handler(cmd_dict, cmd_name, default_cmd=None):
    return cmd_dict.get(cmd_name, default_cmd)

def game():
    commands = {
        'HELP': show_help,
        'QUIT': quit_game
    }
    level = assemble_level(map)

    print(intro_text)
    
    while True:
        cmd_in = input_handler(input('>'))
        command_handler(commands, cmd_in, show_help)()

def main():
    game()

if __name__ == '__main__':
    main()