import sys

import pygame


def main():
    # Initialise useful constants
    c = constants = {
        "SCR_WIDTH": 1280,
        "SCR_HEIGHT": 1024,
        "SCR_DIMS": (1280, 1024),
        "FPS": 60,
        "BOARD_OFFSET_X": 280,
        "BOARD_OFFSET_Y": 152,
        "GRID_SPACING": 80,
        "GRID_OFFSET": 40,
    }

    # Initialise basic game famework
    pygame.init()
    screen = pygame.display.set_mode(c["SCR_DIMS"])
    clock = pygame.time.Clock()
    dt = 0
    running = True
    black_to_play = True

    # Make board (9x9)
    board = pygame.Surface((720, 720))
    board.fill("brown")

    # Create lines spaced 80 px apart
    points = [i for i in range(39, 720, c["GRID_SPACING"])]
    line_length = points[-1] - points[0]
    h_lines = [pygame.Rect(points[0], y, line_length, 3) for y in points]
    v_lines = [pygame.Rect(x, points[0], 3, line_length) for x in points]
    # And star points
    star_points = [
        (points[2] + 1, points[2] + 1),
        (points[2] + 1, points[-3] + 1),
        (points[-3] + 1, points[2] + 1),
        (points[-3] + 1, points[-3] + 1),
        (points[4] + 1, points[4] + 1),
    ]

    # Draw lines and star points on board
    for line in h_lines:
        _ = pygame.draw.rect(board, "black", line)
    for line in v_lines:
        _ = pygame.draw.rect(board, "black", line)
    for point in star_points:
        pygame.draw.circle(board, "black", point, 6)

    # Primary game loop
    while running:
        clicked = False  # Flag for logic loop to check click happened
        # Input event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    lmouse_x, lmouse_y = event.pos
                    clicked = True

        # Update game logic
        if clicked:
            board_x = (lmouse_x - c["BOARD_OFFSET_X"]) // c["GRID_SPACING"]
            board_y = (lmouse_y - c["BOARD_OFFSET_Y"]) // c["GRID_SPACING"]
            if 0 <= board_x < 9 and 0 <= board_y < 9:
                point = (points[board_x] + 1, points[board_y] + 1)
                if black_to_play:
                    pygame.draw.circle(board, "black", point, 35)
                    black_to_play = False
                else:
                    pygame.draw.circle(board, "white", point, 35)
                    black_to_play = True

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
