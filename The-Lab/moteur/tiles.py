import pygame
import pygame.locals

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename)
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width//width):
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            tile_table.append(image.subsurface(rect))
    return tile_table
