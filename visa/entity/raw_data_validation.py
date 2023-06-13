import os ,sys
from visa.logger import logging
from visa.exception import CustomException
#from visa.config.configuration import Configuration
import json
from visa.utils.utils import read_yaml_file
import pandas as pd
import collections

class IngestedDataValidation:
    def __init__(self, validation_path, schema_path):
        try:
            self.validate_path = validation_path
            self.schema_path = schema_path
            self.data = read_yaml_file(self.schema_path)
        except Exception as e:
            raise CustomException(e, sys) from e

    def validation_filename(self, file_name) -> bool:
        try:
            print(self.data['FileName'])
            schema_file_name=self.data['FileName']
            if schema_file_name == file_name:
                return True
        except Exception as e:
            raise CustomException(e, sys) from e

    def validation_column_length(self) -> bool:
        try:
            df=pd.read_csv(self.validate_path)
            if (df.shape[1] == self.data['NumberofColumns']):
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys) from e
        
    # check the missing values columns
    def missing_value_columns(self)->bool:
        try:
            df = pd.read_csv(self.validate_path)
            count = 0
            for columns in df:
                if (len([columns]) - df[columns].count()) == len(df[columns]):
                    count+=1
            return True if (count==0) else False

        except Exception as e:
            raise CustomException(e,sys) from e
        
    # replace the null values
    def replace_null_values_with_null(self)->bool:
        try:
            df = pd.read_csv(self.validate_path)
            df.fillna('NULL', inplace=True)
        except Exception as e:
            raise CustomException(e, sys) from e
        
    #Check columns names
    def check_columns_name(self)->bool:
        try:
            df = pd.read_csv(self.validate_path)
            df_columns_name = df.columns
            schema_columns_name = list(self.data['ColumnNames'].keys())

            return True if(collections.Counter(df_columns_name) == collections.Counter(schema_columns_name)) else False
        except Exception as e:
            raise CustomException(e, sys) from e


