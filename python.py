#import things
import subprocess, sys, os, random


# function to open themes folder and get list of themes
def getthemes():

    allthemes = os.listdir("themes/")
    print(allthemes)
    return allthemes


# function to open hugo.toml and find location of important entries
def opentoml():

    tomlfile = open("hugo.toml", "r")
    tomllines = tomlfile.readlines()
    tomlfile.close()

    # go through each line of hugo.toml and remember which lines theme and title are
    count = 0
    for i in tomllines:
        if 'theme' in i:
            themeline = count
        if 'title' in i:
            titleline = count
        count += 1
    
    return themeline, titleline, tomllines


# function to select a random theme (Not necessary?)
#def randomtheme():
#    return 0


# input title
def titleinput():
    title = "Weavsite"
    return title


# generate text from title
def gentext():
    return


# gen image
def genimage():
    return


# function to write to hugo file
def tomlwrite(newtheme, newtitle, themeline, titleline, lines):

    lines[themeline] = "theme = '"+newtheme+"'\n"
    lines[titleline] = "title = '"+newtitle+"'\n"

    tomlfile = open("hugo.toml", "w")
    tomlfile.writelines(lines)
    tomlfile.close()

    return


# execute hugo commandx, creating html+css in public folder
def hugoexecute():

    result = subprocess.run(["pwsh.exe", "-Command", "hugo"], shell=True, capture_output=True, text=True)
    #output result
    print(result.stdout)
    return

# moves the generator contents to another folder
def movewebfiles():
    return


### old!!!!!!!!!! ###
#function to generate the site, outputs into public folder
def websitegen(title):

    #list all themes in theme directory
    allthemes = os.listdir("themes/")
    print(allthemes)
    #pick random theme in folder
    themechoice = random.choice(allthemes)
    print("Chosen theme = "+themechoice)

    #change theme in hugo.toml
    tomlfile = open("hugo.toml", "r")
    lines = tomlfile.readlines()
    tomlfile.close()
    #theme will usually be stored in line 3, if not all lines are searched through
    # if (len(lines)>=4) and ('theme' in lines[3]):
    #     lines[3] = "theme = '"+themechoice+"'\n"
    # else:
    #     count = 0
    #     for i in lines:
    #         if 'theme' in i:
    #             lines[count] = "theme = '"+themechoice+"'\n"
    #         count += 1

    #replace theme, title and description
    lines[3] = "theme = '"+themechoice+"'\n"
    lines[2] = "title = '"+title+"'\n"


            

    tomlfile = open("hugo.toml", "w")
    tomlfile.writelines(lines)
    tomlfile.close()

# run at the start of the program
allthemes = getthemes()
themeline, titleline, tomllines = opentoml()

# run everytime a new site is generated
newtitle = titleinput()
themechoice = random.choice(allthemes)
tomlwrite(themechoice, newtitle, themeline, titleline, tomllines)
hugoexecute()