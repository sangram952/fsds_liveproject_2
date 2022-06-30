

# here in util file we will be saving all the helping functions like reading file , making pickle file ect.     

import yaml
from housing.exception import HousingException
import os,sys
from housing.constant import *

print(os.getcwd())
os.chdir("c:\\Users\\Dell\\Desktop\\fsds_liveproject\\fsds_liveproject_2\\fsds_liveproject_2")


def read_yaml_file(file_path:str) -> dict:
    
    """this will be used to read yamal file in form of dict """
    try:
        print(os.getcwd())
        os.chdir("c:\\Users\\Dell\\Desktop\\fsds_liveproject\\fsds_liveproject_2\\fsds_liveproject_2")

        with open (file_path, "rb") as yaml_file :
            return yaml.safe_load(yaml_file)
    except Exception as e :
        raise HousingException(e,sys) from e  





