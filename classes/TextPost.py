from classes.Post import Post


class TextPost(Post):
    def __init__(self,username,location,description,likes_counter,comments,text,text_color,background_color):
        super().__init__(username,location,description,likes_counter,comments)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
