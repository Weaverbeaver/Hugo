"""Import all the modules"""
import os
import streamlit
from urllib.request import urlretrieve
from apikey import apikey
from modules.generators import (
    generate_company,
    generate_bio,
    generate_image,
    generate_website,
)
from modules.scanfiles import get_themes

# from modules.hugorun import hugoexecute, zip_web

os.environ["OPENAI_API_KEY"] = apikey

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
        urlretrieve(biophoto, "public/bio.png")
        generate_website(person=person, role=role, themes=all_themes)
        # hugoexecute()
        # zip_web()
