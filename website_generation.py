"""import things"""
import random
from modules.scanfiles import tomlwrite, opentoml, getthemes
from modules.generators import titleinput, gentext, genimage
from modules.hugorun import hugoexecute, insertcontent, movewebfiles

# run at the start of the program
g_allthemes = getthemes()
g_themeline, g_titleline, g_tomllines = opentoml()


# run everytime a new site is generated
g_newtitle = titleinput()
g_newtext = gentext()
#g_themechoice = random.choice(g_allthemes)
insertcontent(g_newtitle, g_newtext)
tomlwrite("ananke", g_newtitle, g_themeline, g_titleline, g_tomllines)
hugoexecute()
