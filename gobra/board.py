import pygame

from gobra.constants import Constant as c
from gobra.stone import Stone


class Board:
    def __init__(self, size=9):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = Stone.BLACK

        # Make board (9x9)
        self.surface = pygame.Surface((720, 720))
        self.surface.fill(pygame.Color("#d65d0e"))

        # Create lines spaced 80 px apart
        self._points = [i for i in range(39, 720, c.GRID_SPACING)]
        line_length = self._points[-1] - self._points[0]
        h_lines = [
            pygame.Rect(self._points[0], y, line_length, 3) for y in self._points
        ]
        v_lines = [
            pygame.Rect(x, self._points[0], 3, line_length) for x in self._points
        ]
        # And star points
        star_points = [
            (self._points[2] + 1, self._points[2] + 1),
            (self._points[2] + 1, self._points[-3] + 1),
            (self._points[-3] + 1, self._points[2] + 1),
            (self._points[-3] + 1, self._points[-3] + 1),
            (self._points[4] + 1, self._points[4] + 1),
        ]

        # Draw lines and star points on board
        for line in h_lines:
            _ = pygame.draw.rect(self.surface, pygame.Color("#1d2021"), line)
        for line in v_lines:
            _ = pygame.draw.rect(self.surface, pygame.Color("#1d2021"), line)
        for point in star_points:
            pygame.draw.circle(self.surface, pygame.Color("#1d2021"), point, 6)

    def is_empty(self, x, y):
        return self.grid[y][x] == 0

    def is_legal(self, x, y):
        pass

    def place_stone(self, x, y, color=Stone.BLACK):
        if self.is_empty(x, y):
            self.grid[y][x] = color
            if color == Stone.BLACK:
                pygame.draw.circle(
                    self.surface,
                    pygame.Color("#1d2021"),
                    (self._points[x] + 1, self._points[y] + 1),
                    radius=35,
                )
            else:
                pygame.draw.circle(
                    self.surface,
                    pygame.Color("#fbf1c7"),
                    (self._points[x] + 1, self._points[y] + 1),
                    radius=35,
                )
            return True
        else:
            return False
