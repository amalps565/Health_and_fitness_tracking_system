"""Application settings and configuration."""
import os
from urllib.parse import quote_plus


class Settings:
    def __init__(self):
        # Database Configuration
        self.postgres_url: str = os.environ.get("POSTGRES_URL", "localhost:5432/health_and_fitness_tracking")
        self.postgres_user: str = os.environ.get("POSTGRES_USER", "grclocal")
        self.postgres_password: str = os.environ.get("POSTGRES_PASSWORD", "12345")

        # Application Configuration
        self.environment: str = os.environ.get("FLASK_ENV", "development")
        self.is_test: bool = os.environ.get("TESTING", "false").lower() == "true"
        self.debug: bool = self.environment == "development"

        self.jwt_secret_key: str = os.environ.get("JWT_SECRET_KEY", "jwt_secret_key")

    @property
    def database_uri(self) -> str:
        # Quote special characters in password
        escaped_password = quote_plus(self.postgres_password)
        return f"postgresql://{self.postgres_user}:{escaped_password}@{self.postgres_url}"

    @property
    def flask_sqlalchemy_config(self) -> dict:
        return {
            "SQLALCHEMY_DATABASE_URI": self.database_uri,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }

    def validate(self) -> None:
        required_settings = {
            "POSTGRES_URL": self.postgres_url,
            "POSTGRES_USER": self.postgres_user,
            "POSTGRES_PASSWORD": self.postgres_password,
            "JWT_SECRET_KEY": self.jwt_secret_key,
        }

        missing = [key for key, value in required_settings.items() if not value]
        if missing:
            raise ValueError(f"Missing required settings: {', '.join(missing)}")


# Global settings instance
settings = Settings()
