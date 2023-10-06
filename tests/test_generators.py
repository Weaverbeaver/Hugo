"""python modules needed"""
import os
from urllib.request import urlretrieve
from modules.generators import generate_company, generate_bio, generate_image
from apikey import APIKEY

os.environ["OPENAI_API_KEY"] = APIKEY


def test_generate_company():
    """tests if the title of the hugo.toml matches up with what it is suppose to be"""
    test_generate_company_obj = generate_company()
    assert isinstance(test_generate_company_obj, str)
    assert len(test_generate_company_obj) > 10
    assert len(test_generate_company_obj) < 200


def test_gen_bio():
    """Tests that the bio is text of between 200 and 2000 characters."""
    test_gen_bio_obj = generate_bio("Test person", "Test role", "Test company")
    assert isinstance(test_gen_bio_obj, str)
    assert len(test_gen_bio_obj) > 200
    assert len(test_gen_bio_obj) < 2000


def test_gen_image(tmp_path):
    """Testing that bio.png is created and is larger than 100KB"""
    biophoto = generate_image("Joe","CEO")
    print(tmp_path)
    urlretrieve(biophoto, str(tmp_path)+"\\bio.png")
    assert os.path.isfile(str(tmp_path)+"\\bio.png")
    assert os.path.getsize(str(tmp_path)+"\\bio.png") > 100000
