import sys

import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

from settings import Settings
from snakesquare import SnakeSquare
from snake import Snake

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")
        self.bg_color = BLACK
        self.snake = Snake(self, (8, 8))
        self.stop_movement()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

            FPS = 1
            clock = pygame.time.Clock()
            clock.tick(FPS)
            

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif (event.type == pygame.K_UP) and not self.moving_down:
                    self.stop_movement()
                    self.moving_up = True
                    print('up')
                elif event.type == pygame.K_DOWN and not self.moving_up:
                    self.stop_movement()
                    self.moving_down = True
                elif event.type == pygame.K_LEFT and not self.moving_right:
                    self.stop_movement()
                    self.moving_left = True
                elif event.type == pygame.K_RIGHT and not self.moving_left:
                    self.stop_movement()
                    self.moving_right = True

    def _game_logic(self):
        if (self.moving_right):
            self.snake.move(right=True)
        elif (self.moving_left):
            self.snake.move(left=True)
        elif (self.moving_down):
            self.snake.move(down=True)
        elif (self.moving_up):
            self.snake.move(up=True)

    def stop_movement(self):
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False

    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        self._game_logic()
        pygame.display.flip()

if __name__ == '__main__':
    snake = SnakeGame()