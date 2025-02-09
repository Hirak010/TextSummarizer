from src.textsummarizer.constants import *
from src.textsummarizer.utils.common import read_yaml, create_directories
from src.textsummarizer.entity import DataIngesttionConfig

class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion(self):
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngesttionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config