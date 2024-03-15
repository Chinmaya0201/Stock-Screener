## Configuation manager working properly

from stockScreener.config.configuration import ConfigurationManager 
import pandas as pd

cm = ConfigurationManager()
fmc = cm.get_stock_list_config()
df = pd.read_csv(fmc.stock_list_file_path)
# print(type(fmc.stock_list_file_path))
# print(df.head())

pg_config = cm.get_page_config()
print(pg_config.initial_sidebar_state, type(pg_config.initial_sidebar_state))
print(pg_config.layout, type(pg_config.layout))
print(pg_config.page_title, type(pg_config.page_title))
