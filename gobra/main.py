import sys

import pygame

from gobra.board import Board
from gobra.constants import Constant as c
from gobra.stone import Stone


def main():
    # Initialise basic game famework
    pygame.init()
    screen = pygame.display.set_mode(c.SCR_DIMS)
    clock = pygame.time.Clock()
    dt = 0
    running = True
    black_to_play = True

    # Make board (9x9)
    board = Board(size=9)
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
            board_x = (lmouse_x - c.BOARD_OFFSET_X) // c.GRID_SPACING
            board_y = (lmouse_y - c.BOARD_OFFSET_Y) // c.GRID_SPACING
            if 0 <= board_x < board.size and 0 <= board_y < board.size:
                if black_to_play:
                    success = board.place_stone(board_x, board_y, color=Stone.BLACK)
                    if success:
                        black_to_play = False
                else:
                    success = board.place_stone(board_x, board_y, color=Stone.WHITE)
                    if success:
                        black_to_play = True

        # Update display
        screen.fill(pygame.Color("#928374"))
        screen.blit(board.surface, dest=(280, 152))
        pygame.display.flip()

        # Limit fps and update dt
        dt = clock.tick(60) / 1000

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
