import os
import subprocess

import pygame
import yaml
from scripts import Cursor, PinInputScene

pygame.init()
SETTINGS = yaml.safe_load(open("settings.yaml"))["touch_gui"]
RESOLUTION = (SETTINGS["res_width"], SETTINGS["res_height"])
MAIN_SCREEN = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)
RENDER_RESOLUTION = RESOLUTION
IMAGES = {}
COLORS = {}
FONTS = {}


def main():
    global MAIN_SCREEN, SETTINGS, RESOLUTION, RENDER_RESOLUTION, IMAGES, COLORS
    load_assets()

    assets = {
        "base_resolution": RESOLUTION,
        "images": IMAGES,
        "colors": COLORS,
        "fonts": FONTS,
    }

    title = SETTINGS["title"]
    fps = SETTINGS["fps"]
    clock = pygame.time.Clock()

    pygame.display.set_caption(title)
    pygame.mouse.set_visible(False)
    current_scene = PinInputScene(assets)
    cursor = Cursor(IMAGES["cursor"], RESOLUTION)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                resize_screen((event.w, event.h))
                RENDER_RESOLUTION = (event.w, event.h)

        cursor.update(RENDER_RESOLUTION)
        current_scene.update(RENDER_RESOLUTION, cursor.pos)
        current_scene.draw(RENDER_RESOLUTION)
        cursor.draw(current_scene.surface)
        render(current_scene.surface)

        pygame.display.flip()
        clock.tick(fps)

        if current_scene.change_scene:
            current_scene = current_scene.next_scene

    pygame.quit()


def resize_screen(resolution):
    """
    Resize the screen to a new resolution.
    This should be triggered by the VIDEORESIZE event.
    """
    global MAIN_SCREEN
    if MAIN_SCREEN.get_size() != resolution:
        MAIN_SCREEN = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    return


def render(surface):
    """
    Scale 'surface' to the current resolution and blit it to the screen.
    """
    global MAIN_SCREEN, RENDER_RESOLUTION
    scaled_surface = pygame.transform.scale(surface, RENDER_RESOLUTION)
    MAIN_SCREEN.blit(scaled_surface, (0, 0))
    return


def load_assets():
    load_colors()
    load_images()
    load_fonts()
    return


def load_colors():
    global COLORS
    for key, value in SETTINGS["colors"].items():
        COLORS[key] = pygame.Color(value)
    return


def load_images():
    global IMAGES
    IMAGE_FOLDER = "images"
    for filename in os.listdir(IMAGE_FOLDER):
        if filename.endswith(".png"):
            key = os.path.splitext(filename)[0]  # Remove file extension
            IMAGES[key] = pygame.image.load(os.path.join(IMAGE_FOLDER, filename))
    return


def load_fonts():
    global FONTS
    FONT_FOLDER = "fonts"
    for filename in os.listdir(FONT_FOLDER):
        if filename.endswith(".ttf"):
            key = os.path.splitext(filename)[0]  # Remove file extension
            FONTS[key] = pygame.font.Font(os.path.join(FONT_FOLDER, filename), 32)
    return


if __name__ == "__main__":
    main()
