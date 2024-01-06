from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_engestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage02_data_validation import DataValidationPipeline
from src.mlProject.pipeline.stage03_data_transformation import DataTransformationPipeline
from src.mlProject.pipeline.stage04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training stage"

try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e