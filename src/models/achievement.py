from . import db

class Achievement(db.Model):
    """
    Achievement model to store information about user achievements.
    """
    __tablename__ = "achievements"

    id = db.Column(db.Integer, primary_key=True)
    achievement_name = db.Column(db.String(80), nullable=False)  # Name of the achievement
    description = db.Column(db.String(255), nullable=True)  # Description of the achievement (optional)
    criteria = db.Column(db.String(255), nullable=False)  # Criteria to unlock the achievement
    badge_image_url = db.Column(db.String(255), nullable=True)  # URL to the badge image (optional)
    
    user = db.relationship("User", back_populates="achievements",secondary="user_achievements")