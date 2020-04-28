import random

import Util
from GameState import GameState
from Snake import Snake
from Vector import Vector


class GameManager:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.moving_direction = Vector(1, 0)

        snake_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
        self.snake = Snake(snake_pos)
        apple_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))
        while apple_pos.equals(snake_pos):
            apple_pos = Vector(random.randrange(grid_size.x), random.randrange(grid_size.y))

        self.apple_pos = apple_pos

    def simulate_move(self, input):
        if input is not None and not Util.is_opposite(self.moving_direction, input):
            self.moving_direction = input

        self.snake.move(self.moving_direction)

        # crossing border
        snake_head_pos = self.snake.head.get_pos()
        if snake_head_pos.x < 0:
            self.snake.head.change_pos(Vector(self.grid_size.x - 1, snake_head_pos.y))
        elif snake_head_pos.x > self.grid_size.x - 1:
            self.snake.head.change_pos(Vector(0, snake_head_pos.y))
        elif snake_head_pos.y < 0:
            self.snake.head.change_pos(Vector(snake_head_pos.x, self.grid_size.y - 1))
        elif snake_head_pos.y > self.grid_size.y - 1:
            self.snake.head.change_pos(Vector(snake_head_pos.x, 0))

        # eating apple
        if snake_head_pos.equals(self.apple_pos):
            self.snake.grow_pending = True

            # todo: delete when having implemented score system as actual size updates after some frames
            if self.snake.get_size() == self.grid_size.x * self.grid_size.y - 1:
                self.running = False

            while self.apple_pos in self.snake.get_slots_occupied_by_body() or \
                    self.apple_pos.equals(self.snake.head.get_pos()):
                self.apple_pos = Vector(random.randrange(self.grid_size.x), random.randrange(self.grid_size.y))

        # checking self collision
        if self.snake.check_collision():
            self.running = False

    def get_current_game_state(self):
        return GameState(self.grid_size, self.apple_pos, self.snake, self.moving_direction)
