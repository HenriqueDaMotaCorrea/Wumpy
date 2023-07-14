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
    while True:
        print(intro_text)
        cmd_in = input_handler(input('>'))
        command_handler(commands, cmd_in, show_help)()

def main():
    game()

if __name__ == '__main__':
    main()