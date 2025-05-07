from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_models():
    from .user import User
    from .workout import Workout
    from .user_profile import UserProfile
    from .user_workout import UserWorkout
    from .user_achievement import UserAchievement
    from .achievement import Achievement
    from .workout_exercise import WorkoutExercise
    from .exercise import Exercise
    from .nutrition import Nutrition
    from .measurement import Measurement
    from .goal import Goal