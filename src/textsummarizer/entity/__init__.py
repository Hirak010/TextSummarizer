from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngesttionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path