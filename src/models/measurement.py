from . import db

class Measurement(db.Model):
    """
    Measurement model to store information about user measurements.
    """
    __tablename__ = "measurements"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)  # Date of the measurement
    measurement_type = db.Column(db.String(50), nullable=False)  # Type of measurement (e.g., weight, body fat percentage, etc.)
    value = db.Column(db.Float, nullable=False)  # Measurement value (e.g., weight, body fat percentage, etc.)
    notes = db.Column(db.String(255), nullable=True)  # Additional notes or comments about the measurement (optional)