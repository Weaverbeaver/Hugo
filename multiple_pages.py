"""code for developing multiple page websites"""
import os
import random
import shutil
import streamlit
from modules.website import Website
from modules.generators import generate_company_people, generate_bios
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

    num = random.randint(2,max_people)
    company_gen = generate_company_people(3,"any")
    people = company_gen[2:-1]

    streamlit.write("**" + company_gen[0] + "**")
    streamlit.write(company_gen[1])
    streamlit.write(company_gen[-1])

    people_desc = generate_bios(people, company_gen[0])
    TEAM_TEXT = team_page_build(people_desc, gen_image_bool)

    streamlit.write(TEAM_TEXT)

    if os.path.exists("content/"):
        shutil.rmtree("content/")
    os.mkdir("content/")

    insert_index(company_gen[0],company_gen[1],"content","_index.md","main")
    insert_index("About",company_gen[-1],"content","about.md","sub")
    insert_index("The Team",TEAM_TEXT,"content","team.md","sub")

    this_website = Website()
    this_website.read_toml()
    this_website.update_title(company_gen[0])
    this_website.update_theme("ananke")
    this_website.write_toml()

    hugo_execute()
    zip_web("generated_pages",company_gen[0].replace(" ",""),"public")
