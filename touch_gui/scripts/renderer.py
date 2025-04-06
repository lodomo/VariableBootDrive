import pygame


class Renderer:
    def __init__(self, base_resolution):
        self.__base_resolution = base_resolution
        self.__render_resolution = base_resolution

        self.__screen = pygame.display.set_mode(
            base_resolution, pygame.RESIZABLE)

    @property
    def base_resolution(self):
        """
        The resolution that the program should be rendered at no matter
        what the resolution of the screen is.

        It will squish or stretch the image to fit the screen, without any
        anti-aliasing.
        """
        return self.__base_resolution

    @property
    def current_resolution(self):
        """
        The resolution that the monitor/window is currently set to.
        """
        return self.__render_resolution

    def resize_screen(self, resolution):
        """
        Resize the screen to a new resolution.
        This should be triggered by the VIDEORESIZE event.
        """
        if self.__render_resolution == resolution:
            return
        self.__render_resolution = resolution
        self.__screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

    def render(self, surface):
        """
        Scale 'surface' to the current resolution and blit it to the screen.
        """
        scaled_surface = pygame.transform.scale(
            surface, self.__render_resolution)
        self.__screen.blit(scaled_surface, (0, 0))
