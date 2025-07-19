from typing import Optional
from sqlalchemy.orm import Session
from ..repositories.user_repository import UserRepository
from ..schemas.auth import LoginRequest, RegisterRequest, AuthResponse, UserResponse
from ..utils.auth import hash_password, verify_password, create_access_token
from ..utils.logger import logger
from fastapi import HTTPException


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def register(self, request: RegisterRequest) -> AuthResponse:
        """Register a new user"""
        # Check if user already exists
        if self.user_repository.find_by_username(request.username):
            raise HTTPException(status_code=400, detail="Username already exists")

        if self.user_repository.find_by_email(request.email):
            raise HTTPException(status_code=400, detail="Email already exists")

        # Hash password
        hashed_password = hash_password(request.password)

        # Create user
        user_data = {
            "username": request.username,
            "email": request.email,
            "password": hashed_password,
            "role": "user",
        }

        user = self.user_repository.create(user_data)
        logger.info(f"User registered: {user.username}")

        # Generate token
        token = create_access_token(
            data={"user_id": user.id, "username": user.username, "role": user.role}
        )

        return AuthResponse(token=token, user=UserResponse.model_validate(user))

    def login(self, request: LoginRequest) -> AuthResponse:
        """Login user"""
        # Find user
        user = self.user_repository.find_by_username(request.username)
        if not user or not verify_password(request.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not user.is_active:
            raise HTTPException(status_code=401, detail="Account is deactivated")

        logger.info(f"User logged in: {user.username}")

        # Generate token
        token = create_access_token(
            data={"user_id": user.id, "username": user.username, "role": user.role}
        )

        return AuthResponse(token=token, user=UserResponse.model_validate(user))

    def get_profile(self, user_id: int) -> UserResponse:
        """Get user profile"""
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return UserResponse.model_validate(user)
