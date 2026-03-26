from fastapi import APIRouter
from google import auth
from pydantic import BaseModel
from app.core.security import create_access_token

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str


@router.post('/login')
def login(auth_input: AuthInput):
    if (auth.username == 'admin') and (auth.password == 'admin'):
        token = create_access_token(data={"sub": auth_input.username})
        return {"access_token": token, "token_type": "bearer"}
    return {'error': 'Invalid credentials'}