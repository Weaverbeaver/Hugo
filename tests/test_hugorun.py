"""python modules needed"""
import os
from modules.hugorun import hugo_execute


def test_hugo_execute():
    """Test if hugo has generated correct html and css files in public"""
    test_execute = hugo_execute()
    print(test_execute)
    assert "error" not in test_execute.stdout
    assert os.path.exists("public/index.html")
