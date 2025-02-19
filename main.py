from src.textsummarizer.logging import logger

from src.textsummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTraininingPipeline
from src.textsummarizer.pipeline.stage_2_data_transformtion_pipeline import DataTransformationTrainingPipeline
from src.textsummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textsummarizer.pipeline.stage_4_model_eval_pipeline import ModelEvaluationTrainingPipeline


STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f"{STAGE_NAME} started")
    pipeline = DataIngestionTraininingPipeline()
    pipeline.run()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed", exc_info=True)
    raise e


STAGE_NAME = 'Data transformation stage'

try:
    logger.info(f"{STAGE_NAME} started")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed", exc_info=True)
    raise e

STAGE_NAME = 'Model Training stage'

try:
    logger.info(f"{STAGE_NAME} started")
    pipeline = ModelEvaluationTrainingPipeline()
    pipeline.initiate_model_trainer()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed", exc_info=True)
    raise e

STAGE_NAME = 'Model Evaluation stage'

try:
    logger.info(f"{STAGE_NAME} started")
    pipeline = ModelEvaluationTrainingPipeline()
    pipeline.initiate_model_eval()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed", exc_info=True)
    raise e