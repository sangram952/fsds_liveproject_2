
""" from ast import Return
import logging

#from fsds_liveproject_2.housing.util.util import read_yaml_file
from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, \
ModelTrainerConfig, ModelTrainerConfig, ModelEvalutionConfig, ModelPusherConfig, TraningPipelineConfig
from housing.util.util import * """

from bdb import effective
from cmath import e
from tkinter import E
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig, ModelTrainerConfig,ModelPusherConfig, ModelEvaluationConfig, TrainingPipelineConfig


from housing.util.util import *
from housing.logger import logging
import sys,os
from housing.constant import *
from housing.exception import HousingException

import os
import sys




ROOT_DIR




class Configuration:

	def __init__(self, config_file_path = CONFIG_FILE_PATH ,current_time_stamp = CURRENT_TIME_STAMP) -> None:
		try:
			self.config_info = read_yaml_file(file_path = config_file_path)
			self.traning_pipeline_config= self.get_traning_pipeline_config()
			self.time_stamp = current_time_stamp 
			
		except HousingException as e:
			raise HousingException(e,sys) from e 	
				
			

	


	def get_data_ingestion_config(self) -> DataIngestionConfig:
		try:

			artifact_dir = self.traning_pipeline_config.artifact_dir

			data_ingestion_artifact_dir = os.path.join(artifact_dir , DATA_INGESTION_ARTIFACT_DIR, self.time_stamp)
			data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]

			dataset_download_url= data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]

			tgz_downloadz_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]  )




			raw_data_dir= os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])


			ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY] )



			ingested_test_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_DIR_NAME_KEAY] )


			ingeted_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])


			data_ingestion_config = DataIngestionConfig(
			dataset_download_url=dataset_download_url,
			tgz_downloadz_dir=tgz_downloadz_dir,
			raw_data_dir=raw_data_dir,
			ingested_test_dir=ingested_test_dir,
			ingeted_train_dir=ingeted_train_dir,

			)

		except Exception as e :
			pass



	def get_data_validation_config(self) -> DataValidationConfig:
		pass


	def get_data_transformation_config(self)-> DataTransformationConfig:
		pass

	def get_model_trainer_config(self)-> ModelTrainerConfig:
		pass


	def get_model_evalution_config(self)->ModelEvaluationConfig:
		pass

	def get_model_pusher_config(self)-> ModelPusherConfig:
		pass


	def get_traning_pipeline_config(self)-> TrainingPipelineConfig :
		
		try:
			Traning_Pipeline_Config  =self.config_info[TRANING_PIPELINE_CONFIG_KEY],
			artifact_dir = os.path.join(ROOT_DIR,Traning_Pipeline_Config[TRANING_PIPELINE_NAME_KEY],
			Traning_Pipeline_Config[TRANING_PIPELINE_ARTIFACT_DIR_KEY]  )

			Traning_Pipeline_Config = TrainingPipelineConfig (artifact_dir=artifact_dir)
			logging.info(f"traning pipeline config : {Traning_Pipeline_Config}")
			return Traning_Pipeline_Config
		
		except Exception as e :

			raise HousingException(e,sys) from e




