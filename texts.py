# Text strings displayed in-game

#TODO: Add translation support

text_invalid = """What? (Enter [H]elp for instructions.)"""

text_help = """
Wumpy - Hunt the Wumpus in Python

Commands:
    - [Q]uit: exit the program
    - [H]elp: display commands and instructions
    - [M]ove: prompt to select a room to move into
    - [S]hoot: prompt to select a room to shoot into

Instructions:

    [YOU, THE PLAYER]
    You are hunting a Wumpus in its cave. The cave is made up of 20 rooms, 
    connected as the vertices of a dodecahedron. That means each room connects 
    to 3 other rooms.
    Every turn, you can choose to either MOVE or SHOOT an arrow into a room 
    that's connected to the one you're currently in.
    
    [PITS]
    Some rooms contain bottomless pits. You will FEEL A DRAFT if near one.
    If you enter a room with a pit, you'll plummet to your doom! Stay alert!

    [BATS]
    Bat swarms make the cave their home, you'll HEAR FLAPPING if they're close.
    If you disturb a swarm, they'll snatch you up and drop you somewhere else!

    [WUMPUS]
    Your objective is to find the Wumpus, and shoot an arrow into the room it 
    sleeps in. You will SMELL it when you get close.
    The Wumpus sleeps most of the time, but will wake up if:
    - You enter its room
    - You shoot an arrow and miss
    Upon waking up, the Wumpus has a 3 in 4 chance of moving to an adjacent 
    room, and a 1 in 4 chance of staying where it is.
    The Wumpus won't get carried by bats, nor fall down pits.
    If you enter the Wumpus' room and it stays, or if it moves into the room 
    you're in, you're toast!

    You know what to do now, so get out there and HUNT THE WUMPUS!
"""

text_intro = """
Welcome to Wumpy!
Enter [H]elp for instructions, or [Q]uit to leave."""

# Warnings
text_wumpus_msg = """That smell... the Wumpus is close by!"""

text_pit_msg = """You feel a draft."""

text_bat_msg = """You hear flapping!"""

# Events
text_pit_fall = """
'AAAAAAAA--' You fell into a pit!"""

text_bat_snatch = """
The bat swarm snatches you up and drops you in another room!"""

text_wumpus_bump = """
Bumped into a Wumpus!"""

text_wumpus_gotcha = """
The Wumpus gets you, and you get nothing!"""

text_win = """
YOU GOT THE WUMPUS! Good job!"""

text_lose = """
YOU LOSE!"""

text_arrow_miss = """
Didn't hit anything..."""

# Standard
text_roomdesc = """
You are in room {}. Exits to: {} ([M]ove/[S]hoot)"""

text_wheremove = """Room to go to? """

text_nomove = """
You can't get there from this room!"""

text_nosuchroom ="""
There's no such room."""

text_whereshoot = """Room to shoot into? """

text_noshoot = """
You can't shoot there from this room!"""

text_playagain = """
Would you like to play again?"""