import pygame
import projectile as prjct

SPEED = 10
PROJ_CD = 60

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/player.png")
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.cd = 0

    def movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= SPEED
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += SPEED
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= SPEED
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += SPEED

    def get_projectile(self, event):
        if self.cd == 0:
            self.cd = PROJ_CD
            proj = prjct.Projectile(self.rect, event)
            return proj
        else:
            return None

    def update_cd(self):
        if self.cd > 0:
            self.cd -= 1


    def update(self, screen):
        self.movement()
        self.update_cd()
        screen.blit(self.image, self.rect)