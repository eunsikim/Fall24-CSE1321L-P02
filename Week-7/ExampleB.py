import pygame, sys
from pygame.locals import *


def main():
    # Initialize pygame and set resolution and
    # create a clock ovject to control frame rate
    pygame.init()

    resolution = (500, 500)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    # Set surface properties
    dimension = (50, 50)
    position = (0, 0)
    color_red = (255, 0, 0)
    s1 = pygame.Surface(dimension)
    s1.fill(color_red)

    # Main loop
    while True:
        # Event listener for user action
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        # "Draw" the background
        screen.fill(color=(0, 0, 0))

        # Add surfaces/rect into the screen here
        screen.blit(s1, position)

        # Update screen and set the frame rate
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
