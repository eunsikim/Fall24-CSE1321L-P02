import pygame, sys
from pygame.locals import *

# 1. Add 60 x 60 Box in the middle of the screen
# 2. Add a 30 x 30 Box in the upper left corner of the screen
# 3. The 30 x 30 Box should be able to move freely in the in the window (WASD)
# 4. If the 30 x 30 Box hits the 60 x 60 Box, change the color of the 60 x 60 Box
#    to green and output "Collision Detected" to the console
# 5. The 30 x 30 Box should not be able to move outside the window


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
