class Blog:
    def __init__(self, id, username, password, secret):
        self.id = id
        self.title = username # Act as id
        self.description = password
        self.comments = []

    def append_comment(self, comment):
        self.comments.append(comment)

class BlogRepository:
    def __init__(self, blogs):
        self.blogs = blogs

    def get_by_id(self, id):
        return next(
            (blog for blog in self.blogs if blog.id == id),
            None,
        )


blog_repository = BlogRepository(
    [
        Blog(1, "Climate Change", "Climate change is the significant variation of average weather conditions becoming, for example, warmer, wetter, or drier", ["noice", "toit"]),
        Blog(1, "2024 US Election", "The 2024 United States presidential election will be the 60th quadrennial presidential election, set to be held on Tuesday, November 5, 2024.", ["noice", "toit"]),
    ]
)