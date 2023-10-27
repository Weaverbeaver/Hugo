"""module provides functions to open/edit files necessary for hugo"""
import os
import shutil


def get_themes():
    """function to open themes folder and get list of themes"""
    allthemes = os.listdir("themes/")
    print(allthemes)
    return allthemes


def insert_index(title,body,path,filename,pagetype):
    """insert content into content/_index.md including the title, description and image"""
    if not os.path.exists(path):
        os.makedirs(path)
    ins = ""
    if pagetype == "sub":
        ins = "type: page \nmenu: main"
    with open(path + "/" + filename,"w", encoding="utf-8") as md_insert:
        md_insert.write("""---
title: " """+title+""" "
description: "  "
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
