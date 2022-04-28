"""
# Flyer Molude root
"""

from fastapi import FastAPI


DESCRIPTION ="""
## Welcome To Flyer
- ...

[terms of use](https://raw.githubusercontent.com/olivmath/flyer/main/LICENSE)

***by olivmath®***
"""


app = FastAPI(
    docs_url="/",
    openapi_url="/api/v1/openapi.json",
    description=DESCRIPTION,
    title="Pix API",
    version="0.1.0",
    openapi_tags=[]
)
