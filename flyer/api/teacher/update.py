from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from flyer.api.teacher import router
from fastapi import status


class Teacher(BaseModel):
    name: str = Field(..., example="Lucas Oliveira")
    subject: str = Field(..., example="Matemática")

@router.post(
    path="/upd",
    description="Update a Teacher",
    status_code=status.HTTP_200_OK
)
async def update_teacher(prof: Teacher):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=prof.dict()
    )
