from flask import session


class Unauthorized(Exception):
    """Unauthorized User"""
    pass


class AuthorizationHelper:

    @staticmethod
    def validate_session():
        if "current_user" not in session:
            raise Unauthorized
