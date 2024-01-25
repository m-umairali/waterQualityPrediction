import os
import scipy
import pandas as pd
from waterQualityPrediction import logger
from sklearn.model_selection import train_test_split
from waterQualityPrediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    def preprocess_data(self):
        data = pd.read_csv(self.config.data_path)
        logger.info("Imputing missing values in the dataset")
        data['ph'] = data.groupby(['Potability'])['ph'].transform('mean')
        data['Sulfate'] = data.groupby(['Potability'])['Sulfate'].transform('mean')
        data['Trihalomethanes'] = data.groupby(['Potability'])['Trihalomethanes'].transform('mean')
        # Removing rows where "ph" is less than or equal to 0
        logger.info("Removing row contain 0")
        data = data[data["ph"] > 0]
        
        # Applying Box-Cox transformation to all columns
        logger.info("Normalizing the data with Box-Cox")
        data["ph"], fitted_lambda = scipy.stats.boxcox(data["ph"])
        data["Hardness"], fitted_lambda = scipy.stats.boxcox(data["Hardness"])
        data["Solids"], fitted_lambda = scipy.stats.boxcox(data["Solids"])
        data["Chloramines"], fitted_lambda = scipy.stats.boxcox(data["Chloramines"])
        data["Sulfate"], fitted_lambda = scipy.stats.boxcox(data["Sulfate"])
        data["Conductivity"], fitted_lambda = scipy.stats.boxcox(data["Conductivity"])
        data["Organic_carbon"], fitted_lambda = scipy.stats.boxcox(data["Organic_carbon"])
        data["Trihalomethanes"], fitted_lambda = scipy.stats.boxcox(data["Trihalomethanes"])
        data["Turbidity"], fitted_lambda = scipy.stats.boxcox(data["Turbidity"])
        
        #saving data after preprocessing
        data.to_csv(os.path.join(self.config.root_dir, "water-quality-processed.csv"), index=False)


    def train_test_spliting(self):
        # data = pd.read_csv(self.config.root_dir)
        data = pd.read_csv(os.path.join(self.config.root_dir, "water-quality-processed.csv"))

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        