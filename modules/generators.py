"""module provides functions for taking a title inputand generating text and an image from this"""
import os
import random
from urllib.request import urlretrieve
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from langchain.agents import load_tools, initialize_agent
import openai


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


def generate_bio(thisperson, thiscompany, thisrole):
    """generate text from title"""
    llms = OpenAI(temperature=0.9)
    bio_template = PromptTemplate(
        input_variables=["thisperson", "thisrole", "thiscompany"],
        template=(
            "Write a biography about {thisperson}"
            "to go on the company website."
            " {thisperson} is the {thisrole} of {thiscompany}."
            "Maximum 500 characters."
        ),
    )
    bio_chain = LLMChain(llm=llms, prompt=bio_template)
    bio = bio_chain.run(
        {"thisperson": thisperson, "thisrole": thisrole, "thiscompany": thiscompany}
    )
    print(bio)
    return bio


def generate_image(thisperson, thisrole, gen_type):
    """generate an image with Dall-E and return the URL for download"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if thisrole == "any":
        image_prompt = (
            "Create a professional photo of "
            + thisperson
            + "to accompany their biography on the company website"
        )
    else:
        image_prompt = (
            "Create a profeesional photo of "
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

    if os.path.exists("imagecache/") is False:
        os.mkdir("imagecache/")
    urlretrieve(photo["data"][0]["url"], "imagecache/" + gen_type + "-" \
                + thisrole + "-" +thisperson.replace(' ',"") + ".png")

    return photo["data"][0]["url"]


def generate_company_people(amount,field):
    """generate a company name, tagline and description, along with a specified number of names"""

    right_ats = False
    times = 0
    while not right_ats:
        llms = OpenAI(temperature=0.9)
        if field == "any":
            response = llms("Generate a list with each entry seperated by @ symbols"\
                            " comprising of the following entries:\n" \
                            "A realistic sounding company name.\n" \
                            "A tagline for the company.\n" \
                            + str(amount) + " full names.\n" \
                            "A 250 word description of the company.")
        else:
            response = llms("Generate a list with each entry seperated by @ symbols "\
                            "comprising of the following entries:\n" \
                            "A realistic sounding " + field + " company name.\n" \
                            "A tagline for the company.\n" \
                            + str(amount) + " full names.\n" \
                            "A 250 word description of the company.")

        print(response)
        ats_count = response.count("@")
        times = times + 1
        if ats_count == 3:
            right_ats = True
    print("amount of times ChatGPT generated this text is", times)
    response = (response.replace("@ ","@")).replace('"',"")
    formatted = response.split("@")

    for i in enumerate(formatted):
        if ":" in formatted[i[0]]:
            formatted[i[0]] = formatted[i[0]][formatted[i[0]].find(":")+1:]
        formatted[i[0]] = formatted[i[0]].strip("\n")
    #put into a function

    return formatted


def generate_bios(people, company, insert_name, insert_role):
    """generate a bio for each person input"""

    roles = ["CEO", "CIO", "CFO", "CTO", "CAO", "CCO", "CSO", "CMO"]

    if "," in people[0]:
        people = str(people[0]).split(",")

    people = [j.strip(" 123456789.") for j in people]


    if insert_name != "no":

        roles.remove(insert_role)
        person_array = [ [0]*3 for i in range(0, len(people)+1)]

    else:

        person_array = [ [0]*3 for i in people]


    loop = 0
    llms = OpenAI(temperature=0.9)

    for i in people:
        response = llms("Write a biography about " + i + " to go on the company website. " + i + \
                        " is the " + roles[loop] + " at " + company + ".Maximum 300 characters.")
        person_array[loop][0] = i
        person_array[loop][1] = response.replace("\n","")
        person_array[loop][2] = roles[loop]
        loop += 1

    if insert_name != "no":

        response = llms("Write a biography about " + insert_name + \
                        " to go on the company website. " + insert_name + \
                        " is the " + insert_role + " at " + company + ".Maximum 300 characters.")
        person_array[-1][0] = insert_name
        person_array[-1][1] = response.replace("\n","")
        person_array[-1][2] = insert_role

    return person_array


def generate_unit_type():
    """generate unit type"""
    unit_name = random.choice(["Signals", "Logistics", "Infantry", "Engineers", "Intelligence"])
    number = random.randint(100, 999)
    ordinal = "%d%s" % (number,"tsnrhtdd"[(number//10%10!=1)*(number%10<4)*number%10::4])
    unit_name = ordinal + " " + unit_name + " Unit"
    return unit_name

def generate_military_unit(unit_name):
    """Generate military unit name, motto, description, along with a specified number of names."""

    llms = OpenAI(temperature=0.9)

    response = llms("Generate a list with each entry separated by @ symbols comprising of "\
                    "the following entries:\n"
                    "A catchy motto or slogan for the unit " + unit_name + \
                    ", which isnt just the name of the unit.\n"
                    "A 250 word description of the military unit and their commanding officer.")

    response = (response.replace("@ ", "@")).replace('"', "")
    formatted = response.split("@")

    for i in enumerate(formatted):
        if ":" in formatted[i[0]]:
            formatted[i[0]] = formatted[i[0]][formatted[i[0]].find(":") + 1:]
        formatted[i[0]] = formatted[i[0]].strip("\n")

    return formatted


def generate_military_image(thisperson, unit_name):
    """generate an image with Dall-E and return the URL for download"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    image_prompt = (
        "Create a professional photo of "
        + thisperson
        + ", who is within a "
        + unit_name
        + " unit of the military to accompany their biography on the website"
    )
    photo = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="256x256",
    )

    return photo

def generate_military_vehicles_image():
    """generate an image with Dall-E and return the URL for download"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    image_prompt = (
        "Create a professional photo of a military vehicle"
    )
    photo = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="256x256",
    )
    if os.path.exists("imagecache/") is False:
        os.mkdir("imagecache/")
    num = random.randint(1000, 9999)
    urlretrieve(photo["data"][0]["url"], "imagecache/" +\
         "military_vehicle_image_" + str(num) + ".png")

    return photo

# def generate_military_vehicles():
#     """Generate military vehicle images and return a list of their URLs."""
#     vehicle_images = []

#     for i in range(2):
#         vehicle_image = generate_military_vehicles_image()
#         vehicle_images.append(vehicle_image)

#     return vehicle_images
