from . import db

class WorkoutExercise(db.Model):
    """
    WorkoutExercise model to store information about exercises in a workout.
    """
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer, nullable=False)  # Number of sets
    reps = db.Column(db.Integer, nullable=False)  # Number of repetitions per set
    duration_seconds = db.Column(db.Integer, nullable=True)  # Duration in seconds for timed exercises (optional)
    rest_time_seconds = db.Column(db.Integer, nullable=True)  # Rest time in seconds between sets (optional)
    order = db.Column(db.Integer, nullable=False)  # Order of the exercise in the workout