from fastapi.testclient import TestClient
from flyer.main import app
from fastapi import Response
from fastapi import status
from pytest import fixture, mark


@fixture
def hello() -> Response:
    client = TestClient(app)
    return client.get("/teacher/consult/123")


def test_add_teacher(hello: Response):
    assert hello.json() == {"prof": 123}
    assert hello.status_code == status.HTTP_201_CREATED
