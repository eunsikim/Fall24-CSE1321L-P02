import pygame, sys
from pygame.locals import *

# Since your project structure may be different, make sure
# to change the path to the image file
PYTHON_LOGO_PATH = "./Week-9/python-logo.png"


def main():
    # Initialize pygame and set resolution and
    # create a clock ovject to control frame rate
    pygame.init()

    resolution = (500, 500)
    BACKGROUND_COLOR = (100, 200, 200)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    # The image address may be different for you
    python_logo = pygame.image.load(PYTHON_LOGO_PATH).convert_alpha()
    # user .convert() if the image does not have transparency
    # user .convert_alpha() if the image has transparency
    python_logo_rect = python_logo.get_rect()
    python_logo_rect.topleft = (200, 200)

    python_logo = pygame.transform.scale(python_logo, (100, 100))

    # Main loop
    while True:
        # Event listener for user action
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        screen.fill(BACKGROUND_COLOR)

        screen.blit(python_logo, python_logo_rect.topleft)

        # Update screen and set the frame rate
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
