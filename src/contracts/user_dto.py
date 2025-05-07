from dataclasses  import dataclass
from typing import  Dict, Any

@dataclass
class UserDTO:
    """
    Data Transfer Object for User
    """

    # id: Optional[int] = None
    username: str = ""
    email: str = ""
    password: str = ""

def to_dict(self) -> Dict[str, Any]:
    return {
        "username": self.username,
        "email": self.email,
        "password": self.password,
    }
