from Vector import Vector
from RenderPacket import RenderPacket
import pygame
import copy


class Head:

    sprite = pygame.image.load("resources/head.png")

    def __init__(self, position=Vector(0, 0), rotation=0):
        self.position = position
        self.rotation = rotation

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    def move_direction_to_rotation(self, move_direction):
        if move_direction.equals(Vector(0, -1)):
            self.rotation = 90
        elif move_direction.equals(Vector(-1, 0)):
            self.rotation = 180
        elif move_direction.equals(Vector(0, 1)):
            self.rotation = 270
        else:
            self.rotation = 0

    def move(self, moving_direction=Vector(0, 0)):
        previous_pos = Vector(self.position.x, self.position.y)
        self.position.x += moving_direction.x
        self.position.y += moving_direction.y
        return previous_pos

    def does_collide(self, another_body_piece):
        return self.position.equals(another_body_piece.pos)

    @staticmethod
    def convert_sprites():
        Head.sprite = Head.sprite.convert()
        Head.sprite.set_colorkey((255, 0, 255))

    def get_rendering_components(self):
        return RenderPacket(Head.sprite, copy.deepcopy(self.position), self.rotation)
