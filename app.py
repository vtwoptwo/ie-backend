from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:srbija@localhost/cook'
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.String(500), nullable=False)
    favorite = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name}'
    
    def __init__(self, name, ingredients, instructions, favorite, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.favorite = favorite
        self.rating = rating


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

