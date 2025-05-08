from . import db

class User(db.Model):
    __tablename__="users"

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(120),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    registration_date=db.Column(db.DateTime,nullable=False)
    account_status=db.Column(db.String(20),nullable=True)  # e.g., 'active', 'inactive', 'suspended'

    achievements = db.relationship("Achievement", back_populates="user",secondary="user_achievements")
 