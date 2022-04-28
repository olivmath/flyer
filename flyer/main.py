from flyer.api.home import hello
from flyer import app

app.include_router(hello.router)
