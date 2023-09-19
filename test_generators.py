"""python modules needed"""
from modules.scanfiles import tomlwrite, opentoml, getthemes
from modules.generators import titleinput, gentext, genimage
from modules.hugorun import hugoexecute, movewebfiles


def test_titleinput():
    """ tests if the title of the hugo.toml matches up with what it is suppose to be"""
    test_object = titleinput()
    assert test_object == "Weavsite" or "Stevesite"


def test_gentext():
    """ Comment for pylint, replace when test has been written."""



def test_genimage():
    """ Comment for pylint, replace when test has been written."""
