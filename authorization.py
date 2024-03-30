import random
import string

from flask import session, request

CSRF_TOKENS = []


class Unauthorized(Exception):
    """Unauthorized User"""
    pass


class MissingCSRFToken(Exception):
    """Missing CSRF"""
    pass


class AuthorizationHelper:

    @staticmethod
    def validate(with_token):
        if "current_user" not in session:
            raise Unauthorized

        csrf_token = request.form["csrf"]
        if with_token and csrf_token not in CSRF_TOKENS:
            raise MissingCSRFToken
        CSRF_TOKENS.remove(csrf_token)

    @staticmethod
    def generate_token():
        csrf_token = ''.join(random.choices(string.ascii_letters, k=30))
        CSRF_TOKENS.append(csrf_token)
        return csrf_token
