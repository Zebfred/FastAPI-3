from fastapi import APIRouter, Body
from database.models import UserSchema, UserLoginSchema
# from scripts.auth_bearer import JWTBearer
from scripts.auth_handler import signJWT

router = APIRouter()

users = []

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

import random

def generate_mock_activity_data(user_count: int):
    activities = ['search', 'view', 'purchase']
    mock_data = []
    for _ in range(user_count):
        user_activity = {
            "email": f"user{_}@example.com",
            "activity": random.choice(activities)
        }
        mock_data.append(user_activity)
    return mock_data

@router.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@router.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }


