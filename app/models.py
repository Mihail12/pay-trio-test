from app import db
from datetime import datetime

class Transaction(db.Model):
    pay_id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3))
    amount = db.Column(db.String(10))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(100))
  
        
