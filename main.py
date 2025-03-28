import pygame

import buttons
import helpers
from classes.ImagePost import ImagePost
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Button import Button


def main():
    pygame.init()

    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    posts = [ImagePost("noa_kirel","tel aviv", "this is an ImagePost", "Images\noa_kirel.jpg"),
             ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if helpers.mouse_in_button(buttons.like_button, pygame.mouse.get_pos()):
                    pass
                if helpers.mouse_in_button(buttons.comment_button, pygame.mouse.get_pos()):
                    pass
                if helpers.mouse_in_button(buttons.click_post_button, pygame.mouse.get_pos()):
                    pass
                pass
                if helpers.mouse_in_button(buttons.view_more_comments_button, pygame.mouse.get_pos()):
                    pass

        screen.fill(BLACK)
        screen.blit(background, (0, 0))





        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    quit()


main()
