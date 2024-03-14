import os
import sys
import logging
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H')}.log" # -> name of the log file in the format which would be inside the logs folder
logs_path = os.path.join(os.getcwd(),'LOGS', os.path.splitext(LOG_FILE)[0]) # Creating the complete path which includes current working directory+name of the folder "LOGS"+ name of the file we created above
os.makedirs(logs_path, exist_ok= True) # Creating those directory

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[%(asctime)s] file name = %(pathname)s in line number %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # format to have time, filename, line number and error message  
    level= logging.INFO
)

logger = logging.getLogger('stockScreenerLogger')

if __name__ == "__main__":

    logging.info('Logging has started')