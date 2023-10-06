"""Import all the modules"""
import os
from urllib.request import urlretrieve
import streamlit
from apikey import APIKEY
from modules.generators import (
    generate_company,
    generate_person,
    generate_bio,
    generate_image,
    generate_website,
)
from modules.scanfiles import get_themes
from modules.hugorun import hugo_execute, zip_web

os.environ["OPENAI_API_KEY"] = APIKEY

# Create application
streamlit.title("Website generator")
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
        biophoto = generate_image(person, role)
        streamlit.image(
            biophoto,
            caption=person + ", " + role,
            width=256,
            use_column_width=None,
            clamp=False,
            channels="RGB",
            output_format="auto",
        )
        generate_website(person=person, role=role, themes=all_themes)
        hugo_execute()
        urlretrieve(biophoto, "public/bio.png")
        zip_web("generated_pages",person,"public")
