from stockScreener.constants import LOCAL_FILE_PATH, PAGE_CONFIG_PATH
from stockScreener.utils.common import read_yaml
from stockScreener.entity import FileManagerConfig, PageConfig
from stockScreener.logging import logger


class ConfigurationManager:

    def __init__(self, 
                 local_file_path= LOCAL_FILE_PATH,
                 page_config_path= PAGE_CONFIG_PATH):

        self.stock_list_config = read_yaml(local_file_path)
        self.page_config = read_yaml(page_config_path)

    
    def get_stock_list_config(self) -> FileManagerConfig:

        file_manager_config = FileManagerConfig(
            stock_list_file_path= self.stock_list_config.stock_list_path
        )

        return file_manager_config
    
    def get_page_config(self) -> PageConfig:
        
        page_config = PageConfig(
            page_title= self.page_config.page_title,
            layout= self.page_config.layout,
            initial_sidebar_state= self.page_config.initial_sidebar_state
        )

        return page_config
    

if __name__ == "__main__":

    cm = ConfigurationManager()
    fmc = cm.get_stock_list_config()
    print(fmc.stock_list_file_path)
    logger.info('Completed comfiguation manager')

