from fastapi import APIRouter, Depends
from ..controllers.auth_controller import AuthController
from ..middleware.auth_middleware import require_admin
from ..schemas.auth import TokenData

router = APIRouter(prefix="/admin", tags=["Admin"])
auth_controller = AuthController()


@router.get("/test", summary="Admin only endpoint")
async def admin_test(current_user: TokenData = Depends(require_admin)):
    """
    Example endpoint that requires admin access.

    Requires valid JWT token with admin role.
    """
    return auth_controller.admin_only(current_user.username)
