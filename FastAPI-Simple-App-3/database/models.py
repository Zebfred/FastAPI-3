from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    country: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Jimmy Zeb",
                "email": "Jimmy@xyz.com",
                "password": "jimmy",
                "country": "Mexico"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "Jimmy@xyz.com",
                "password": "jimmy"
            }
        }