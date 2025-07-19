import sys
import os
from loguru import logger
from ..config.config import settings


def setup_logging():
    """Setup logging configuration"""
    # Add file logger
    if not os.path.exists("logs"):
        os.makedirs("logs")
        with open("logs/app.log", "w") as f:
            f.write("Log file created\n")
        with open("logs/error.log", "w") as f:
            f.write("Error log file created\n")

    # Remove default logger
    logger.remove()

    # Add console logger
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=settings.log_level,
    )

    logger.add(
        "logs/app.log",
        rotation="1 day",
        retention="30 days",
        level=settings.log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    )

    # Add error file logger
    logger.add(
        "logs/error.log",
        rotation="1 day",
        retention="30 days",
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    )

    return logger
