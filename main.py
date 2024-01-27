from waterQualityPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from waterQualityPrediction.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from waterQualityPrediction.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from waterQualityPrediction import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} started<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<< \n\nx======x")
except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} started<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<< \n\nx======x")
except Exception as e:
    logger.info(e)
    raise e 



STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} started<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<< \n\nx======x")
except Exception as e:
    logger.info(e)
    raise e 
    
    