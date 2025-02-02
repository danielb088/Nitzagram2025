import pygame

from constants import *
from helpers import screen

class Post:
    def __init__(self, username, location, description, counter_likes, comments):
        self.username = username
        self.location = location
        self.description = description
        self.counter_likes = counter_likes
        self.comments = comments

    def display(self):
        #display_surface.blit(text, textRect)
        self.display_content()
        self.display_title()
        self.display_buttons()
        self.display_comments()

    def display_content(self):
        pass

    def display_title(self):
        pass

    def display_buttons(self):
        pass

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.counter_likes += 1