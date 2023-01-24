import pytest
from pydantic import ValidationError

from pypi_python_template.function import UserCreate, UserManagement, UserUpdate


def test_create_user() -> None:
    user_management = UserManagement()
    user_data = {
        "email": "test@example.com",
        "password": "testpassword",
        "name": "Test User",
        "age": 20,
    }
    user = user_management.create_user(UserCreate(**user_data))
    assert user.email == "test@example.com"
    assert user.password == "testpassword"
    assert user.name == "Test User"
    assert user.age == 20
    assert user.is_admin is False
    with pytest.raises(ValidationError):
        user_data = {
            "email": "test",
            "password": "testpassword",
            "name": "Test User",
            "age": 20,
        }
        user_management.create_user(UserCreate(**user_data))
    with pytest.raises(ValueError):
        user_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "name": "Test User",
            "age": 20,
        }
        user_management.create_user(UserCreate(**user_data))


def test_update_user() -> None:
    user_management = UserManagement()
    user_data = {
        "email": "test@example.com",
        "password": "testpassword",
        "name": "Test User",
        "age": 20,
    }
    user_management.create_user(UserCreate(**user_data))
    user_data = {
        "email": "test@example.com",
        "name": "Updated User",
        "age": 30,
        "is_admin": True,
    }
    user = user_management.update_user("test@example.com", UserUpdate(**user_data))
    assert user.email == "test@example.com"
    assert user.name == "Updated User"
    assert user.age == 30
    assert user.is_admin is True
    with pytest.raises(ValueError):
        user_management.update_user("invalid@example.com", UserUpdate(**user_data))


def test_delete_user() -> None:
    user_management = UserManagement()
    user_data = {
        "email": "test@example.com",
        "password": "testpassword",
        "name": "Test User",
        "age": 20,
    }
    user_management.create_user(UserCreate(**user_data))
    assert "test@example.com" in user_management.users
    user_management.delete_user("test@example.com")
    assert "test@example.com" not in user_management.users
    with pytest.raises(ValueError):
        user_management.delete_user("invalid@example.com")
