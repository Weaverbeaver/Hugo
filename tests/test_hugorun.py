"""python modules needed"""
import os
from modules.hugorun import hugo_execute, zip_web, insert_index


def test_hugo_execute():
    """Test if hugo has generated correct html and css files in public"""
    test_execute = hugo_execute()
    print(test_execute)
    assert "error" not in test_execute.stdout
    assert os.path.exists("public/index.html")



def test_insert_index(tmp_path):
    """Tests that insert_index can create an index file in the content folder"""
    print(str(tmp_path)+"/content")
    insert_index("Joe","Good man","CEO",str(tmp_path)+"/content","_index.md","main")
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
