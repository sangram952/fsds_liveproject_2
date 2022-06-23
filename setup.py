from ast import Pass
from setuptools import setup
#from typing import list


#declerng variables for setup function
PROJET_NAME="housing_pricepredictor"
VERSION ="0.0.2" 
AUTHOR = "SAM"
DESCRIPTION = "this frist end to end fsds nov21 batch project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements_list():
    """ths function is going to return list of requirement mention in requirements.txt file
    
    return function will give list of libreries mentioined in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name= PROJET_NAME,
version= VERSION,
author= AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requres=get_requirements_list()

)


