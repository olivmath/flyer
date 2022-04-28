from pytest import fixture
from unittest import mock

@fixture(scope="session", autouse=True)
def mock_settings_env_vars():
    import os

    with mock.patch.dict(os.environ, {}): yield
