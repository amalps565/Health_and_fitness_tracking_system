from . import db

class Exercise(db.Model):
    """
    Exercise model to store information about exercises.
    """
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'cardio', 'strength', 'flexibility'
    difficulty_level = db.Column(db.String(50), nullable=False)  # e.g., 'easy', 'medium', 'hard'
    muscle_groups = db.Column(db.String(100), nullable=False)  # e.g., 'upper body', 'lower body', 'core'
    demonstration_video_url = db.Column(db.String(255), nullable=True)  # URL to a video demonstrating the exercise