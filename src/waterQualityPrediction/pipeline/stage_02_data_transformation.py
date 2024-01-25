from waterQualityPrediction.config import ConfigurationManager
from waterQualityPrediction.components import DataTransformation
from waterQualityPrediction import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.preprocess_data()
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e