from fastapi.testclient import TestClient
from flyer.main import app
from fastapi import Response
from fastapi import status
from pytest import fixture, mark


@fixture
def hello() -> Response:
    client = TestClient(app)
    return client.get("/")


def test_hello_route(hello: Response):
    assert hello.status_code == status.HTTP_200_OK
    assert hello.json() == {"message": "Hello World!"}
