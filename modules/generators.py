"""module provides functions for taking a title inputand generating text and an image from this"""
import random

def titleinput():
    """input title"""
    newtitle = random.choice(["Weavsite","Stevesite"])
    return newtitle


def gentext():
    """generate text from title"""
    description_text = "Welcome to my site, my favourite food is pasta"
    return description_text



def genimage():
    """gen image"""
    return NotImplemented
