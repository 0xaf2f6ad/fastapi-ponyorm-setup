from fastapi import HTTPException

# all custom exception classes are defined here

UNAUTHORIZED_REQUEST = HTTPException(status_code=401, detail="Unauthorized request")
INVALID_REQUEST = HTTPException(status_code=400, detail="Invalid Request")
