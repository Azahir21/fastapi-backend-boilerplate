from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "123456"
    db_name: str = "headcount_checker"
    db_ssl_mode: str = "disable"

    # JWT
    jwt_secret: str = "your-secret-key-change-this-in-production"
    jwt_expiry_hours: int = 72
    jwt_algorithm: str = "HS256"

    # Server
    server_port: int = 8080
    server_host: str = "0.0.0.0"
    server_env: str = "development"

    # Default Admin
    default_admin_username: str = "admin"
    default_admin_email: str = "admin@example.com"
    default_admin_password: str = "admin123"

    # Logging
    log_level: str = "INFO"

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
