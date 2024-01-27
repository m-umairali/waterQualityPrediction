from waterQualityPrediction import logger
import pandas as pd
import numpy as np
from pathlib import Path
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from waterQualityPrediction.entity.config_entity import ModelEvaluationConfig
from waterQualityPrediction.utils.common import read_yaml, create_directories, save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def classification_metrics(self, actual, pred):
        accuracy = accuracy_score(actual, pred)
        class_report = classification_report(actual, pred)
        return accuracy, class_report
    
    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.iloc[:, :-1]
        test_y = test_data.iloc[:, -1]   

        
        predicted_qualities = model.predict(test_x)

        (accuracy, class_report) = self.classification_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"accuracy": accuracy, "classification-report": class_report}
        save_json(path=Path(self.config.metric_file_name), data=scores)