"""import things"""
from modules.scanfiles import get_themes

# from modules.hugorun import hugoexecute  # , movewebfiles
from modules.generators import generate_website


# run at the start of the program
all_themes = get_themes()
generate_website(person="Dave Smith", role="CTO", themes=all_themes)
# hugoexecute()
