#here we are createing functions for data processing



from curses import raw
from housing.entity.config_entity  import DataIngestionConfig
from housing.exception import HousingException
import sys,os
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile #fro extarsct compressed file
from six.moves import urllib #for download tgz file
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit



class DataIngestion:


    def __init__(self,data_ingestion_config:DataIngestionConfig) :
        try:
            logging.info(f'{"="*20}Data Ingestion log started.{"="*20}')
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys)

    def download_housing_data (self,) -> str  :

        try:
            #extracting remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_downloadz_dir

            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir , exist_ok=True)

            housing_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)
            logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")

            #to download file
            urllib.request.urlretrive(download_url,tgz_file_path)
            logging.info(f"Downloading of file into :[{tgz_file_path}] has completed ")

            return tgz_file_path

        except Exception  as e:
            raise HousingException(e,sys) from e

    def extrec_tgz_file (self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir # here data get extracted

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir, exist_ok=True)

            logging.info(f"extraxting tgz file : [{tgz_file_path}] into dir [{raw_data_dir}]")

            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)

            logging.info(f"extraction completed")    





        except Exception as e:
            raise HousingException (e,sys) from e


    def split_data_as_train_test(self,)-> DataIngestionArtifact:
        try:

            raw_data_dir = self.data_ingestion_config.raw_data_dir

            #below listdir function will go into given file path and retuns list of files avalible by slicing we get the individual file name 
            file_name = os.listdir(raw_data_dir)[0]
            #here we are getting exact file path 
            housing_file_path = os.path.join(raw_data_dir,file_name)
            #by using panadas we are reading extracted file
            logging.info(f"reading csv file : [{housing_file_path}]")
            housing_data_frame = pd.read_csv(housing_file_path)

            housing_data_frame["income_cat"]= pd.cut(
                housing_data_frame["median_income"],
                bins=[ 0.0, 1.5, 3.0, 4.5, 6.0, np.inf]
                labels=[1,2,3,4,5]
            )

            logging.info(f"spliting data into train test split")

            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1 , test_size=0.2, random_state=42)

            for train_index, test_index in split.split(housing_data_frame , housing_data_frame["income_cat"]):
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"], axis=1)
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"], axis = 1)


            train_file_path =  os.path.join(self.data_ingestion_config.ingeted_train_dir,file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingeted_train_dir,exist_ok=True)
                logging.info(f"Exporting traning dataset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)

            if strat_test_set is not None :
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True) 
                logging.info(f"Exporting Test dataset to file: [{test_file_path}]") 
                strat_test_set.to_csv(strat_test_set,index=False)  

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
            test_file_path=test_file_path,
            is_ingested=True,
            message=f"data ingestion completed susccessfully"
            
            )

            logging.info(f"data_ingestion_artifact : [{data_ingestion_artifact}]")    

            return data_ingestion_artifact


        except Exception as e :
            raise HousingException(e,sys) from e





        




    def initiate_data_ingestion(self)-> DataIngestionArtifact :
        try:

            tgz_file_path = self.download_housing_data()

            self.extrec_tgz_file(tgz_file_path=tgz_file_path)

            return self.split_data_as_train_test()
            
        except Exception as e:
            raise HousingException (e,sys) from e   

    


    def __del__(self):
        logging.info(f"{'='*20}Data Ingstion log complted.{'='*20} \n\n")
