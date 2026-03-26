from fastapi import Header, HTTPException, Depends
from app.core.config import settings
from app.core.security import verify_access_token

def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
def get_current_user(token: str = Header(...)):
    user = verify_access_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user