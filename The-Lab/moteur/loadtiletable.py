import pygame
import pygame.locals


#Thomas Lemaitre 

#Encore utilisé dans le projet a 1 endroit ou 2 mais obsolète (Remplacé par un methode dans Image)

def load_tile_table(filename, width, height):
    '''
    permet de charger un tile table en natif avec pygame (pour la classe map) car flemme de changer avec l'objet Image (même si possible)
    '''
    image = pygame.image.load(filename)
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width//width):
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            tile_table.append(image.subsurface(rect))
    return tile_table
