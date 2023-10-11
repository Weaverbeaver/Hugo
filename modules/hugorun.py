"""module provides functions for executing hugo and moving generated web files to
   different folders"""
import subprocess
import shutil
import os


def hugo_execute():
    """execute hugo commandx, creating html+css in public folder"""
    result = subprocess.run(
        "hugo",
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )
    # output result
    print(result.stdout)
    return result


def insert_index(name,text,title,index_path):
    """insert content into content/_index.md including the title, description and image"""
    if not os.path.exists(index_path):
        os.mkdir(index_path)
    with open(index_path+"/_index.md","w", encoding="utf-8") as md_insert:
        md_insert.write("""---
title: " """+name+""" "

description: " """+title+""" "

theme_version: '2.8.2'
---
{{< figure src=\"bio.png\" >}}
"""+text)
        return md_insert


def zip_web(location,name,root):
    """Zips up the files in the web content folder"""
    name_formatted = (name.replace(" ","")).replace(".","")
    if os.path.exists(location) is False:
        os.mkdir(location)
    zipped = shutil.make_archive(location+"/"+name_formatted, format='zip', root_dir=root)
    return zipped
