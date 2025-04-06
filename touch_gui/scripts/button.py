import pygame


class Button:
    def __init__(
        self,
        position,
        value,
        sprite_sheet,
        label,
        width,
        height,
        label_offset,
        hover_offset,
        press_offset,
    ):
        self._sprite_sheet = sprite_sheet
        self._pos = position
        self._size = (width, height)
        self._label = label
        self._label_offset = label_offset
        self._hover_offset = hover_offset
        self._press_offset = press_offset

        self._label_posit = (
            self._pos[0] + self._label_offset[0],
            self._pos[1] + self._label_offset[1],
        )
        self._label_draw_posit = self._label_posit
        self._states = {"idle": 0, "hover": 1, "pressed": 2}

        self._sprites = self._set_sprites(self._sprite_sheet)
        self._state = self._states["idle"]
        self._pressed = False
        self._value = value

    @property
    def pressed(self):
        return self._pressed

    @property
    def value(self):
        return self._value

    def _set_sprites(self, sprite_sheet):
        sprites = {}
        sprites[self._states["idle"]] = sprite_sheet.subsurface(
            pygame.Rect(0, 0, self._size[0], self._size[1])
        )

        sprites[self._states["hover"]] = sprite_sheet.subsurface(
            pygame.Rect(self._size[0], 0, self._size[0], self._size[1])
        )

        sprites[self._states["pressed"]] = sprite_sheet.subsurface(
            pygame.Rect(self._size[0] * 2, 0, self._size[0], self._size[1])
        )
        return sprites

    def update(self, cursor_pos):
        state_was = self._state
        self._pressed = False

        # Check if the cursor is outside the button
        if (
            cursor_pos[0] < self._pos[0]
            or cursor_pos[1] < self._pos[1]
            or cursor_pos[0] > self._pos[0] + self._size[0]
            or cursor_pos[1] > self._pos[1] + self._size[1]
        ):
            self._state = self._states["idle"]
            self._label_draw_posit = self._label_posit
            return

        # Check if the button is being pressed
        if pygame.mouse.get_pressed()[0]:
            self._state = self._states["pressed"]
            self._label_draw_posit = (
                self._label_posit[0] + self._press_offset[0],
                self._label_posit[1] + self._press_offset[1],
            )
            return

        # Check if the cursor is hovering over the button
        self._state = self._states["hover"]
        self._label_draw_posit = (
            self._label_posit[0] + self._hover_offset[0],
            self._label_posit[1] + self._hover_offset[1],
        )

        # The button gets marked as pressed for 1 frame when the mouse is released
        if self._state == self._states["hover"] and state_was == self._states["pressed"]:
            self._pressed = True
        else:
            self._pressed = False
        return

    def draw(self, screen):
        screen.blit(self._sprites[self._state], self._pos)
        screen.blit(self._label, self._label_draw_posit)
