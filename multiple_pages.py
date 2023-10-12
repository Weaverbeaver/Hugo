"""code for developing multiple page websites"""
import os
from modules.generators import generate_company_people, generate_bios
from modules.website import Website
from modules.hugorun import insert_index
from apikey import APIKEY

os.environ["OPENAI_API_KEY"] = APIKEY

company_gen = generate_company_people(4,"any")

people = company_gen[2:-1]
people_desc = generate_bios(people, company_gen[0])
for i in enumerate(people_desc):
    people_desc[i[0]][0] = "**" + people_desc[i[0]][0] + "**"
    people_desc[i[0]][1] = people_desc[i[0]][1] + "\n"
TEAMTEXT = '\n\n'.join(str(item) for innerlist in people_desc for item in innerlist)

insert_index(company_gen[0],company_gen[1],"content","_index.md","main")
insert_index("About",company_gen[-1],"content","about.md","sub")
insert_index("The Team",TEAMTEXT,"content","team.md","sub")

this_website = Website()
this_website.read_toml()
this_website.update_title(company_gen[0])
this_website.write_toml()
