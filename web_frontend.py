"""Import all the modules"""
import os
import streamlit
from apikey import apikey
from modules.generators import generate_company, generate_bio
from modules.scanfiles import get_themes
from modules.generators import generate_website

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
        generate_website(person=person, role=role, themes=all_themes)
        # hugoexecute()
        # zip_web()
