"""Import all the modules"""
import os
import streamlit
from apikey import apikey
from modules.generators import generate_company, generate_bio

os.environ["OPENAI_API_KEY"] = apikey

# Create application
streamlit.title("Website generator")
person = streamlit.text_input("Enter name of person")

if person:
    company = generate_company()
    streamlit.write(company)
    bio = generate_bio(person, company)
    streamlit.write(bio)
