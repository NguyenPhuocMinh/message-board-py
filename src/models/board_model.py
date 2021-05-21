from pydantic import BaseModel, Field
from typing import Optional
from fastapi import status
from datetime import datetime


class BoardModel(BaseModel):
    registerDate: datetime
    title: str = Field(..., max_length=100)
    name: str = Field(..., max_length=50)
    description: str = Field(..., max_length=1000)
    deleted: Optional[bool] = False
    v : Optional[int] = 0

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": "6097b34899a605daea8cbf42",
                "registerDate": "2020-12-04T17:00:00+00:00",
                "title": "Hoc python",
                "name": "Python",
                "text": "Hello python",
            }
        }


def ResponseCreate(data, message):
    return {
        "data": data,
        "status": status.HTTP_201_CREATED,
        "message": message,
    }


def SuccessGetAllResponse(data, total, message):
    return {
        "result": data,
        "total": total,
        "status": 200,
        "message": message,
    }


def SuccessResponse(data, message):
    return {
        "data": data,
        "status": 200,
        "message": message,
    }


def ErrorResponse(error, code, message):
    return {"error": error, "code": code, "message": message}
