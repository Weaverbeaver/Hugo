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


def movewebfiles():
    """moves the generator contents to another folder"""
    return NotImplemented


def zip_web():
    """Zips up the files in the web content folder"""
    return NotImplemented
