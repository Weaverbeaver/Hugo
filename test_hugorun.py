"""python modules needed"""
import os
from modules.hugorun import hugoexecute  # , movewebfiles


def test_hugoexecute():
    """Comment for pylint, replace when test has been written. test if hugo has generated correct html and css files in public with correct theme and title"""
    test_execute = hugoexecute()
    print(test_execute)
    assert os.path.exists("public\\index.html")


def test_movewebfiles():
    """Comment for pylint, replace when test has been written."""
    return NotImplemented
