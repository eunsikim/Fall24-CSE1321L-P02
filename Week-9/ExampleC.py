import pygame, sys
from pygame.locals import *

ORANGE_BUTTON_PATH = "./Week-9/Orange-Button-PNG-Pic.png"
GREEN_BUTTON_PATH = "./Week-9/Green-Button-PNG-Pic.png"
SOUND_1_PATH = "./Week-9/retro-select-236670.mp3"
SOUND_2_PATH = "./Week-9/medium-text-blip-14855.mp3"


def main():
    # Initialize pygame and set resolution and
    # create a clock ovject to control frame rate
    pygame.init()

    resolution = (500, 500)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    # The image address may be different for you
    orange_button_image = pygame.image.load(ORANGE_BUTTON_PATH).convert_alpha()
    orange_button_image = pygame.transform.scale(orange_button_image, (100, 100))
    orange_button_image_rect = orange_button_image.get_rect()
    orange_button_image_rect.topleft = (125, 200)

    green_button_image = pygame.image.load(GREEN_BUTTON_PATH).convert_alpha()
    green_button_image = pygame.transform.scale(green_button_image, (100, 100))
    green_button_rect = green_button_image.get_rect()
    green_button_rect.left = orange_button_image_rect.right + 50
    green_button_rect.centery = orange_button_image_rect.centery

    sound_1 = pygame.mixer.Sound(SOUND_1_PATH)
    sound_2 = pygame.mixer.Sound(SOUND_2_PATH)

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
                if (
                    orange_button_image_rect.collidepoint(event.pos)
                    and not pygame.mixer.get_busy()
                ):
                    sound_1.play()

                if (
                    green_button_rect.collidepoint(event.pos)
                    and not pygame.mixer.get_busy()
                ):
                    sound_2.play()

        screen.fill(color=(255, 255, 255))

        screen.blit(orange_button_image, orange_button_image_rect.topleft)
        screen.blit(green_button_image, green_button_rect.topleft)

        # Update screen and set the frame rate
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
