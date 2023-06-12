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

    def head_pos(self):
        return(self.head.pos)
    
    def head_rect(self):
        return(self.head.rect)

    def should_grow(self):
        bool = self.no_decay_ticks > 0
        if bool:
            self.no_decay_ticks -= 1
        return bool
    
    def occupied_squares(self):
        list = []
        node = self.head
        while node:
            list.append(node.pos)
            node = node.next
        return(list)

    def move(self, right=False, left=False, up=False, down=False):
        head_pos = self.head.pos
        old_head = self.head
        if right == True:
            new_pos = self.grid_helper.right_of(head_pos)
        elif left == True:
            new_pos = self.grid_helper.left_of(head_pos)
        elif up == True:
            new_pos = self.grid_helper.up_of(head_pos)
        elif down == True:
            new_pos = self.grid_helper.down_of(head_pos)
        self.head = SnakeSquare(self.snake_game, new_pos, None, old_head)
        old_head.new_parent(self.head)
        self.head.update(self.should_grow())

        
            
            

    