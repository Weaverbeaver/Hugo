"""python modules needed"""
from modules.generators import titleinput, gentext, genimage


def test_titleinput():
    """tests if the title of the hugo.toml matches up with what it is suppose to be"""
    test_titleinput_obj = titleinput()
    assert isinstance(test_titleinput_obj, str)


def test_gentext():
    """Comment for pylint, replace when test has been written."""
    test_gentext_obj = gentext("Test company")
    assert isinstance(test_gentext_obj, str)


def test_genimage():
    """Comment for pylint, replace when test has been written."""
    genimage_output = genimage()
    assert genimage_output == NotImplemented
