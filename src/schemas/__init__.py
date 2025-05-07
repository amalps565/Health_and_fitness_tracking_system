from flask_marshmallow import Marshmallow

ma= Marshmallow()

def init_schemas() -> None:
    
    from .user import UserSchema