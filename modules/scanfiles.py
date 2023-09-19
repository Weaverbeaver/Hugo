"""module provides functions to open/edit files necessary for hugo"""
import os

def tomlwrite(newtheme, newtitle, themeline, titleline, lines):
    """function to write to hugo file"""
    lines[themeline] = "theme = '" + newtheme + "'\n"
    lines[titleline] = "title = '" + newtitle + "'\n"
    with open("hugo.toml", "w", encoding="utf-8") as tomlfile:
        tomlfile.writelines(lines)
        return tomlfile


def opentoml():
    """function to open hugo.toml and find location of important entries"""
    with open("hugo.toml", "r", encoding="utf-8") as tomlfile:
        tomllines = tomlfile.readlines()

    # go through each line of hugo.toml and remember which lines theme and title are
    count = 0
    for i in tomllines:
        if "theme" in i:
            themeline = count
        if "title" in i:
            titleline = count
        count += 1

    return themeline, titleline, tomllines


def getthemes():
    """function to open themes folder and get list of themes"""
    allthemes = os.listdir("themes/")
    print(allthemes)
    return allthemes
