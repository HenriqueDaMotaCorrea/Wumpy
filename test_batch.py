# Tests for TDD
# To run tests: enter "pytest" in terminal

import pytest
from main import *

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