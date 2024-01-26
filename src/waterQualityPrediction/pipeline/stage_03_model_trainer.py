from waterQualityPrediction.config import ConfigurationManager
from waterQualityPrediction.components import ModelTrainer
from waterQualityPrediction import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config, params=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
