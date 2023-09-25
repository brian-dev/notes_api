# Demo API automation using PyTest


[![Python API Test Demo](https://github.com/brian-dev/pytest_api/actions/workflows/python-app.yml/badge.svg)](https://github.com/brian-dev/pytest_api/actions/workflows/python-app.yml)

## Project Overview
This demo project is based on a simple notes web app. The application consists of both a UI and an API, with this 
repository focusing specifically on the API side of the application. The Notes API consists of the three major 
functional areas: an endpoint to check overall system health, a collection of User endpoints for managing users and a 
collection of endpoints for managing Notes. The test suite consists of positive and negative cases for each endpoint, 
as well as some cases where boundary and/or edge conditions where applicable. 

## Project Setup
First, clone the[ core-python](https://github.com/brian-dev/core-python) framework. From a terminal execute the 
following commands in the core-python directory:
```
python repo_cli.py  
Select the Python API option  
cd notes_api
pytest
```

### The _python repo_cli.py_ command
This command opens a CLI that presents a list of automation projects that are available to clone in to the core 
automation framework. This repo is labeled Python API, which corresponds to the GitHub repository name of the 
automation project. Selecting this option, the notes_api project repository is cloned as a subdirectory of the 
core python automation framework. 

### The _cd notes_api_ command  
Changes the active working directory to the automation project directory. Once here, the project behaves much like 
any other standalone project using source control. 

### The _pytest_ command  
This executes the entire automation suite and reports results to the terminal.