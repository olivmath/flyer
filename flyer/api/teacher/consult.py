from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from flyer.api.teacher import router
from fastapi import Path, status


@router.get(
    path="/consult/{prof_id}",
    description="Insert a new Teacher",
    status_code=status.HTTP_200_OK
)
async def consult_teacher(prof_id: int = Path(
        ...,
        example="123321",
        description="`Id of Teacher`"
        )
    ):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "prof": prof_id
        }
    )
