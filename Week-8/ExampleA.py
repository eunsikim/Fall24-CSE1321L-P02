import pygame, sys
from pygame.locals import *


def main():
    pygame.init()

    resolution = (500, 500)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    # Main loop
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        screen.fill(color=(255, 255, 255))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
