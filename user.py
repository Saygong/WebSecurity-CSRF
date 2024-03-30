class User:
    def __init__(self, username, password, secret, email):
        self.username = username
        self.password = password
        self.secret = secret
        self.email = email

    def change_email(self, email):
        self.email = email


class UserRepository:
    def __init__(self, users):
        self.users = users

    def get_by_username(self, username):
        return next(
            (user for user in self.users if user.username == username),
            None,
        )

    def get_user(self, session):
        username = session.get("current_user")
        return self.get_by_username(username)


user_repository = UserRepository(
    [
        User("alice", "123", "15_th15_th3_r34l_l1f3", "alice@mail.com"),
        User("bob", "456", "15_th15_ju57_f4nt45y", "bob@mail.com"),
    ]
)
