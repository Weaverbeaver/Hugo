"""import things"""
import subprocess

# import sys - not used
import os
import random


def getthemes():
    """function to open themes folder and get list of themes"""
    allthemes = os.listdir("themes/")
    print(allthemes)
    return allthemes


def opentoml():
    """function to open hugo.toml and find location of important entries"""
    tomlfile = open("hugo.toml", "r", encoding="utf-8")
    tomllines = tomlfile.readlines()
    tomlfile.close()

    # go through each line of hugo.toml and remember which lines theme and title are
    count = 0
    for i in tomllines:
        if "theme" in i:
            themeline = count
        if "title" in i:
            titleline = count
        count += 1

    return themeline, titleline, tomllines


# def randomtheme():
#    """function to select a random theme (Not necessary?)"""
#    return 0


def titleinput():
    """input title"""
    title = "Weavsite"
    return title


def gentext():
    """generate text from title"""
    return NotImplemented


def genimage():
    """gen image"""
    return NotImplemented


def tomlwrite(newtheme, newtitle, themeline, titleline, lines):
    """function to write to hugo file"""
    lines[themeline] = "theme = '" + newtheme + "'\n"
    lines[titleline] = "title = '" + newtitle + "'\n"
    tomlfile = open("hugo.toml", "w", encoding="utf-8")
    tomlfile.writelines(lines)
    tomlfile.close()
    return tomlfile


def hugoexecute():
    """execute hugo commandx, creating html+css in public folder"""
    result = subprocess.run(
        ["pwsh.exe", "-Command", "hugo"],
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )
    # output result
    print(result.stdout)
    return result


def movewebfiles():
    """moves the generator contents to another folder"""
    return NotImplemented


### old!!!!!!!!!! ###
# def websitegen():
#     """function to generate the site, outputs into public folder"""
#     # list all themes in theme directory
#     allthemes = os.listdir("themes/")
#     print(allthemes)
#     # pick random theme in folder
#     themechoice = random.choice(allthemes)
#     print("Chosen theme = " + themechoice)

#     # change theme in hugo.toml
#     tomlfile = open("hugo.toml", "r")
#     lines = tomlfile.readlines()
#     tomlfile.close()
#     # theme will usually be stored in line 3, if not all lines are searched through
#     # if (len(lines)>=4) and ('theme' in lines[3]):
#     #     lines[3] = "theme = '"+themechoice+"'\n"
#     # else:
#     #     count = 0
#     #     for i in lines:
#     #         if 'theme' in i:
#     #             lines[count] = "theme = '"+themechoice+"'\n"
#     #         count += 1

#     # replace theme, title and description
#     lines[3] = "theme = '" + themechoice + "'\n"
#     lines[2] = "title = '" + title + "'\n"

#     tomlfile = open("hugo.toml", "w")
#     tomlfile.writelines(lines)
#     tomlfile.close()


# run at the start of the program
g_allthemes = getthemes()
g_themeline, g_titleline, g_tomllines = opentoml()

# run everytime a new site is generated
g_newtitle = titleinput()
g_themechoice = random.choice(g_allthemes)
tomlwrite(g_themechoice, g_newtitle, g_themeline, g_titleline, g_tomllines)
hugoexecute()
