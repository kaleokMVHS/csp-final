import sys
import random
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

from settings import Settings
from snakesquare import SnakeSquare
from snake import Snake
from gridhelper import GridHelper

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")
        self.bg_color = BLACK
        self.snake = Snake(self, (8, 8))
        self.all_positions = [(x, y) for x in range(0, 9) for y in range(0, 9)]
        self.berry_rect = None
        self.place_berry()
        self.stop_movement()
        self.game_rect = pygame.Rect((200, 0), (800, 800))
        self.moving_right = True
        self.running = True

    def run_game(self):
        while self.running:
            self._check_events()
            self.screen.fill(self.bg_color)
            self._game_logic()
            self.draw_obstacles()
            self._update_screen()

            if not self.snake_alive(self.snake.head_rect()):
                self.running = False

            FPS = 2
            clock = pygame.time.Clock()
            clock.tick(FPS)

    def draw_obstacles(self):
        left_rect = pygame.Rect((0, 0), (200, 800))
        right_rect = pygame.Rect((1000, 0), (200, 800))
        pygame.draw.rect(self.screen, (196, 196, 196), left_rect)
        pygame.draw.rect(self.screen, (196, 196, 196), right_rect)
        pygame.draw.rect(self.screen, RED, self.berry_rect)

    def snake_alive(self, rect):
        in_bounds = (self.game_rect.colliderect(rect))

        snake_collision = False
        # print(self.snake.occupied_squares()[1:])
        # print(self.snake.head_pos(), 'head')
        if self.snake.head_pos() in self.snake.occupied_squares()[1:]:
            snake_collision = True
        return((in_bounds) and (not snake_collision))

    
    def place_berry(self):
        berry_opts = self.all_positions
        for pos in self.snake.occupied_squares():
            if pos in berry_opts:
                berry_opts.remove(pos)
        berry_pos = random.choice(berry_opts)
        print(berry_pos)
        self.berry_rect = pygame.Rect(GridHelper().pos_to_coord(berry_pos), (50, 50))

    def berry_collision(self, rect):
        return(self.berry_rect.colliderect(rect))
            

    def _check_events(self):
        evts = pygame.event.get()
        for event in evts:
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP) and not self.moving_down:
                    self.stop_movement()
                    self.moving_up = True
                elif event.key == pygame.K_DOWN and not self.moving_up:
                    self.stop_movement()
                    self.moving_down = True
                elif event.key == pygame.K_LEFT and not self.moving_right:
                    self.stop_movement()
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT and not self.moving_left:
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
        
        if self.berry_collision(self.snake.head_rect()):
            self.snake.grow()
            self.place_berry()

    def stop_movement(self):
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False

    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    snake = SnakeGame()
    snake.run_game()