import os
import sys
from visa.constant import *
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import *

class Configuration:
    def __init__(self,
                 config_file_path : str = CONFIG_FILE_PATH,
                 current_time_stamp : str = CURRENT_TIME_STAMP) -> None:
        try:
            self.config_info = (file_path = config_file_path)
            self.time_stamp = current_time_stamp
            self.training_pipeline_config = self.get_training_pipeline_config()

        except Exception as e:
            raise CustomException(e, sys)
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass
          