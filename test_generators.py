"""python modules needed"""
from modules.generators import generate_company, generate_bio, genimage


def test_generate_company():
    """tests if the title of the hugo.toml matches up with what it is suppose to be"""
    test_titleinput_obj = generate_company()
    assert isinstance(test_titleinput_obj, str)


def test_gen_bio():
    """Comment for pylint, replace when test has been written."""
    test_gen_bio_obj = generate_bio("Test company")
    assert isinstance(test_gen_bio_obj, str)


def test_genimage():
    """Comment for pylint, replace when test has been written."""
    genimage_output = genimage()
    assert genimage_output == NotImplemented
