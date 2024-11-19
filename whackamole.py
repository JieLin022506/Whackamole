import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        mole_pos = (16,16)
        def draw_grid():
            for i in range(1, 16):
                pygame.draw.line(
                screen,
                    (0,0,0),
       (0, i * 32),
       (640, i * 32),
                1
                )
            for i in range(1, 20):
                pygame.draw.line(
                screen,
                    (0,0,0),
       (i * 32, 0),
       (i * 32, 512),
                1
                )
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    mole_rect = mole_image.get_rect(center=mole_pos)
                    if mole_rect.collidepoint((x,y)):
                        mole_pos = (random.randrange(16, 640, 32), (random.randrange(16, 512, 32))
                                    )

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(center=mole_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
