from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.config.configuration import Configuration
import os, sys
from visa.logger import logging
from visa.exception import CustomException
from visa.pipeline.pipeline import Pipeline
from flask import Flask

if __name__ == "__main__":
    logging.info("Starting training pipeline")
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.info("Training pipeline completed")
        raise CustomException(e, sys) from e

