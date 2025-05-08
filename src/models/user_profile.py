from . import db

class UserProfile(db.Model):
    """
    UserProfile model to store additional information about users.
    """
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    height_cm = db.Column(db.Float, nullable=False)
    weight_kg = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    fitness_level = db.Column(db.String(50), nullable=False)  # e.g., 'beginner', 'intermediate', 'advanced'
    goals = db.Column(db.String(100), nullable=False)  # e.g., 'weight loss', 'muscle gain', 'maintenance'
    health_conditions = db.Column(db.String(200), nullable=True)  # e.g., 'diabetes', 'hypertension'

    