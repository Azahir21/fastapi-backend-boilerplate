from sqlalchemy.orm import Session
from ..config.database import SessionLocal
from ..config.config import settings
from ..repositories.user_repository import UserRepository
from ..utils.auth import hash_password
from ..utils.logger import logger


def seed_database():
    """Seed the database with initial data"""
    db = SessionLocal()
    try:
        user_repo = UserRepository(db)

        # Create default admin user if not exists
        existing_admin = user_repo.find_by_username(settings.default_admin_username)

        if not existing_admin:
            admin_data = {
                "username": settings.default_admin_username,
                "email": settings.default_admin_email,
                "password": hash_password(settings.default_admin_password),
                "role": "admin",
                "is_active": True,
            }

            user_repo.create(admin_data)
            logger.info(
                f"Default admin user created (username: {settings.default_admin_username}, password: {settings.default_admin_password})"
            )

        logger.info("Database seeding completed successfully")

    except Exception as e:
        logger.error(f"Error seeding database: {str(e)}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
