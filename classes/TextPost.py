import helpers
from classes.Post import Post
from helpers import *






class TextPost(Post):
    def __init__(self,username,location,description,likes_counter,comments,text,text_color,background_color):
        super().__init__(username,location,description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display_content(self):
        screen.blit(self.background_color,(POST_X_POS,POST_Y_POS))
        screen.blit(self.text,(LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS))
        super().display_content()
