"""
Standard Enterprise ERP Domain and Application Exceptions.
"""
from typing import Optional, Dict, Any

class ERPBaseException(Exception):
    """Root ERP exception with status code and error details."""
    def __init__(self, message: str, status_code: int = 400, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

class DomainException(ERPBaseException):
    """Raised when a domain rule or invariant is violated."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=422, details=details)

class EntityNotFoundException(ERPBaseException):
    """Raised when requested entity is not found."""
    def __init__(self, entity_name: str, entity_id: str):
        message = f"{entity_name} with ID '{entity_id}' not found."
        super().__init__(message, status_code=404, details={"entity": entity_name, "id": entity_id})

class UnauthorizedException(ERPBaseException):
    """Raised on authentication failure."""
    def __init__(self, message: str = "Invalid authentication credentials"):
        super().__init__(message, status_code=401)

class ForbiddenException(ERPBaseException):
    """Raised on authorization failure or missing permissions."""
    def __init__(self, message: str = "Operation not permitted"):
        super().__init__(message, status_code=403)

class ConflictException(ERPBaseException):
    """Raised on duplicate unique constraints."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=409, details=details)

class ValidationException(ERPBaseException):
    """Raised on invalid user input."""
    def __init__(self, message: str, errors: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=400, details=errors)

class ConcurrencyException(ERPBaseException):
    """Raised on optimistic locking conflict."""
    def __init__(self, message: str = "Entity was modified by another transaction. Please refresh."):
        super().__init__(message, status_code=409)
