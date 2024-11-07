import pygame


BASE_IMG_PATH = 'images/'

def load_image(path, size=None):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))

    if size:
        return pygame.transform.scale(img, size)
    return img