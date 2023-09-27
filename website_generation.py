"""import things"""
import random
from modules.scanfiles import tomlwrite, opentoml, getthemes
from modules.generators import generate_company  # , generate_bio, generate_image
from modules.hugorun import hugoexecute  # , movewebfiles

# run at the start of the program
g_allthemes = getthemes()
g_themeline, g_titleline, g_tomllines = opentoml()

# run everytime a new site is generated
g_newtitle = generate_company()
g_themechoice = random.choice(g_allthemes)
tomlwrite(g_themechoice, g_newtitle, g_themeline, g_titleline, g_tomllines)
hugoexecute()
