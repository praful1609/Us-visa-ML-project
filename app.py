from flask import Flask,request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from visa.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

#Route for prediction page
@app.route('/',methods=['GET', 'POST'])

def predict_datapoint():
 if request.method=='GET':
  return render_template('prediction_result.html')
 else:
  data=CustomData(
   prevailing_wage = request.form.get('prevailing_wage'),
   has_job_experience = request.form.get('has_job_experience'),
   requires_job_training = request.form.get('requires_job_training'),
   full_time_position = request.form.get('full_time_position'),
   education_of_employee = request.form.get('education_of_employee'),
   continent = request.form.get('continent'),
   unit_of_wage = request.form.get('unit_of_wage'),
   region_of_employment = request.form.get('region_of_employment'),
   no_of_employees = request.form.get('no_of_employees'),
   company_age = request.form.get('company_age')
   )
  
  pred_df = data.get_data_as_data_frame()
  print(pred_df)
  print("Before Prediction")

  predict_pipeline = PredictPipeline()
  print("Mid Prediction")
  results = predict_pipeline.predict(pred_df)
  print("After Prediction")

  return render_template("prediction_result.html", result = results[0])
 


if __name__ == "__main__":
 app.run(host="0.0.0.0", debug=True)