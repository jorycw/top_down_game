import pygame

SPEED = 4

class Player:

    def __init__(self, x, y):
        self.image = pygame.image.load("resources/player.png")
        self.x = x
        self.y = y

    def get_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.x -= SPEED
        if keys_pressed[pygame.K_RIGHT]:
            self.x += SPEED
        if keys_pressed[pygame.K_UP]:
            self.y -= SPEED
        if keys_pressed[pygame.K_DOWN]:
            self.y += SPEED

    def detect_click(self):
        not_done = True

    def update(self, screen):
        self.get_movement()
        screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()