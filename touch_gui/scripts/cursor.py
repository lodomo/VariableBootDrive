import pygame


class Cursor:
    def __init__(self, sprite, base_resolution, timeout=120):
        self.__base_resolution = base_resolution
        self.__pos = (0, 0)
        self.__relative_pos = (0, 0)
        self.__timeout = timeout
        self.__last_update = timeout
        self.__sprite = sprite

    @property
    def pos(self):
        return self.__relative_pos

    def update(self, window_size):
        previous_pos = self.__pos
        self.__pos = self.get_pos(window_size)

        if self.__pos == previous_pos:
            self.__last_update += 1
        else:
            self.__last_update = 0

    def draw(self, screen):
        if self.__last_update >= self.__timeout:
            return

        cursor = self.__sprite
        cursor_rect = cursor.get_rect()
        cursor_rect.topleft = self.__pos
        screen.blit(cursor, cursor_rect)

    def get_pos(self, window_size):
        if not self.__base_resolution:
            return pygame.mouse.get_pos()

        ratio = (
            window_size[0] / self.__base_resolution[0],
            window_size[1] / self.__base_resolution[1],
        )
        screen_mouse_pos = pygame.mouse.get_pos()
        relative_mouse_position = (
            int(screen_mouse_pos[0] / ratio[0]),
            int(screen_mouse_pos[1] / ratio[1]),
        )

        self.__relative_pos = relative_mouse_position

        return relative_mouse_position
