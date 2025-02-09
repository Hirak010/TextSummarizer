from src.textsummarizer.logging import logger

from src.textsummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTraininingPipeline


STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f"{STAGE_NAME} started")
    pipeline = DataIngestionTraininingPipeline()
    pipeline.run()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed", exc_info=True)
    raise e