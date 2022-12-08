from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()

if os.getenv('ENV') != 'dev':
    print("running in production mode")
    app.config.from_object('config.ProductionConfig')

else:
    print("running in development mode")
    app.config.from_object('config.DevelopmentConfig')
    
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
CORS(app)








