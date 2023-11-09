# Hugo

## About

This application generates static websites using the ChatGPT API to generate biographies of fictional "C" level members. It runs a local web server that prompts for user input, generating a number of websites contained within discrete zip files.

### Current Features

- Individual generation
  - Generates up to 10 single page websites
  - Biography of a single "C" level employee on each website
  - First name prescribed and future names auto-generated
- Company generation
  - Generates up to 10 multi page company websites
  - Names and biographies of between 3 and 8 people per company
  - Choose to many insert a person into the first company

### Roadmap

- Caching of generated images in a repository to reduce costs. Currently, images are cached locally.
- Migration of codebase and hosting to corporate services. This will include the git repository, the web front end and the image repository.

## Components

The application is written in python3. It is designed to be executed locally with its own built-in local web server. Pipelines run on the repository when pushed to ensure code quality.

### Modules

generators.py - Contains a number of functions used to generate content using OpenAI API.

hugorun.py - Functions to execute the static website generator, Hugo, concatenate people into a paragraph, and create a website class.

scanfile.py - Functions to enumerate Hugo themes, create .md files, and export the generated website as a zip file.

website.py - A class for a website instance. Contains the config for the website and functions to update the config.

### Pipelines

Pipelines are stored as code in .github/workflows

codeql.yml - Runs code vulnerability analysis.

hugo.yml - (Deprecated) Runs hugo application.

pylint.yml - Validates formatting of python code.

python-app.yml - Runs pytest.

### Web Server

web_frontend.py creates a web front end for a user to control the application through a graphical interface. It is roughly equivalent to console output in a command line and is not designed to be used in a production setting.

## External Dependencies

### OpenAI

The application uses the OpenAI API to generate content. This happens over HTTPS and the application will not function without it.

## Installation

1. Clone the repo (including submodues) using:

```
git clone https://github.com/Weaverbeaver/Hugo.git --recurse-submodules
```

2. Install necessary python dependencies with:

```
pip install -r requirements.txt
```

3. Install hugo following the [documentation](https://gohugo.io/installation/windows/)

Run the web frontend using

```
py -m streamlit run web_frontend.py
```
