"""python modules needed"""
import os
from modules.hugorun import hugoexecute  # , movewebfiles


def test_hugoexecute():
    """Comment for pylint, replace when test has been written.
    Test if hugo has generated correct html and css files in public with correct theme and title
    """
    test_execute = hugoexecute()
    print(test_execute)
    assert os.path.exists("public\\index.html")
    assert "error" not in test_execute.stdout


def test_movewebfiles():
    """Comment for pylint, replace when test has been written."""
    assert NotImplemented
