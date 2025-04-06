import pygame

from .scene import Scene


class HomeScene(Scene):
    def __init__(self, assets):
        super().__init__(assets)
        self._background_color = self._colors["mid"]

    def update(self, render_resolution, cursor_pos):
        pass

    def draw(self, render_resolution):
        self._surface.fill(self._background_color)
        self._surface.blit(self._images["home_window"], (0, 0))
        return
