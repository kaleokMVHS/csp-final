import pygame
from gridhelper import GridHelper

class SnakeSquare:
    def __init__(self, snake_game, pos = (0, 0), next=None):
        self.screen = snake_game.screen
        self.gridhelper = GridHelper()
        self.screen_rect = snake_game.screen.get_rect()
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.pos = pos
        self.rect.topleft = (self.gridhelper.pos_to_coord(pos))
        self.next = next

    def update(self, decay=False):
        if ((next == None) and decay):
            return
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)
        if (next):
            next.update(decay)

    def pos(self):
        return(self.pos)