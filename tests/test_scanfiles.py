"""python modules needed"""
import os
from modules.scanfiles import get_themes, insert_index, zip_web

def test_getthemes():
    """ Tests if the themes have been retrieved """
    test_getthemes_obj = get_themes()
    assert isinstance(test_getthemes_obj, list)
    assert len(test_getthemes_obj) >= 1


def test_insert_index(tmp_path):
    """Tests that insert_index can create an index file in the content folder"""
    print(str(tmp_path)+"/content")
    insert_index("Joe","Good man",str(tmp_path)+"/content","_index.md","main")
    assert os.path.isfile(str(tmp_path)+"/content/_index.md")
    with open(str(tmp_path)+"/content/_index.md", 'r', encoding="utf-8") as index:
        assert index.readline() == "---\n"


def test_zip_web(tmp_path):
    """Tests that the zip_web function can zip files"""
    os.mkdir(str(tmp_path)+"/tester")
    with open(str(tmp_path)+"/tester/tester.txt", 'w', encoding="utf-8"):
        print(str(tmp_path)+"/tester.txt")
    zip_web(str(tmp_path),"testarchive",str(tmp_path)+"/tester/")
    assert os.path.isfile(str(tmp_path)+"/testarchive.zip")
