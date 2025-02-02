from classes.Post import Post


class PhotoPost(Post):
    def __init__(self, username, location, description, likes_counter, comments,image)
        super().__init__( username, location, description, likes_counter, comments)
        self.image = image
