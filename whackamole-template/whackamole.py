import pygame
import math

#set constants
height = 512
width = 640


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            #draw horizontal lines
            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    "black",
                    (0, i * width / 20),
                    (width, i * width / 20))
            #draw vertical lines
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    "black",
                     (i* width/20, 0),
                     (i*width/20, height)
                )

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
