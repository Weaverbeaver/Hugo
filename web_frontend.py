"""Import all the modules"""
import os
import random
import shutil
from urllib.request import urlretrieve
import streamlit
from apikey import APIKEY
from modules.website import Website
from modules.generators import (
    generate_company,
    generate_person,
    generate_bio,
    generate_image,
    generate_company_people,
    generate_bios,
    make_unit_name,
    generate_military_unit
)
from modules.scanfiles import get_themes, insert_index, zip_web
from modules.hugorun import hugo_execute, create_website, team_page_build

os.environ["OPENAI_API_KEY"] = APIKEY

# Create application
streamlit.title("Website generator")

versions = ["Individuals","Companys","Units"]
version_select = streamlit.radio("What would you like to generate", versions, index=None)

if version_select == "Individuals":

    person = streamlit.text_input("Enter name of person")
    roles = ["CEO", "CIO", "CFO", "CTO"]
    role = streamlit.radio("Role", roles, index=3)
    sites = streamlit.slider("Websites", min_value=1, max_value=10)
    all_themes = get_themes()

    if person:
        for x in range(1, sites + 1):
            company = generate_company()
            streamlit.write(company)
            if x > 1:
                person = generate_person(role)
            bio = generate_bio(person, role, company)
            streamlit.write(bio)
            biophoto = generate_image(person, role, "individual")
            streamlit.image(
                biophoto,
                caption=person + ", " + role,
                width=256,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="auto",
            )
            if os.path.exists("content/"):
                shutil.rmtree("content/")
                os.mkdir("content/")
            create_website(person=person, role=role, themes=all_themes)
            hugo_execute()
            urlretrieve(biophoto, "public/bio.png")
            zip_web("generated_pages",person,"public")


elif version_select == "Companys":

    INSERT_NAME = "no"
    INSERT_ROLE = ""

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


elif version_select == "Units":

    site_num = streamlit.slider("How many military units to generate?"\
                                , min_value=1, max_value=10, value=1)
    # insert_name_bool = streamlit.toggle("Insert a name?", value=False)
    # if insert_name_bool:
    #     INSERT_NAME = streamlit.text_input("Enter name of the unit")
    # gen_image_bool = streamlit.toggle("Generate images?", value=False)

    if streamlit.button("Generate Military Units"):

        for i in range(0, site_num):
            print(f"Generating Military Unit {i + 1}")

            unit_name = make_unit_name()

            streamlit.subheader(f"**{unit_name}**")

            about_unit = generate_military_unit(unit_name)

            streamlit.write(about_unit[0])
            streamlit.write(about_unit[1])

            if os.path.exists("content/"):
                shutil.rmtree("content/")
            os.mkdir("content/")

            this_website = Website()
            this_website.read_toml()
            this_website.update_title(unit_name)
            this_website.update_theme("hugo-theme-w3css-basic")
            this_website.write_toml()

            hugo_execute()
            zip_web("generated_pages", unit_name.replace(" ", ""), "public")
