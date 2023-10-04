import sys, os
import pandas as pd
import numpy as np
from visa.logger import logging
from visa.exception import CustomException
from visa.utils.utils import load_object

class PredictPipeline:
 def __init__(self):
  pass

 def predict(self, features):
  try:
   
   preprocessor_path = r"C:\Users\Praful Bhojane\OneDrive\Desktop\ML project template\Us-visa-ML-project\US_VISA\artifact\data_transformation\2023-10-04-18-59-13\preprocessed\preprocessed.pkl"

   model_path = r"C:\Users\Praful Bhojane\OneDrive\Desktop\ML project template\Us-visa-ML-project\saved_models\20231004191100\model.pkl"

   model = load_object(file_path=model_path)

   preprocessor = load_object(file_path=preprocessor_path)
   
   #logging
   data_scaled = preprocessor.transform(features)

   preds = model.predict(data_scaled)

   return preds

  except Exception as e:
   raise CustomException(e,sys)

  


class CustomData:
 """Description: This class will be responsible for maping all the user input with backend data"""
 def __init__(self,
              prevailing_wage: float,
              has_job_experience: str,
              requires_job_training: str,
              full_time_position: str,
              education_of_employee: str,
              continent: str,
              unit_of_wage: str,
              region_of_employment: str,
              no_of_employees: int,
              company_age: int
              ):
  
  self.prevailing_wage= prevailing_wage
  self.has_job_experience= has_job_experience
  self.requires_job_training= requires_job_training
  self.full_time_position= full_time_position
  self.education_of_employee= education_of_employee
  self.continent= continent
  self.unit_of_wage= unit_of_wage
  self.region_of_employment= region_of_employment
  self.no_of_employees= no_of_employees
  self.company_age= company_age
  
  
  
  
 
 def get_data_as_data_frame(self):
  """Description: This function convert data in dict format and return in pandas DataFrame"""
  try:
   custom_data_input_dict = {
    "prevailing_wage": [self.prevailing_wage],
    "has_job_experience": [self.has_job_experience],
    "requires_job_training": [self.requires_job_training],
    "full_time_position": [self.full_time_position],
    "education_of_employee": [self.education_of_employee],
    "continent": [self.continent],
    "unit_of_wage": [self.unit_of_wage],
    "region_of_employment": [self.region_of_employment],
    "no_of_employees": [self.no_of_employees],
    "company_age": [self.company_age]
   }

   df = pd.DataFrame(custom_data_input_dict)
   
   return df
  
  except Exception as e:
   raise CustomException(e,sys)

