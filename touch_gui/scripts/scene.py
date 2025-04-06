import pygame

class Scene:
    def __init__(self, assets):
        self.assets = assets
        self._base_resolution = assets["base_resolution"]
        self._images = assets["images"]
        self._colors = assets["colors"]
        self._fonts = assets["fonts"]
        self._surface = pygame.Surface(self._base_resolution)
        self._background_color = (255, 255, 255)
        self._change_scene = False
        self._next_scene = None

    @property
    def surface(self):
        return self._surface

    @property
    def change_scene(self):
        return self._change_scene

    @property
    def next_scene(self):
        return self._next_scene

    def update(self):
        raise NotImplementedError("Subclasses must implement this method.")
        return

    def draw(self):
        raise NotImplementedError("Subclasses must implement this method.")
        return
