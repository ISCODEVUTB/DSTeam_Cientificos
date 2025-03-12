from src.models import User

def test_user_authentication():
    user = User("testuser", "password123")
    assert user.authenticate("password123") is True
    assert user.authenticate("wrongpassword") is False
