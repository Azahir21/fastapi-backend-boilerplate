from typing import Optional
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..repositories.user_repository import UserRepository
from ..services.auth_service import AuthService
from ..controllers.auth_controller import AuthController


class Container:
    """Dependency injection container"""

    _instance: Optional["Container"] = None

    def __init__(self):
        self._auth_controller: Optional[AuthController] = None

    @classmethod
    def get_instance(cls) -> "Container":
        """Get singleton instance"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def auth_controller(self) -> AuthController:
        """Get auth controller instance"""
        if self._auth_controller is None:
            self._auth_controller = AuthController()
        return self._auth_controller

    def get_user_repository(self, db: Session) -> UserRepository:
        """Get user repository instance"""
        return UserRepository(db)

    def get_auth_service(self, db: Session) -> AuthService:
        """Get auth service instance"""
        return AuthService(db)


# Global container instance
container = Container.get_instance()
