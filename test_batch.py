# Unit tests

import pytest
from main import *

def test_input_handler():
    test_inp = input_handler('test')
    assert test_inp == 'TEST'