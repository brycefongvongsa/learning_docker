import pytest
import math
import sys
import os
from src import utils, exceptions

def test_add():
    assert utils.performOperation(20, 5, 2, operation='add') == 27
    print("test_add passed")

def test_subtract():
    assert utils.performOperation(20, 5, 2, operation='subtract') == 13
    print("test_subtract passed")

def test_multiply():
    assert utils.performOperation(20, 5, 2, operation='multiply') == 200
    print("test_multiply passed")

def test_divide():
    assert utils.performOperation(20, 5, 2, operation='divide') == 2.0
    print("test_divide passed")
    
def divisible_by_zero():
    try:
        utils.performOperation(20, 0, operation='divide') == "Invalid operation"
    except ZeroDivisionError:
        print("test_divide_by_zero passed")
    else:
        print("test_divide_by_zero failed")
