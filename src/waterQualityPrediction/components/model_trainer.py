import pandas as pd
import os
from waterQualityPrediction import logger
import joblib
from sklearn.ensemble import RandomForestClassifier
from waterQualityPrediction.entity.config_entity import ModelTrainingConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig, params: ModelTrainingConfig):
        self.config = config
        self.params = params
   
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
                    
        train_x = train_data.iloc[:, :-1]
        train_y = train_data.iloc[:, -1]
        test_x = test_data.iloc[:, :-1]
        test_y = test_data.iloc[:, -1]   

        random_forest = RandomForestClassifier(max_depth=self.params.max_depth,
                                               n_estimators=self.params.n_estimators, 
                                               n_jobs=self.params.n_jobs)
        random_forest.fit(train_x, train_y)

        joblib.dump(random_forest, os.path.join(self.config.root_dir, self.config.model_name))