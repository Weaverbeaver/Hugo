import os
import random
import shutil
import streamlit
from modules.website import Website
from modules.generators import generate_company_people, generate_military_unit, generate_bios, generate_unit_type
from modules.hugorun import hugo_execute, team_page_build
from modules.scanfiles import insert_index, zip_web
from apikey import APIKEY

os.environ["OPENAI_API_KEY"] = APIKEY

# Create application
streamlit.title("Website generator (multi-page sites)")
max_people = streamlit.slider("Max num of people", min_value=2, max_value=8, value=3)
gen_image_bool = streamlit.toggle("Generate images?", value=False)

if streamlit.button("Go"):
    print("Start")
    num = random.randint(2, max_people)

    unit_name = generate_unit_type()
    print(unit_name)
    streamlit.write(unit_name)
    about_unit = generate_military_unit(unit_name)
    streamlit.write(about_unit[-2])
    streamlit.write(about_unit[-1])
    print(about_unit)

    if os.path.exists("content/"):
        shutil.rmtree("content/")
    os.mkdir("content/")

    insert_index(unit_name, about_unit[-2], "content", "_index.md", "main")
    insert_index("About", about_unit[-1], "content", "about.md", "sub")

    this_website = Website()
    this_website.read_toml()
    this_website.update_title(unit_name)
    this_website.update_theme("ananke")
    this_website.write_toml()

    hugo_execute()
    zip_web("generated_pages", unit_name.replace(" ", ""), "public")
