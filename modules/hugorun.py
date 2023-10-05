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


def zip_web(person_name):
    """Zips up the files in the web content folder"""
    zip_name = person_name.replace(" ","")
    if os.path.exists('generated_pages') == False:
        os.mkdir('generated_pages')
    shutil.make_archive("generated_pages/"+zip_name, format='zip', root_dir='public')
    return "ok"