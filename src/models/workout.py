from datetime import datetime, timezone
from . import db

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    difficulty_level = db.Column(db.String(50), nullable=False)  # e.g., 'easy', 'medium', 'hard'
    creator = db.Column(db.String(100), nullable=False)  # e.g., 'user', 'admin'
    duration_minutes = db.Column(db.Integer, nullable=False)  # Duration in minutes
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )
    # user = db.relationship("user", back_populates="workouts")

    def __repr__(self):
        return f"<Workout(name='{self.name}', duration={self.duration_minutes} mins, calories={self.calories_burned})>"