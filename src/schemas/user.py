from marshmallow import Schema, fields, ValidationError
import re

class UserSchema(Schema):
    username = fields.Str(required=True, error_messages={"required": "Username is mandatory"})

    email = fields.Str(
        required=True,
        validate=lambda e: re.match(r'^[^@]+@[^@]+\.[^@]+$', e),
        error_messages={"required": "Email is mandatory", "validator_failed": "Invalid email format"}
    )

    password = fields.Str(
        required=True,
        validate=lambda p: (
            8 <= len(p) <= 32 and re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', p)
        ),
        error_messages={
            "required": "Password is mandatory",
            "validator_failed": "Password must be 8–32 chars, with at least one letter and one number"
        }
    )

    height = fields.Float(
        required=True,
        validate=lambda h: h > 0,
        error_messages={"required": "Height is mandatory", "validator_failed": "Height must be positive"}
    )

    weight = fields.Float(
        required=True,
        validate=lambda w: w > 0,
        error_messages={"required": "Weight is mandatory", "validator_failed": "Weight must be positive"}
    )
    fitness_level = fields.Str(
        required=True,
        validate=lambda fl: fl in ["beginner", "intermediate", "advanced"],
        error_messages={"required": "Fitness level is mandatory", "validator_failed": "Invalid fitness level"}
    )
    goals=fields.Str(
        required=True,
        validate=lambda g: g in ["weight loss", "muscle gain", "maintenance"],
        error_messages={"required": "Goals are mandatory", "validator_failed": "Invalid goals"}
    )

    age = fields.Int(
        required=True,
        validate=lambda a: a >= 16,
        error_messages={"required": "Age is mandatory", "validator_failed": "Minimum age is 16 years"}
    )

    health_conditions = fields.Str(allow_none=True)  # Optional field