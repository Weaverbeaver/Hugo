"""module provides functions for taking a title inputand generating text and an image from this"""
import random
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from langchain.agents import load_tools, initialize_agent
import openai
from modules.website import Website
from modules.hugorun import insert_index


def generate_company():
    """input title"""
    llms = OpenAI(temperature=0.9)
    newtitle = llms("Write a company name")
    return newtitle


def generate_person(thisrole):
    """generate a person's name"""
    llms = OpenAI(temperature=0.9)
    newtitle = (llms("Write the name of a " + thisrole)).replace("\n","")
    return newtitle


def generate_bio(thisperson, thisrole, thiscompany):
    """generate text from title"""
    llms = OpenAI(temperature=0.9)
    bio_template = PromptTemplate(
        input_variables=["thisperson", "thisrole", "thiscompany"],
        template=(
            "Write a biography about {thisperson}"
            "to go on the company website."
            " {thisperson} is the {thisrole} of {thiscompany}."
            "Maximum 1130 characters."
        ),
    )
    bio_chain = LLMChain(llm=llms, prompt=bio_template)
    bio = bio_chain.run(
        {"thisperson": thisperson, "thisrole": thisrole, "thiscompany": thiscompany}
    )
    print(bio)
    return bio


def generate_image(thisperson, thisrole):
    """generate an image with Dall-E and return the URL for download"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    image_prompt = (
        "Create a photo of "
        + thisperson
        + ", who is the "
        + thisrole
        + " of a company to accompany their biography on the company website"
    )
    photo = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="256x256",
    )
    return photo["data"][0]["url"]


def generate_website(person, role, themes):
    """Generates a company name for the person and role.
    Returns a website class instance"""
    this_website = Website()
    this_website.read_toml()
    this_website.update_title(generate_company())
    description = generate_bio(
        thisperson=person, thisrole=role, thiscompany=this_website.toml["title"]
        )
    insert_index(person,description,role,"content")
    #this_website.update_theme(random.choice(themes))
    print(random.choice(themes))
    this_website.update_theme("ananke")
    this_website.write_toml()
    return this_website
