"""module provides functions to open/edit files necessary for hugo"""
import os

def get_themes():
    """function to open themes folder and get list of themes"""
    allthemes = os.listdir("themes/")
    print(allthemes)
    return allthemes
