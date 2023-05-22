import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'shanicejones567890@gmail.com'
    MAIL_PASSWORD = 'psxpjsmystgvpqqc'
    MAIL_DEFAULT_SENDER = 'shanicejones567890@gmail.com'
    RESUME_FOLDER= os.environ.get('resume_folder')
    JOB_FOLDER= os.environ.get('job_folder')