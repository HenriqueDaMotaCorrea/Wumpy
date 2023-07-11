# Wumpy
# Based on Hunt The Wumpus by Gregory Yob

def input_handler(raw_input):
    proc_input = str.upper(raw_input)
    return proc_input

def game():
    while True:
        print('Type QUIT to leave:')
        command = input_handler(input('>'))
        if command == 'QUIT':
            raise SystemExit()

def main():
    game()


if __name__ == "__main__":
    main()