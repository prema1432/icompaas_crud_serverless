import pytest
from app import db
from app.models.user_models import IcompasUser
from tests.conftest import app, client
import json


@pytest.fixture
def sample_user(app):
    with app.app_context():
        user = IcompasUser(
            email="premanath@prema.com",
            first_name="Talamarla",
            last_name="Premanath",
            password="Welcome@1234",
        )
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
    return user


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_get_user(app, client, sample_user):
    response = client.get(f"/users/{sample_user.id}")
    assert response.status_code == 200
    user_data = json.loads(response.data)
    assert user_data["first_name"] == "Talamarla"
    assert user_data["last_name"] == "Premanath"
    assert user_data["email"] == "premanath@prema.com"


def test_get_invalid_user(app, client, sample_user):
    response = client.get(f"/users/867867678")
    assert response.status_code == 404
    user_data = json.loads(response.data)
    assert user_data["message"] == "User not found"


def test_update_user(app, client, sample_user):
    updated_data = {
        "first_name": "UpdatedFirstName",
        "last_name": "UpdatedLastName",
        "email": "updated_email@example.com",
    }
    response = client.put(f"/users/{sample_user.id}", json=updated_data)
    assert response.status_code == 200
    updated_response = client.get(f"/users/{sample_user.id}")
    updated_user_data = json.loads(updated_response.data)
    assert updated_user_data["first_name"] == "UpdatedFirstName"
    assert updated_user_data["last_name"] == "UpdatedLastName"
    assert updated_user_data["email"] == "updated_email@example.com"


def test_delete_user(app, client, sample_user):
    response = client.delete(f"/users/{sample_user.id}")
    assert response.status_code == 204
    deleted_response = client.get(f"/users/{sample_user.id}")
    assert deleted_response.status_code == 404
    deleted_user_data = json.loads(deleted_response.data)
    assert deleted_user_data["message"] == "User not found"
