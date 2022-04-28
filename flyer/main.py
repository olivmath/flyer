from flyer.api.teacher import (
    add,
    update,
    delete
)
from flyer import app

app.include_router(add.router)
app.include_router(delete.router)
app.include_router(update.router)
