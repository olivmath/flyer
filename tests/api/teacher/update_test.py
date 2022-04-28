from fastapi.testclient import TestClient
from flyer.main import app
from fastapi import Response
from fastapi import status
from pytest import fixture, mark


@fixture
def hello() -> Response:
    client = TestClient(app)
    return client.post("/teacher/upd", json={
        "name": "Lucas Oliveira",
        "subject": "Matemática"
    })


def test_add_teacher(hello: Response):
    assert hello.json() == {
        "name": "Lucas Oliveira",
        "subject": "Matemática"
    }
    assert hello.status_code == status.HTTP_200_OK
