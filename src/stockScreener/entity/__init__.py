from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class FileManagerConfig:

    stock_list_file_path : Path

@dataclass(frozen= True)
class PageConfig:

    page_title: str
    layout : str
    initial_sidebar_state : str 