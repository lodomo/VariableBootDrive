import pygame

from .button import Button
from .device_api import DeviceAPI
from .scene import Scene
from .scene_home import HomeScene


class PinInputScene(Scene):
    def __init__(self, assets):
        """
        From Parent:
        _surface = pygame.Surface(resolution)
        _images = images
        _background_color = (255, 255, 255)
        _change_scene = False
        """
        super().__init__(assets)
        self._background_color = self._colors["mid"]
        self.__buttons = []
        self.__pin_input = ""
        self.create_buttons()
        self.pin_window = PinWindow((89, 2), self._images, self._colors)

    def update(self, render_resolution, cursor_pos):
        for button in self.__buttons:
            button.update(cursor_pos)
            if button.pressed:
                self.update_pin(button.value)
                print("Pin input:", self.__pin_input)
        self.pin_window.update()

        # Check if the pin is complete.
        if len(self.__pin_input) == 4:
            if DeviceAPI().sign_in(self.__pin_input):
                self._change_scene = True
                self._next_scene = HomeScene(self.assets)
            else:
                self._change_scene = True
                self._next_scene = AccessDeniedScene(self.assets)
        return

    def draw(self, render_resolution):
        self._surface.fill(self._background_color)

        # Backgrounds
        self._surface.blit(self._images["graffiti"], (0, 0))
        self._surface.blit(self._images["pin_entry_box"], (0, 0))
        self.pin_window.draw(self._surface, self.__pin_input)

        for button in self.__buttons:
            button.draw(self._surface)

        for i in range(len(self.__pin_input)):
            if i >= 4:
                break

            self._surface.blit(self._images["pin_light"], (6 + 10 * i, 2))

        pass

    def create_buttons(self):
        button_names = "1234567890<C"
        button_names = list(button_names)
        button_index = 0
        first_posit = (3, 10)
        width = 26
        space = 1
        for h in range(4):
            for w in range(3):
                pos = (
                    first_posit[0] + (width + space) * w,
                    first_posit[1] + (width + space) * h,
                )
                # Create a rect of a sprite sheet, 16x16, for each number on the "pin_numbers" sheet
                button_label = self._images["pin_numbers"].subsurface(
                    pygame.Rect(16 * button_index, 0, 16, 16)
                )
                self.__buttons.append(
                    PinButton(
                        pos,
                        button_names.pop(0),
                        self._images["pin_button"],
                        button_label,
                    )
                )
                button_index += 1

    def update_pin(self, value):
        if value == "<":
            self.__pin_input = self.__pin_input[:-1]
            return

        if value == "C":
            self.__pin_input = ""
            return

        self.__pin_input += value
        return


class PinWindow:
    def __init__(self, pos, images, colors):
        self.colors = colors
        self.sprite = images["pin_entry_window"]
        self.pos = pos
        self.size = self.sprite.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.set_colorkey(self.colors["transparent"])
        self.big_x = images["pin_big_x"]

        self.pin_cursor = [
            images["pin_entry_cursor"].subsurface(pygame.Rect(0, 0, 14, 37)),
            images["pin_entry_cursor"].subsurface(pygame.Rect(14, 0, 14, 37)),
        ]

        self.pin_cursor_index = 0
        self.flash_timer = 0
        self.flash_speed = 30
        self.input_y_pos = 32
        self.input_x_pos = [11, 34, 57, 80]

    def draw(self, screen, current_pin):
        self.surface.fill(self.colors["transparent"])
        self.surface.blit(self.sprite, (0, 0))

        for i, pin in enumerate(current_pin):
            if i >= 4:
                break
            self.surface.blit(self.big_x, (self.input_x_pos[i], self.input_y_pos))

        if len(current_pin) < 4:
            self.surface.blit(
                self.pin_cursor[self.pin_cursor_index],
                (self.input_x_pos[len(current_pin)], self.input_y_pos),
            )
        screen.blit(self.surface, self.pos)
        return

    def update(self):
        self.flash_timer += 1
        if self.flash_timer >= self.flash_speed:
            self.flash_timer = 0
            self.pin_cursor_index = 0 if self.pin_cursor_index else 1

        return


class PinButton(Button):
    def __init__(self, pos, value, sprite_sheet, label):
        width = 26
        height = 26
        label_offset = (5, 5)
        hover_offset = (-1, -1)
        press_offset = (1, 1)
        super().__init__(
            pos,
            value,
            sprite_sheet,
            label,
            width,
            height,
            label_offset,
            hover_offset,
            press_offset,
        )


class AccessDeniedScene(Scene):
    def __init__(self, assets):
        super().__init__(assets)
        self._background_color = self._colors["mid"]
        self.lifetime = 120

    def update(self, render_resolution, cursor_pos):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self._change_scene = True
            self._next_scene = PinInputScene(self.assets)

    def draw(self, render_resolution):
        self._surface.fill(self._background_color)
        self._surface.blit(self._images["pin_access_denied"], (0, 0))
        return
