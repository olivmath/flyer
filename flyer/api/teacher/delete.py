from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from flyer.api.teacher import router
from fastapi import status


class Teacher(BaseModel):
    name: str = Field(..., example="Lucas Oliveira")
    subject: str = Field(..., example="Matemática")

@router.delete(
    path="/del",
    description="Delete a Teacher",
    status_code=status.HTTP_202_ACCEPTED
)
async def delete_teacher(prof: Teacher):
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content=prof.dict()
    )
