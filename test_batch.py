# Tests for TDD
# To run tests: enter "pytest" in terminal

import pytest
from main import *

# Commands
def test_input_handler():
    test_inp = input_handler('test')
    assert test_inp == 'TEST'

def test_command_handler_function_matching():
    def test_command():
        pass

    test_dict = {
        'TEST': test_command
    }
    test_cmd = command_handler(test_dict, 'TEST')
    assert test_cmd == test_command

def test_command_handler_default_matching():
    def test_command():
        pass
    
    def test_default_func():
        pass

    test_dict = {
        'TEST': test_command
    }
    test_cmd = command_handler(test_dict, 'NOTTEST', test_default_func)
    assert test_cmd == test_default_func

# Room
def test_room_id():
    id = 1
    test_room = Room(id)
    assert test_room.id == id

def test_room_connections():
    id = 1
    connect = [2, 3, 4]
    test_room = Room(id, connect)
    assert test_room.connections == connect

def test_room_messages():
    id = 1
    connect = [2, 3, 4]
    msg = ['msg1', 'msg2']
    test_room = Room(id, connect, msg)
    assert test_room.messages == msg

def test_assemble_level():
    pentagon = [[2,5],[1,3],[2,4],[3,5],[1,4]]
    r1 = Room(1, pentagon[0])
    r2 = Room(2, pentagon[1])
    r3 = Room(3, pentagon[2])
    r4 = Room(4, pentagon[3])
    r5 = Room(5, pentagon[4])
    lvl = {
        '1': r1,
        '2': r2,
        '3': r3,
        '4': r4,
        '5': r5
    }
    test_level = assemble_level(pentagon)
    for key in list(test_level):
        assert test_level[key].id == lvl[key].id
        assert test_level[key].connections == lvl[key].connections

def test_room_is_connected():
    map = [[2],[1]]
    r1 = Room(1, map[0])
    r2 = Room(2, map[1])
    assert r1.is_connected(r2) == True

# Entity
def test_entity_location():
    loc = Room()
    test_entity = Entity(location=loc)
    assert test_entity.location == loc

def test_entity_move():
    r1 = Room(1)
    r2 = Room(2)
    test_entity = Entity(location=r1)
    test_entity.move(r2)
    assert test_entity.location == r2

"""
def test_entity_move_connected():
    map = [[2],[1]]
    r1 = Room(1, map[0])
    r2 = Room(2, map[1])
    lvl = [r1, r2]
    test_entity = Entity(location=r1)
    test_entity.move_connected(r2)
    assert test_entity.location == r2

def test_entity_move_connected_invalid():
    map = [[2],[1,3],[2]]
    r1 = Room(1, map[0])
    r2 = Room(2, map[1])
    r3 = Room(3, map[2])
    lvl = [r1, r2, r3]
    test_entity = Entity(location=r1)
    assert test_entity.move_connected(r3) == False
"""