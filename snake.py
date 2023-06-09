import pygame
from gridhelper import GridHelper
from snakesquare import SnakeSquare

class Snake:
    def __init__(self, snake_game, head_pos):
        self.grid_helper = GridHelper()
        self.head = SnakeSquare(snake_game, head_pos)
        self.no_decay_ticks = 3
        self.snake_game = snake_game

    def grow(self):
        self.no_decay_ticks += 1

    def should_decay(self):
        return (self.no_decay_ticks > 0)

    def move(self, right: False, left: False, up: False, down: False):
        head_pos = self.head.pos()
        old_head = self.head
        if right == True:
            new_pos = self.grid_helper.right_of(head_pos)
        elif left == True:
            new_pos = self.grid_helper.left_of(head_pos)
        elif up == True:
            new_pos = self.grid_helper.up_of(head_pos)
        elif down == True:
            new_pos = self.grid_helper.down_of(head_pos)
        self.head = SnakeSquare(self.snake_game, new_pos, old_head)
        self.head.update(self.should_decay())
        
            
            

    