import os
from datetime import datetime
from visa.logger import logging
from visa.exception import CustomException

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()
ROOT_DIR = os.getcwd() #to get current working directory
CONFIG_DIR = 'config'
CONFIG_FILE_NAME = 'config.yaml'

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

#Data Ingestion related Variable
DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'
DATA_INGESTION_DOWNLOAD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_INGESTED_DIR_KEY = 'ingested_dir'
DATA_INGESTION_TRAIN_DIR_KEY = 'ingested_train_dir'
DATA_INGESTION_TEST_DIR_KEY = 'ingested_test_dir'

#Data Validation related_variable
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_SCHEMA_DIR_KEY = 'schema_yaml'

#Company variable
COLUMN_COMPANY_AGE = 'company_age'
COLUMN_YEAR_ESTB = 'yr_of_estab'
COLUMN_ID = 'case_id'
COLUMN_CASE_STATUS = 'case_status'


#Training pipeline releated pipeline
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline"

