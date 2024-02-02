from app import db
from datetime import datetime


class IcompasUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, email: str, first_name: str, last_name: str, password: str):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return self.email
