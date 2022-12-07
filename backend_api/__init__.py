from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:srbija@localhost/cook'
db = SQLAlchemy(app)


with app.context():
    db.create_all()

from backend_api import routes
from backend_api.models import Recipe
