import pygame, sys
from pygame.locals import *
import random


def main():
    red = 255
    green = 255
    blue = 255
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
            if event.type == KEYDOWN:  # This prints only once per keypress
                if event.key == K_w:
                    print("UP")
            if keys[pygame.K_s]:  # This prints continously
                print("DOWN")

        screen.fill((red, green, blue))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
