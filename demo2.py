from flask import Flask 
import os,sys
from visa.exception import customException
from visa.logger import logging

app = Flask(__name__)

logging.info("Creating route for flask app")
@app.route('/', methods = ['GET', 'POST'])
def index():
    try:
        raise Exception("Testing exception module")
    except Exception as e:
        visa = customException(e, sys)
        logging.info(visa.error_message)
        logging.info("Testing Exception module")
        

if __name__ == "__main__":
    app.run(debug=True)
    