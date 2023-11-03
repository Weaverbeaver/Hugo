import os
import random
import shutil
import streamlit
from modules.website import Website
from modules.generators import generate_unit_type, generate_military_unit, generate_military_vehicles
from modules.hugorun import hugo_execute
from modules.scanfiles import insert_index, zip_web

from apikey import APIKEY



os.environ["OPENAI_API_KEY"] = APIKEY

insert_name = "no"
insert_role = ""

# Create application
streamlit.title("Website generator (military multi-page sites)")
site_num = streamlit.slider("How many military units to generate?", min_value=1, max_value=10, value=1)
max_units = streamlit.slider("Max num of units", min_value=3, max_value=8, value=3)
insert_name_bool = streamlit.toggle("Insert a name?", value=False)
if insert_name_bool:
    insert_name = streamlit.text_input("Enter name of the unit")
gen_image_bool = streamlit.toggle("Generate images?", value=False)

if streamlit.button("Generate Military Units"):

    for i in range(0, site_num):
        print(f"Generating Military Unit {i + 1}")

        num = random.randint(3, max_units)
        unit_name = generate_unit_type()

        streamlit.subheader(f"**{unit_name}**")

        about_unit = generate_military_unit(unit_name)

        streamlit.write(about_unit[-2])
        streamlit.write(about_unit[-1])

        if gen_image_bool:
            unit_photos = generate_military_vehicles()
            for image in unit_photos:
                streamlit.image(image, caption="Military Vehicle")

        if os.path.exists("content/"):
            shutil.rmtree("content/")
        os.mkdir("content/")

        insert_index(unit_name, about_unit[-2], "content", "_index.md", "main")
        insert_index("About", about_unit[-1], "content", "about.md", "sub")

        this_website = Website()
        this_website.read_toml()
        this_website.update_title(unit_name)
        this_website.update_theme("hugo-theme-w3css-basic")
        this_website.write_toml()

        hugo_execute()
        zip_web("generated_pages", unit_name.replace(" ", ""), "public")

