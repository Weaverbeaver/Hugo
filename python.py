import subprocess, sys

#change theme
result = subprocess.run(["pwsh.exe", "-Command", "echo \"`ntheme = 'blowfish'\" >> hugo.toml"], shell=True, capture_output=True, text=True)

#generate html
result = subprocess.run(["pwsh.exe", "-Command", "hugo"], shell=True, capture_output=True, text=True)

print(result.stdout)