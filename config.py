from dotenv import load_dotenv
import os
load_dotenv()

class Config(object):
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.environ.get('DB_USER'),
        dbpass=os.environ.get('DB_PASS'),
        dbhost=os.environ.get('DB_HOST'),
        dbname=os.environ.get('DB_NAME')
    )

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.environ.get('DB_USER'),
        dbpass=os.environ.get('DB_PASS'),
        dbhost=os.environ.get('DB_HOST') + ".postgres.database.azure.com",
        dbname=os.environ.get('DB_NAME')
    )