from typing import Any, Optional
from fastapi.responses import JSONResponse


class APIResponse:
    @staticmethod
    def success(message: str, data: Any = None, status_code: int = 200) -> JSONResponse:
        """Create success response"""
        response_data = {
            "status": "success",
            "message": message,
        }
        if data is not None:
            response_data["data"] = data

        return JSONResponse(content=response_data, status_code=status_code)

    @staticmethod
    def error(
        message: str, status_code: int = 400, errors: Optional[dict] = None
    ) -> JSONResponse:
        """Create error response"""
        response_data = {
            "status": "error",
            "message": message,
        }
        if errors:
            response_data["errors"] = errors

        return JSONResponse(content=response_data, status_code=status_code)
