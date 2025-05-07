from . import db

class Goal(db.Model):
    """
    Goal model to store information about user goals.
    """
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    goal_type = db.Column(db.String(50), nullable=False)  # Type of goal (e.g., weight loss, muscle gain, etc.)
    target_value = db.Column(db.Float, nullable=False)  # Target value for the goal (e.g., target weight, target reps, etc.)
    current_value = db.Column(db.Float, nullable=False)  # Current value towards the goal (optional)
    start_date = db.Column(db.DateTime, nullable=False)  # Start date of the goal
    target_date = db.Column(db.DateTime, nullable=False)  # Target date to achieve the goal
    status = db.Column(db.String(20), nullable=False)  # Status of the goal (e.g., 'active', 'completed', 'failed')
    progress = db.Column(db.Float, nullable=True)  # Progress towards the goal (optional)
