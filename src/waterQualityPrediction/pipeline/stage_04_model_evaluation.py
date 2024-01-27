from waterQualityPrediction.config import ConfigurationManager
from waterQualityPrediction.components import ModelEvaluation
from waterQualityPrediction import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.save_results()
        except Exception as e:
            raise e

