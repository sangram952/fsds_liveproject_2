from collections import namedtuple


# all the configuration required to load the data is strored in 'DataIngestionConfig'
DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_downloadz_dir","raw_data_dir","ingeted_traina_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["chema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                     "trandformed_train_dir",
                                                                   "transformed_test_dir",
                                                                  "preprocessed_object_file_path" ])


ModelTrainerConfig = namedtuple ("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])                                                                 

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evalition_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusheConfig",["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

