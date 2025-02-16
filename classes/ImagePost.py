from classes.Post import Post
from constants import *

import helpers
import pygame
from helpers import screen



class ImagePost(Post):

    def __init__(self, username, location, description, likes_counter, comments,image):
        super().__init__( username, location, description, likes_counter, comments)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, POST_WIDTH, POST_HEIGHT)

    def display_content(self):
        pass

    def display_image(self):
        screen.display(self.image)