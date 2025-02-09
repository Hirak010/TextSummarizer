from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_ingestion import DataIngestion
from src.textsummarizer.logging import logger


class DataIngestionTraininingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.data_ingestion_config = self.config.get_data_ingestion()
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)

    def run(self):
        logger.info("Data ingestion pipeline started")
        self.data_ingestion.download_file()
        self.data_ingestion.extract_zip_file()
        logger.info("Data ingestion pipeline completed")
