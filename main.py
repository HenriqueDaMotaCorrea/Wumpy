# Wumpy
# Based on Hunt The Wumpus by Gregory Yob

def input_handler(raw_in):
    proc_in = str.upper(raw_in)
    return proc_in

def command_handler(cmd_dict, cmd_name):
    return cmd_dict.get(cmd_name, show_help)

def show_help():
    print("""
          HELP: displays available commands and instructions.
          QUIT: exits the game.
        """)

commands = {
    'QUIT': SystemExit,
    'HELP': show_help,
}

def game():
    while True:
        print('Type QUIT to leave:')
        command = input_handler(input('>'))
        if command == 'QUIT':
            raise SystemExit()

def main():
    game()


if __name__ == '__main__':
    main()