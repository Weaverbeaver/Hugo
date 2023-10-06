"""python modules needed"""
from modules.scanfiles import opentoml, get_themes#, tomlwrite

def test_getthemes():
    """ tests if the themes have been retrieved """
    test_getthemes_obj = get_themes()
    assert isinstance(test_getthemes_obj, list)
    assert len(test_getthemes_obj) >= 1


def test_opentoml():
    """ tests if important entries have been retrieved from hugo.toml """
    test_opentoml_obj = opentoml()
    assert isinstance(test_opentoml_obj[0], int)
    assert isinstance(test_opentoml_obj[1], int)

#def test_tomlwrite():
#    """Comment for pylint, replace when test has been written."""
#    return NotImplemented
