from dataclasses  import dataclass
import datetime
from typing import  Dict, Any, Optional

@dataclass
class UserDTO:
    """
    Data Transfer Object for User
    """

    # id: Optional[int] = None
    username: str
    email: str
    password: str
    height: float
    weight: float
    fitness_level: str
    goals: str
    age: int
    health_conditions: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "height": self.height,
            "weight": self.weight,
            "fitness_level": self.fitness_level,
            "goals": self.goals,
            "age": self.age,
            "health_conditions": self.health_conditions,
        }
@dataclass
class UserResponseDTO:
    """
    Data Transfer Object for User Response
    """
    user_id: int
    username: str
    email: str
    registration_date: datetime
    height: float
    weight: float
    fitness_level: str
    goals: str
    age: int
    health_conditions: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.user_id,
            "username": self.username,
            "email": self.email,
            "registration_date": self.registration_date,
            "height": self.height,
            "weight": self.weight,
            "fitness_level": self.fitness_level,
            "goals": self.goals,
            "age": self.age,
            "health_conditions": self.health_conditions,
        }
