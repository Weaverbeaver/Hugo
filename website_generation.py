"""import things"""
import random
from modules.scanfiles import get_themes
from modules.generators import generate_company, generate_bio  # , generate_image

# from modules.hugorun import hugoexecute  # , movewebfiles
from modules.website import Website


def generate_website(person, role, themes):
    """Generates a company name for the person and role.
    Returns a website class instance"""
    this_website = Website()
    this_website.read_toml()
    this_website.update_title(generate_company())
    this_website.update_description(
        generate_bio(
            thisperson=person, thisrole=role, thiscompany=this_website.toml["title"]
        )
    )
    this_website.update_theme(random.choice(themes))
    this_website.write_toml()
    return this_website


# run at the start of the program
all_themes = get_themes()
generate_website(person="Dave Smith", role="CTO", themes=all_themes)
