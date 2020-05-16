from Menu.Text import Text
from Rendering.ActionFrame import ActionFrame
from Menu.Button import Button
from Model.GameSettings import GameSettings
from Model.Vector import Vector
from Rendering.ResourceManager import ResourceManager


class MainMenuWindow:

    def __init__(self):
        self.node_size = Vector(40, 40)

        self.game_mode_text = Text(Vector(0, 0), "Game mode")
        self.is_player_button = Button(Vector(1, 1), Vector(1, 1), True, "Player")
        self.is_bot_button = Button(Vector(1, 2), Vector(1, 1), False, "Bot")

        self.rendering_text = Text(Vector(0, 4), "Rendering")
        self.rendering_enabled_button = Button(Vector(1, 5), Vector(1, 1), True, "Enabled")
        self.rendering_disabled_button = Button(Vector(1, 6), Vector(1, 1), False, "Disabled")

        self.board_size_text = Text(Vector(0, 8), "Board size")
        self.small_board_button = Button(Vector(1, 9), Vector(1, 1), True, "Small")
        self.medium_board_button = Button(Vector(1, 10), Vector(1, 1), False, "Medium")
        self.large_board_button = Button(Vector(1, 11), Vector(1, 1), False, "Large")

        self.start_button = Button(Vector(4, 13), Vector(3, 1), False, "Start game", sprite=ResourceManager.snake_head)

        self.buttons = [
            self.start_button, self.is_player_button, self.is_bot_button, self.game_mode_text,
            self.rendering_text, self.rendering_disabled_button, self.rendering_enabled_button,
            self.board_size_text, self.small_board_button, self.medium_board_button, self.large_board_button
        ]

    def handle_mouse_click(self, click_position):
        click_position = click_position.divide(self.node_size)
        if self.check_start_button_click(click_position):
            return True

        if self.check_player_buttons_click(click_position):
            return False

        if self.check_render_buttons_click(click_position):
            return False

        if self.check_board_size_buttons_click(click_position):
            return False

    def check_start_button_click(self, click_position):
        if self.start_button.contains_position(click_position):
            self.start_button.is_marked = True
            return True

    def check_player_buttons_click(self, click_position):
        if self.is_bot_button.contains_position(click_position):
            self.is_bot_button.is_marked = True
            self.is_player_button.is_marked = False
            return True
        elif self.is_player_button.contains_position(click_position):
            self.is_bot_button.is_marked = False
            self.is_player_button.is_marked = True
            self.rendering_enabled_button.is_marked = True
            self.rendering_disabled_button.is_marked = False
            return True

    def check_render_buttons_click(self, click_position):
        if self.is_bot_button.is_marked:
            if self.rendering_enabled_button.contains_position(click_position):
                self.rendering_enabled_button.is_marked = True
                self.rendering_disabled_button.is_marked = False
                return True
            elif self.rendering_disabled_button.contains_position(click_position):
                self.rendering_enabled_button.is_marked = False
                self.rendering_disabled_button.is_marked = True
                return True

    def check_board_size_buttons_click(self, click_position):
        if self.small_board_button.contains_position(click_position):
            self.small_board_button.is_marked = True
            self.medium_board_button.is_marked = False
            self.large_board_button.is_marked = False
            return True
        elif self.medium_board_button.contains_position(click_position):
            self.small_board_button.is_marked = False
            self.medium_board_button.is_marked = True
            self.large_board_button.is_marked = False
            return True
        elif self.large_board_button.contains_position(click_position):
            self.small_board_button.is_marked = False
            self.medium_board_button.is_marked = False
            self.large_board_button.is_marked = True
            return True

    def get_game_settings(self):
        if self.small_board_button.is_marked:
            board_size = 9
        elif self.medium_board_button.is_marked:
            board_size = 12
        else:
            board_size = 16

        return GameSettings(self.is_bot_button.is_marked, self.rendering_enabled_button.is_marked, board_size)

    def get_action_frame(self):
        return ActionFrame(
            Vector(11, 15),
            self.node_size,
            self.buttons
        )
