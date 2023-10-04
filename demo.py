from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact
import sys
from visa.logger import logging
from visa.exception import CustomException
from visa.pipeline.pipeline import Pipeline


if __name__ == "__main__":
    logging.info("Starting training pipeline")
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        raise CustomException(e, sys) from e



