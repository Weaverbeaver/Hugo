import os
import random
import shutil
import streamlit
from modules.website import Website
from modules.generators import generate_company_people, generate_military_unit, generate_bios
from modules.hugorun import hugo_execute, team_page_build
from modules.scanfiles import insert_index, zip_web
from apikey import APIKEY

os.environ["OPENAI_API_KEY"] = APIKEY

# Create application
streamlit.title("Website generator (multi-page sites)")
max_people = streamlit.slider("Max num of people", min_value=2, max_value=8, value=3)
generate_type = streamlit.radio("Select type to generate", ["Company Page", "Military Unit Page"])
gen_image_bool = streamlit.toggle("Generate images?", value=False)

if streamlit.button("Go"):
    print("Start")
    num = random.randint(2, max_people)

    if generate_type == "Company Page":
        page_type = "Company"
        page_name = "Company XYZ"
        people_gen = generate_company_people(num, "any")
    else:
        page_type = "Military Unit"
        page_name = "Military Unit ABC"
        people_gen = generate_military_unit(num)

    people = people_gen[2:-1]

    streamlit.write(f"**{page_name} {page_type}**")
    streamlit.write(people_gen[1])
    streamlit.write(people_gen[-1])

    people_desc = generate_bios(people, f"{page_name} {page_type}")
    TEAM_TEXT = team_page_build(people_desc, gen_image_bool)

    streamlit.write(TEAM_TEXT)

    if os.path.exists("content/"):
        shutil.rmtree("content/")
    os.mkdir("content/")

    insert_index(f"{page_name} {page_type}", people_gen[1], "content", "_index.md", "main")
    insert_index("About", people_gen[-1], "content", "about.md", "sub")
    insert_index("The Team", TEAM_TEXT, "content", "team.md", "sub")

    this_website = Website()
    this_website.read_toml()
    this_website.update_title(f"{page_name} {page_type}")
    this_website.update_theme("ananke")
    this_website.write_toml()

    hugo_execute()
    zip_web("generated_pages", page_name.replace(" ", ""), "public")
