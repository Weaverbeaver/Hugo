"""module provides high level functions for creating websites with hugo"""
import subprocess
import os
#import random
import shutil
from urllib.request import urlretrieve
from modules.generators import generate_image, generate_company, generate_bio
from modules.website import Website
from modules.scanfiles import insert_index


def hugo_execute():
    """execute hugo commandx, creating html+css in public folder"""

    if os.path.exists("public/"):
        shutil.rmtree("public/")

    result = subprocess.run(
        "hugo",
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )

    # output result
    print(result.stdout)
    return result


def team_page_build(people_desc, gen_images_bool):
    """Concatenate all people into 1 page. People names are bolded."""

    if os.path.exists("static/"):
        shutil.rmtree("static/")
    os.makedirs("static/images/")

    if gen_images_bool is True:
        for i in enumerate(people_desc):

            name_nospace = people_desc[i[0]][0].replace(' ',"")
            biophoto = generate_image(str(people_desc[i[0]][0]),str(people_desc[i[0]][2]),"company")
            urlretrieve(biophoto, "static/images/" + name_nospace + ".png")
            people_desc[i[0]][0] = "**" + people_desc[i[0]][0] + "**" + " " + people_desc[i[0]][2]
            people_desc[i[0]][1] = "![" + name_nospace + "](/images/" + \
            name_nospace + ".png) \n\n" + people_desc[i[0]][1] + "\n"
            people_desc[i[0]][2] = ""

        team_text = '\n\n'.join(str(item) for innerlist in people_desc for item in innerlist)

    else:
        for i in enumerate(people_desc):

            people_desc[i[0]][0] = "**" + people_desc[i[0]][0] + "**" + " " + people_desc[i[0]][2]
            people_desc[i[0]][1] = people_desc[i[0]][1] + "\n"
            people_desc[i[0]][2] = ""

        team_text = '\n\n'.join(str(item) for innerlist in people_desc for item in innerlist)

    return team_text


def create_website(person, role, themes):
    """Generates a company name for the person and role.
    Returns a website class instance"""

    this_website = Website()
    this_website.read_toml()
    this_website.update_title(generate_company())
    description = generate_bio(
        thisperson=person, thisrole=role, thiscompany=this_website.toml["title"]
        )
    insert_index(person,description,"content","_index.md","main")
    print(themes)
    this_website.update_theme("ananke")
    print(this_website)
    this_website.write_toml()
    return this_website
