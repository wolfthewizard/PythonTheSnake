import pygame


class ActionFrame:

    def __init__(self, grid_size, node_size, components=None, bg_color=(150, 150, 150)):
        pygame.display.set_caption("Python the Game")
        self.window = pygame.display.set_mode((grid_size.x * node_size.x, grid_size.y * node_size.y))
        self.grid_size = grid_size
        self.node_size = node_size
        self.components = components
        if not self.components:
            self.components = []
        self.bg_color = bg_color

    def add_rendering_component(self, component):
        self.components.append(component)

    def remove_rendering_component(self, component):
        if component in self.components:
            self.components.remove(component)

    def apply_absolute_cords(self, rendering_component):
        pos = rendering_component.position
        pos.x *= self.node_size.x
        pos.y *= self.node_size.y
        return rendering_component

    def get_rendering_components(self):
        return [self.apply_absolute_cords(rc) for c in self.components for rc in c.get_rendering_components()]
