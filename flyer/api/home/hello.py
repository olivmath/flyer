from fastapi.responses import JSONResponse
from flyer.api.home import router
from fastapi import status

@router.get(
    path="/",
    description="Hello World!",
    status_code=status.HTTP_200_OK
)
async def hello():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Hello World!"
        }
    )
