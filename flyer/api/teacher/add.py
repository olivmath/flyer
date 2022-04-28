from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from flyer.api.teacher import router
from fastapi import status


class Teacher(BaseModel):
    name: str = Field(..., example="Lucas Oliveira")
    subject: str = Field(..., example="Matemática")

@router.post(
    path="/add",
    description="Insert a new Teacher",
    status_code=status.HTTP_201_CREATED
)
async def add_teacher(prof: Teacher):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=prof.dict()
    )
