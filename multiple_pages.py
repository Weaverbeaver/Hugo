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

INSERT_NAME = "no"
INSERT_ROLE = ""

# Create application
streamlit.title("Website generator (multi-page sites)")
site_num = streamlit.slider("How many sites to generate?",min_value=1, max_value=10, value=1)
max_people = streamlit.slider("Max num of people", min_value=3, max_value=8, value=3)
insert_name_bool = streamlit.toggle("Insert a name?", value=False)
if insert_name_bool is True:
    streamlit.caption("If enabled, the entered name will be inserted into the first "\
                      "generated site. All following sites will generate as normal.")
    INSERT_NAME = streamlit.text_input("Enter name of person")
    roles = ["CEO", "CIO", "CFO", "CTO"]
    insert_role = streamlit.radio("Role", roles, index=3)
gen_image_bool = streamlit.toggle("Generate images?", value=False)

if streamlit.button("Go"):

    print(site_num)

    for i in range (0 , site_num):

        print("Start")
        print(i)

        num = random.randint(3,max_people)
        company_gen = generate_company_people(num,"any")
        people = company_gen[2:-1]

        streamlit.subheader("**" + company_gen[0] + "**")
        streamlit.write(company_gen[1])
        streamlit.write(company_gen[-1])

        people_desc = generate_bios(people, company_gen[0], INSERT_NAME, INSERT_ROLE)
        INSERT_NAME = "no"
        INSERT_ROLE = ""

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
