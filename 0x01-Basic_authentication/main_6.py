#!/usr/bin/env python3
"""Main module for user creation and base64 encoding of credentials."""

import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User


def create_user():
    """Create and save a new user, then print user info."""
    user_email = "bob@hbtn.io"
    user_clear_pwd = "H0lbertonSchool98!"
    user = User()
    user.email = user_email
    user.password = user_clear_pwd
    print(f"New user: {user.id} / {user.display_name()}")
    user.save()

    basic_clear = f"{user_email}:{user_clear_pwd}"
    basic_base64 = base64.b64encode(basic_clear.encode('utf-8')).decode('utf-8')
    print(f"Basic Base64: {basic_base64}")


if __name__ == "__main__":
    create_user()
