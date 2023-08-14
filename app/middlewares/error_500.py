from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from fastapi.responses import JSONResponse

class ErrorHandlerMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            if response.status_code == 500:
                error_response = {
                    "error": "Internal server error",
                    "detail": "An error occurred while processing your request.",
                }
                return JSONResponse(content=error_response, status_code=500)
            return response
        except Exception as e:
            error_response = {
                "error": "Internal server error",
                "detail": "An error occurred while processing your request.",
            }
            return JSONResponse(content=error_response, status_code=500)
