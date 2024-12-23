from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    calories = db.Column(db.Integer, nullable=False)
    exercise = db.Column(db.String(100), nullable=False)
    currentstat = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

def __repr__(self):
    return f"<Workout(type={self.type}, duration={self.duration}, calories={self.calories})>"