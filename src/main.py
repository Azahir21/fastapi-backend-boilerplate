from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
import uvicorn
import os

from .config.config import settings
from .config.database import init_db
from .database.migrations import migrate
from .database.seed import seed_database
from .routes.auth import router as auth_router
from .routes.admin import router as admin_router
from .middleware.error_handler import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler,
)
from .utils.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    logger.info("Starting FastAPI Backend Boilerplate...")

    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    # Initialize database
    init_db()

    # Run migrations
    migrate()

    # Seed database
    seed_database()

    logger.info(f"Server starting on {settings.server_host}:{settings.server_port}")
    yield

    # Shutdown
    logger.info("Shutting down...")


# Setup logging
logger = setup_logging()

# Create FastAPI app
app = FastAPI(
    title="FastAPI Backend Boilerplate",
    version="1.0.0",
    description="A production-ready FastAPI boilerplate with SQLAlchemy, JWT authentication, and clean architecture",
    lifespan=lifespan,
    docs_url="/swagger" if settings.server_env == "development" else None,
    redoc_url="/redoc" if settings.server_env == "development" else None,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)


# Health check endpoint
@app.get("/ping", tags=["Health"])
async def ping():
    """Health check endpoint"""
    return {"message": "pong", "status": "healthy"}


# Include routers
app.include_router(auth_router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "FastAPI Backend Boilerplate",
        "version": "1.0.0",
        "docs": "/swagger",
        "health": "/ping",
    }


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.server_env == "development",
        log_level=settings.log_level.lower(),
    )
