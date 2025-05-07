from . import db

class UserWorkout(db.Model):
    """
    UserWorkout model to store information about workouts associated with users.
    """
    __tablename__ = "user_workouts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    date_completed = db.Column(db.DateTime, nullable=False)  # Date when the workout was completed
    performance_rating = db.Column(db.Integer, nullable=True)  # User's rating of the workout performance (1-5 scale, optional)
    notes = db.Column(db.String(255), nullable=True)  # Additional notes or comments about the workout (optional)