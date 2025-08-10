import sys

import pygame


def main():
    c = constants = {
        "SCR_WIDTH": 1280,
        "SCR_HEIGHT": 1024,
        "SCR_DIMS": (1280, 1024),
        "FPS": 60,
    }

    pygame.init()
    screen = pygame.display.set_mode(c["SCR_DIMS"])
    clock = pygame.time.Clock()
    dt = 0
    running = True

    board = pygame.Surface((720, 720))
    board.fill("brown")

    points = [i for i in range(40, 720, 80)]
    line_length = points[-1] - points[0]
    h_lines = [pygame.Rect(points[0], y, line_length, 1) for y in points]
    v_lines = [pygame.Rect(x, points[0], 1, line_length) for x in points]

    for line in h_lines:
        _ = pygame.draw.rect(board, "black", line)
    for line in v_lines:
        _ = pygame.draw.rect(board, "black", line)

    while running:
        # Input event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game logic

        # Update display
        screen.fill("purple")
        screen.blit(board, dest=(280, 152))
        pygame.display.flip()

        # Limit fps and update dt
        dt = clock.tick(60) / 1000

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
