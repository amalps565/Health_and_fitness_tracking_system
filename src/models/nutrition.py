from .  import db
from datetime import datetime, timezone

class Nutrition(db.Model):
    """
    Nutrition model to store information about nutrition plans associated with users.
    """
    __tablename__ = "nutrition_plans"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)  # Type of meal (e.g., breakfast, lunch, dinner, snack)
    food_items = db.Column(db.String(255), nullable=False)  # List of food items in the meal (comma-separated)
    calories = db.Column(db.Float, nullable=False)  # Total calories in the meal
    macronutrients = db.Column(db.String(100), nullable=False)  # Macronutrient breakdown (e.g., 'protein:30g, carbs:50g, fats:20g')
    micronutrients = db.Column(db.String(100), nullable=True)  # Micronutrient breakdown (e.g., 'vitamin C:50mg, calcium:200mg')
    date_created = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )  # Date when the nutrition plan was created