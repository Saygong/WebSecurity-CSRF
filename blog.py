class Blog:
    def __init__(self, id, title, description, comments):
        self.id = id
        self.title = title
        self.description = description
        self.comments = comments

    def append_comment(self, comment):
        self.comments.append(comment)

class BlogRepository:
    def __init__(self, blogs):
        self.blogs = blogs

    def get_by_id(self, id):
        for blog in self.blogs:
            print(blog)
            if(blog.id == id):
                return blog
            
        raise KeyError


blog_repository = BlogRepository(
    [
        Blog("1", "Climate Change", "Climate change is the significant variation of average weather conditions becoming, for example, warmer, wetter, or drier", ["noice", "toit"]),
        Blog("2", "2024 US Election", "The 2024 United States presidential election will be the 60th quadrennial presidential election, set to be held on Tuesday, November 5, 2024.", ["noice", "toit"]),
    ]
)