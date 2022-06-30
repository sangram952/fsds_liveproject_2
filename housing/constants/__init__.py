

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

# data injgestion related variable
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = ""
DATA_INGESTION_DIR_NAME_KEAY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"