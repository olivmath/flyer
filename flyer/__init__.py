from fastapi import FastAPI


description ="""
## Welcome To Flyer
- ...

[terms of use](https://github.com/olivmath/flyer)

***by olivmath®***
"""


app = FastAPI(
    docs_url="/docs",
    openapi_url="/api/v1/openapi.json",
    description=description,
    title="Pix API",
    version="0.1.0",
    openapi_tags=[]
)
