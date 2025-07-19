from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..config.database import get_db
from ..controllers.auth_controller import AuthController
from ..middleware.auth_middleware import get_current_user
from ..schemas.auth import LoginRequest, RegisterRequest, TokenData

router = APIRouter(prefix="/auth", tags=["Authentication"])
auth_controller = AuthController()


@router.post("/register", summary="Register a new user")
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new user account.

    - **username**: Username (3-50 characters)
    - **email**: Valid email address
    - **password**: Password (minimum 6 characters)
    """
    return auth_controller.register(request, db)


@router.post("/login", summary="User login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate user and return JWT token.

    - **username**: Username
    - **password**: Password
    """
    return auth_controller.login(request, db)


@router.get("/profile", summary="Get user profile")
async def get_profile(
    current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)
):
    """
    Get current user's profile information.

    Requires valid JWT token in Authorization header.
    """
    return auth_controller.get_profile(current_user.user_id, db)
