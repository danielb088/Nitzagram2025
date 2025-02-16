from classes.Post import Post

import pygame
from helpers import screen



class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments,image):
        super().__init__( username, location, description, likes_counter, comments)
        self.image = pygame.image.load(image)


    def override display_content(self):
        screen.display(self.image)



