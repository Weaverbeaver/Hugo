"""python modules needed"""
from modules.hugorun import hugoexecute, movewebfiles
import os


def test_hugoexecute():
    """ Comment for pylint, replace when test has been written. test if hugo has generated correct html and css files in public with correct theme and title"""
    test_execute = hugoexecute()
    assert os.path.exists("public\index.html") == True


def test_movewebfiles():
    """ Comment for pylint, replace when test has been written."""
