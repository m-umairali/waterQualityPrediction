from waterQualityPrediction.pipeline.stage_02_data_ingestion import DataIngestionTrainingPipeline
from waterQualityPrediction import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<< \n\nx======x")
except Exception as e:
    logger.info(e)
    raise e
    
    