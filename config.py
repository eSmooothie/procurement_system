from dotenv import load_dotenv
import logging
from datetime import datetime 
import os

load_dotenv()

# LOGGING-0[p988]
LOG_DIR = 'logs/'
LOG_FILE_NAME = "{}.log".format(datetime.now().strftime("%m_%d_%Y"))
logging.basicConfig(
    filename=LOG_DIR+LOG_FILE_NAME,
    format='[%(asctime)s] -> %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
    )

# DJANGO VARIABLES
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") if os.getenv("DJANGO_SECRET_KEY") else None
DJANGO_DEBUG = os.getenv("DJANGO_DEBUG") if os.getenv("DJANGO_DEBUG") else None

# DATABASE
DB_ENGINE = os.getenv("DB_ENGINE") if os.getenv("DB_ENGINE") else None
DB_NAME = os.getenv("DB_NAME") if os.getenv("DB_NAME") else None
DB_USER = os.getenv("DB_USER") if os.getenv("DB_USER") else None
DB_PASS = os.getenv("DB_PASS") if os.getenv("DB_PASS") else None
DB_HOST = os.getenv("DB_HOST") if os.getenv("DB_HOST") else None
DB_PORT = os.getenv("DB_PORT") if os.getenv("DB_PORT") else None