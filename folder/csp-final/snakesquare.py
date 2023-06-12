import pygame
from gridhelper import GridHelper
import random

class SnakeSquare:
    def __init__(self, snake_game, pos = (0, 0), parent=None, next=None):
        self.screen = snake_game.screen
        self.gridhelper = GridHelper()
        self.screen_rect = snake_game.screen.get_rect()
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.pos = pos
        self.rect.topleft = (self.gridhelper.pos_to_coord(pos))
        self.next = next
        self.parent = parent

    def forget_child(self):
        self.next = None

    def new_parent(self, parent):
        self.parent = parent

    def rand_green(self):
        return (random.randrange(0, 150), random.randrange(220, 256), random.randrange(0, 100))

    def update(self, grow=True):
        if ((self.next == None) and not grow):
            if (not self.parent == None):
                self.parent.forget_child()
                pass
            return
        pygame.draw.rect(self.screen, self.rand_green(), self.rect)
        if (not (self.next == None)):
            self.next.update(grow)
