class Blog:
    def __init__(self, username, password, secret):
        self.title = username # Act as id
        self.description = password
        self.comments = []

    def append_comment(self, comment):
        self.comments.append(comment)