import logging
from config.settings import LOG_FILE

#logging.basicConfig(
#    level=logging.INFO,
#    format="%(asctime)s - %(levelname)s - %(message)s",
#    filename=LOG_FILE,
#    filemode="a"
#)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def get_logger(name):
    return logging.getLogger(name)