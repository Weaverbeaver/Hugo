"""module provides functions for executing hugo and moving generated web files to
   different folders"""
import subprocess


def hugoexecute():
    """execute hugo commandx, creating html+css in public folder"""
    result = subprocess.run(
        ["pwsh.exe", "-Command", "hugo"],
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )
    # output result
    print(result.stdout)
    return result


def insertcontent(title, text):
    """insert content into content/_index.md including the title, description and image"""

    with open("content/_index.md","w", encoding="utf-8") as md_insert:
        md_insert.write("""---
title: " """+title+""" "

description: "Welcome"
# 1. To ensure Netlify triggers a build on our exampleSite instance, we need to change a file in the exampleSite directory.
theme_version: '2.8.2'
---
"""+text)
        return md_insert

def movewebfiles():
    """moves the generator contents to another folder"""
    return NotImplemented
