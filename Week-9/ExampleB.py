import pygame, sys
from pygame.locals import *

# Since your project structure may be different, make sure
# to change the path to the image file and sound file
BUTTON_IMAGE_PATH = "./Week-9/Orange-Button-PNG-Pic.png"
SOUND_PATH = "./Week-9/retro-select-236670.mp3"


def main():
    # Initialize pygame and set resolution and
    # create a clock ovject to control frame rate
    pygame.init()

    resolution = (500, 500)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    # The image address may be different for you
    button_image = pygame.image.load(BUTTON_IMAGE_PATH).convert_alpha()
    button_image = pygame.transform.scale(button_image, (100, 100))
    button_image_rect = button_image.get_rect()
    button_image_rect.topleft = (200, 200)

    sound = pygame.mixer.Sound(SOUND_PATH)

    # Main loop
    while True:
        # Event listener for user action
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_image_rect.collidepoint(event.pos):
                    sound.play()

        screen.fill(color=(255, 255, 255))

        screen.blit(button_image, button_image_rect.topleft)

        # Update screen and set the frame rate
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
