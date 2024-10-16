import pygame, sys
from pygame.locals import *


def main():
    # Initialize pygame and set resolution and
    # create a clock ovject to control frame rate
    pygame.init()

    resolution = (500, 500)
    BACKGROUND_COLOR = (100, 150, 150)
    WHITE = (255, 255, 255)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()

    ms_font = pygame.font.Font(None, 24)
    s_font = pygame.font.Font(None, 48)

    s_text = s_font.render("s: 0 s", True, WHITE)
    s_text_rect = s_text.get_rect()
    s_text_rect.topleft = (25, 25)

    ms_text = ms_font.render("ms: 0 ms", True, WHITE)
    ms_text_rect = ms_text.get_rect()
    ms_text_rect.top = s_text_rect.bottom + 10
    ms_text_rect.left = s_text_rect.left

    # Main loop
    while True:
        # Event listener for user action
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        current_time = pygame.time.get_ticks()
        ms_text = ms_font.render(f"ms: {current_time} ms", True, WHITE)
        s_text = s_font.render(f"s: {current_time // 1000} s", True, WHITE)

        screen.fill(BACKGROUND_COLOR)
        screen.blit(ms_text, ms_text_rect.topleft)
        screen.blit(s_text, s_text_rect.topleft)

        # Update screen and set the frame rate
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
