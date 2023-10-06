"""python modules needed"""
from modules.scanfiles import get_themes#, toml_write, open_toml

def test_getthemes():
    """ Tests if the themes have been retrieved """
    test_getthemes_obj = get_themes()
    assert isinstance(test_getthemes_obj, list)
    assert len(test_getthemes_obj) >= 1


# unused function
#def test_open_toml():
#    """ tests if important entries have been retrieved from hugo.toml """
#    test_opentoml_obj = open_toml()
#    assert isinstance(test_opentoml_obj[0], int)
#    assert isinstance(test_opentoml_obj[1], int)

# unused function
#def test_toml_write():
#    """Comment for pylint, replace when test has been written."""
#    return NotImplemented
