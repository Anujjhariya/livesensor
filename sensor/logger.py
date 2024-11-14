# allows you to log messages at various levels, 
# helping you track issues without using print statements.
# sets up a logging system that allows us to write messages to a file (or the console). 
# Each message can have a severity level, like INFO, ERROR, or DEBUG, 
# which helps us categorize the information.

import logging,os,sys
from datetime import datetime



#this will make date and time as log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# here we store the log path and it will tell us the working directory
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

#this will make directory if not exist already
os.makedirs(logs_path,exist_ok=True)

#this is the complete path with the name we created 
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


# Basic configuration function which contains 5 level:
# Debug>>Info>>Warning>>Error>>Critical


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)