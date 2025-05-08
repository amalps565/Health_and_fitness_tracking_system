from . import db

class UserAchievement(db.Model):
    """
    UserAchievement model to store information about user achievements.
    """
    __tablename__ = "user_achievements"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    achievement_id = db.Column(db.Integer, db.ForeignKey('achievements.id'), nullable=False)  # Foreign key to Achievement
    date_achieved = db.Column(db.DateTime, nullable=False)  # Date when the achievement was unlocked
