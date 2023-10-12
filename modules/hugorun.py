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


def insert_index(title,body,description,path,filename,type):
    """insert content into content/_index.md including the title, description and image"""
    if not os.path.exists(path):
        os.makedirs(path)
    ins = ""
    if type == "sub":
        ins = "type: page \nmenu: main"
    with open(path + "/" + filename,"w", encoding="utf-8") as md_insert:
        md_insert.write("""---
title: " """+title+""" "
description: " """+description+""" "
theme_version: '2.8.2'
"""+ins+"""
---
"""+body)
        return md_insert

#{{< figure src=\"bio.png\" >}}

def zip_web(location,name,root):
    """Zips up the files in the web content folder"""
    name_formatted = (name.replace(" ","")).replace(".","")
    if os.path.exists(location) is False:
        os.mkdir(location)
    zipped = shutil.make_archive(location+"/"+name_formatted, format='zip', root_dir=root)
    return zipped
