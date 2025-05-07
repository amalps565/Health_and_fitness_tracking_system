from dataclasses import dataclass
from typing import Dict

@dataclass
class WorkoutDTO:
    """
    Data Transfer Object for Workout
    """
    name: str = ""
    description: str = ""
    duration: int = 0  # in minutes
    calories_burned: int = 0

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "calories_burned": self.calories_burned,
        }
