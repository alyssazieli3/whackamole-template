import pygame
import random

#set constants
height = 512
width = 640

def set_screen(screen):
    screen.fill("light green")
    # draw horizontal lines
    for i in range(1, 16):
        pygame.draw.line(
            screen,
            "purple",
            (0, i * width / 20),
            (width, i * width / 20))
    # draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            "purple",
            (i * width / 20, 0),
            (i * width / 20, height)
        )


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        set_screen(screen)

        #set mole
        screen.blit(mole_image, mole_image.get_rect(topleft = (0, 0)))
        mole_pos = [0, 0]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x = x // 32
                    y = y // 32
                    if [x, y] == mole_pos:
                        new_x = random.randrange(0, 20)
                        new_y = random.randrange(0, 16)
                        set_screen(screen)
                        screen.blit(mole_image, mole_image.get_rect(topleft = (new_x*32, new_y*32)))
                        mole_pos = [new_x, new_y]

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
