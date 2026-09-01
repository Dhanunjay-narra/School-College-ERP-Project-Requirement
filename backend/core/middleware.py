"""
Custom Enterprise Middlewares: Security, Logging, Tenant Context, and Error Handling.
"""
import time
import logging
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from backend.core.exceptions import ERPBaseException

logger = logging.getLogger("erp.middleware")

class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        tenant_id = request.headers.get("X-Tenant-ID", "default_institution")
        
        request.state.request_id = request_id
        request.state.tenant_id = tenant_id
        
        start_time = time.time()
        logger.info(f"Incoming request: {request.method} {request.url.path} (Tenant: {tenant_id}, ReqID: {request_id})")
        
        try:
            response = await call_next(request)
            process_time = (time.time() - start_time) * 1000
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time-Ms"] = f"{process_time:.2f}"
            
            # Security Headers
            response.headers["X-Content-Type-Options"] = "nosniff"
            response.headers["X-Frame-Options"] = "DENY"
            response.headers["X-XSS-Protection"] = "1; mode=block"
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
            
            logger.info(f"Completed {request.method} {request.url.path} in {process_time:.2f}ms with status {response.status_code}")
            return response
        except ERPBaseException as ex:
            process_time = (time.time() - start_time) * 1000
            logger.warning(f"ERP Exception ({ex.status_code}): {ex.message}")
            return JSONResponse(
                status_code=ex.status_code,
                content={
                    "error": True,
                    "message": ex.message,
                    "details": ex.details,
                    "request_id": request_id
                }
            )
        except Exception as ex:
            process_time = (time.time() - start_time) * 1000
            logger.error(f"Unhandled Exception: {str(ex)}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "error": True,
                    "message": "Internal server error. Our engineering team has been notified.",
                    "request_id": request_id
                }
            )
