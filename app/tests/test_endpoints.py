from fastapi.testclient import TestClient
from main import app
from app.api.models.user import User
from app.db.db import USER_DATA

client = TestClient(app)


def test_register_new_user():
    response = client.post("/auth/register", json={"username": "Test_user", "password": "test_pass"})
    assert response.status_code == 200
    assert User(**{"username": "Test_user", "password": "test_pass"}) in USER_DATA
    assert response.json() == {"message": "Пользователь Test_user успешно зарегистрирован"}


def test_login():
    data = {"username": "Erik", "password": "1245"}
    response = client.post("/auth/login", data=data, headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    return response.json()["access_token"]
