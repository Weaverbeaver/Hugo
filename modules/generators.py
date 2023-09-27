"""module provides functions for taking a title inputand generating text and an image from this"""
# import os # only used for testing API key locally
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# os.environ["OPENAI_API_KEY"] = "api-key for testing"


def titleinput():
    """input title"""
    llms = OpenAI(temperature=0.9)
    newtitle = llms("Write a company name")
    return newtitle


def gentext(thiscompany):
    """generate text from title"""
    llms = OpenAI(temperature=0.9)
    bio_template = PromptTemplate(
        input_variables=["thiscompany"],
        template="Write a biography about the CIO of {thiscompany} to go on the company website",
    )
    bio_chain = LLMChain(llm=llms, prompt=bio_template)
    bio = bio_chain.run(thiscompany)
    return bio


def genimage():
    """gen image"""
    return NotImplemented
