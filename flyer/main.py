from flyer.api.teacher import (
    add,
    update,
    delete,
    consult
)
from flyer import app

app.include_router(consult.router)
app.include_router(delete.router)
app.include_router(update.router)
app.include_router(add.router)
