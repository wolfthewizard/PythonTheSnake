import pygame

from Model.Vector import Vector


class MouseInputProvider:

    @staticmethod
    def get_click_position():
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
                mouse_position = pygame.mouse.get_pos()
                return Vector(mouse_position[0], mouse_position[1])
