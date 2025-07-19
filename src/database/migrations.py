from sqlalchemy import text
from ..config.database import engine
from ..models.user import User
from ..models.base import Base
from ..utils.logger import logger


def create_tables():
    """Create all database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating tables: {str(e)}")
        raise


def drop_tables():
    """Drop all database tables"""
    try:
        Base.metadata.drop_all(bind=engine)
        logger.info("Database tables dropped successfully")
    except Exception as e:
        logger.error(f"Error dropping tables: {str(e)}")
        raise


def migrate():
    """Run database migrations"""
    try:
        # Create tables
        create_tables()

        # Run any additional migrations here
        with engine.connect() as conn:
            # Example: Add indexes
            conn.execute(
                text(
                    "CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);"
                )
            )
            conn.execute(
                text("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);")
            )
            conn.commit()

        logger.info("Database migration completed successfully")
    except Exception as e:
        logger.error(f"Migration error: {str(e)}")
        raise


if __name__ == "__main__":
    migrate()
