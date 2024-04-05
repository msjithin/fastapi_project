from main import app
from models import Token, User2
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from user_authentication import authenticate_user, ACCESS_TOKEN_EXPORE_MINUTES, create_access_token, get_current_active_user
from database import fake_db
from datetime import timedelta

@app.post("/token", response_model=Token)
async def login_for_access_toekn(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"www-authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPORE_MINUTES)
    access_token = create_access_token(data={"sub": user.username},
                                        expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User2)
async def read_users_me(current_user: User2 = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items")
async def read_own_items(current_user: User2 = Depends(get_current_active_user)):
    return [{"item_id": 1, "owner": current_user}]

