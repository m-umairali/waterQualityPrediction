from waterQualityPrediction.constants import *
from waterQualityPrediction.utils import read_yaml, create_directories
from pathlib import Path
import os
from waterQualityPrediction.entity import (DataIngestionConfig,
                                           DataTransformationConfig,
                                           ModelTrainingConfig,
                                           ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:   
        config = self.config.data_ingestion 

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:   
        config = self.config.data_preprocess 

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainingConfig:
        config = self.config.model_trainer
        params = self.params.RandomForest

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            max_depth = params.max_depth,
            n_estimators = params.n_estimators,
            n_jobs = params.n_jobs
            
        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForest

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
        )

        return model_evaluation_config