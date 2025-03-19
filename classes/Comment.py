from helpers import *

class Comment():
    def __init__(self, text):
        self.text = text

    # def addComments(self):
    #     self.text = read_comment_from_user()

    def displayComment(self, comment_number):


        screen.blit(self.text,(FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS))


