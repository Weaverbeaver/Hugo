"""python modules needed"""
from website_generation import titleinput


def test_getthemes():
    """ tests if the themes have been retrieved """



def test_opentoml():
    """ tests if important entries have been retrieved from hugo.toml """



def test_titleinput():
    """ tests if the title of the hugo.toml matches up with what it is suppose to be"""
    test_object = titleinput()
    assert test_object == "Weavsite"

def test_gentext():
    """ Comment for pylint, replace when test has been written."""




def test_genimage():
    """ Comment for pylint, replace when test has been written."""



def test_tomlwrite():
    """ Comment for pylint, replace when test has been written."""


def test_hugoexecute():
    """ Comment for pylint, replace when test has been written."""



def test_movewebfiles():
    """ Comment for pylint, replace when test has been written."""
