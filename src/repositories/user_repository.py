from typing import Optional, List
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.auth import RegisterRequest


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: dict) -> User:
        """Create a new user"""
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find_by_username(self, username: str) -> Optional[User]:
        """Find user by username"""
        return (
            self.db.query(User)
            .filter(User.username == username, User.deleted_at.is_(None))
            .first()
        )

    def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email"""
        return (
            self.db.query(User)
            .filter(User.email == email, User.deleted_at.is_(None))
            .first()
        )

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Find user by ID"""
        return (
            self.db.query(User)
            .filter(User.id == user_id, User.deleted_at.is_(None))
            .first()
        )

    def update(self, user_id: int, user_data: dict) -> Optional[User]:
        """Update user"""
        user = self.find_by_id(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> bool:
        """Soft delete user"""
        user = self.find_by_id(user_id)
        if user:
            from datetime import datetime

            user.deleted_at = datetime.utcnow()
            self.db.commit()
            return True
        return False

    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users"""
        return (
            self.db.query(User)
            .filter(User.deleted_at.is_(None))
            .offset(skip)
            .limit(limit)
            .all()
        )
