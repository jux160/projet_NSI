from flask_sqlalchemy import SQLAlchemy

from .views.py import app

db = SQLAlchemy(app)

class Content(db.model):
    id= db.Column(db.Integer, primary_key=True)
    description= db.Column(db.String(200), nullable=False)
    gender =  db.Column(db.Integer(), nullable=False)
    
    def __init__(self, description, gender):
        self.description = description
        self.gender = gender
        
db.vreate_all()