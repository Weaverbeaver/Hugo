"""module provides functions for taking a title inputand generating text and an image from this"""
import random
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from modules.website import Website


def generate_company():
    """input title"""
    llms = OpenAI(temperature=0.9)
    newtitle = llms("Write a company name")
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
        ),
    )
    bio_chain = LLMChain(llm=llms, prompt=bio_template)
    bio = bio_chain.run(
        {"thisperson": thisperson, "thisrole": thisrole, "thiscompany": thiscompany}
    )
    return bio


def generate_image():
    """gen image"""
    return NotImplemented


def generate_website(person, role, themes):
    """Generates a company name for the person and role.
    Returns a website class instance"""
    this_website = Website()
    this_website.read_toml()
    this_website.update_title(generate_company())
    this_website.update_description(
        generate_bio(
            thisperson=person, thisrole=role, thiscompany=this_website.toml["title"]
        )
    )
    this_website.update_theme(random.choice(themes))
    this_website.write_toml()
    return this_website
