from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..services.auth_service import AuthService
from ..schemas.auth import LoginRequest, RegisterRequest, AuthResponse, UserResponse
from ..utils.response import APIResponse
from ..utils.logger import logger


class AuthController:
    def __init__(self):
        pass

    def register(self, request: RegisterRequest, db: Session = Depends(get_db)):
        """Register a new user"""
        try:
            auth_service = AuthService(db)
            result = auth_service.register(request)
            return APIResponse.success(
                "User registered successfully", result.model_dump(mode="json"), 201
            )
        except HTTPException as e:
            logger.error(f"Registration failed: {e.detail}")
            return APIResponse.error(e.detail, e.status_code)
        except Exception as e:
            logger.error(f"Registration error: {str(e)}")
            return APIResponse.error("Internal server error", 500)

    def login(self, request: LoginRequest, db: Session = Depends(get_db)):
        """Login user"""
        try:
            auth_service = AuthService(db)
            result = auth_service.login(request)
            return APIResponse.success(
                "Login successful", result.model_dump(mode="json")
            )
        except HTTPException as e:
            logger.error(f"Login failed: {e.detail}")
            return APIResponse.error(e.detail, e.status_code)
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return APIResponse.error("Internal server error", 500)

    def get_profile(self, user_id: int, db: Session = Depends(get_db)):
        """Get user profile"""
        try:
            auth_service = AuthService(db)
            result = auth_service.get_profile(user_id)
            return APIResponse.success(
                "Profile retrieved successfully", result.model_dump(mode="json")
            )
        except HTTPException as e:
            logger.error(f"Get profile failed: {e.detail}")
            return APIResponse.error(e.detail, e.status_code)
        except Exception as e:
            logger.error(f"Get profile error: {str(e)}")
            return APIResponse.error("Internal server error", 500)

    def admin_only(self, username: str):
        """Admin only endpoint"""
        return APIResponse.success(
            "Admin access granted",
            {"message": "This is an admin-only endpoint", "user": username},
        )
