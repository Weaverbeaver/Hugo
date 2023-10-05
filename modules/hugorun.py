"""module provides functions for executing hugo and moving generated web files to
   different folders"""
import subprocess
import shutil
import os


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


def insert_content(name,text,title):
    """insert content into content/_index.md including the title, description and image"""

    with open("content/_index.md","w", encoding="utf-8") as md_insert:
        md_insert.write("""---
title: " """+name+""" "

description: " """+title+""" "
# 1. To ensure Netlify triggers a build on our exampleSite instance, we need to change a file in the exampleSite directory.
theme_version: '2.8.2'
---
"""+text)
        return md_insert


def zip_web(person_name):
    """Zips up the files in the web content folder"""
    zip_name = (person_name.replace(" ","")).replace(".","")
    if os.path.exists('generated_pages') == False:
        os.mkdir('generated_pages')
    shutil.make_archive("generated_pages/"+zip_name, format='zip', root_dir='public')
    return "ok"