import pygame
import projectile as prjct

SPEED = 10
PROJ_CD = 60

class Player:

    def __init__(self, x, y):
        self.image = pygame.image.load("resources/player.png")
        self.x = x
        self.y = y
        self.cd = 0

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

    def get_projectile(self, event):
        if self.cd == 0:
            self.cd = PROJ_CD
            proj = prjct.Projectile(self.x, self.y, event)
            return proj
        else:
            return None

    def update_cd(self):
        if self.cd > 0:
            self.cd -= 1


    def update(self, screen):
        self.get_movement()
        self.update_cd()

        screen.blit(self.image, (self.x, self.y))