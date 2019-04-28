import pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
           
        image = pygame.image.load('resources/block.png')
        self.rect = image.get_rect()
           
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
    	image = pygame.image.load('resources/block.png')
    	screen.blit(image, self.rect)