import os
import urllib.request as request
from pathlib import Path
from waterQualityPrediction.entity import DataIngestionConfig
from waterQualityPrediction import logger
from waterQualityPrediction.utils import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists: {(Path(self.config.local_data_file))}")