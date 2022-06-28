

# we have created this file so as to declate all the constant variables here
from datetime import datetime
import os

ROOT_DIR = os.getcwd() # to get current working directory
CONFIG_DIR = "config"
CONFIG_FILE = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE)

CURRENT_TIME_STAMP =  f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"

# traning pipeline related variable
TRANING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRANING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRANING_PIPELINE_NAME_KEY = "pieline_name"