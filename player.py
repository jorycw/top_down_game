import pygame
import projectile as prjct

SPEED = 5
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
        change = [0, 0]
        if keys_pressed[pygame.K_LEFT]:
            change[0] -= SPEED
        if keys_pressed[pygame.K_RIGHT]:
            change[0] += SPEED
        if keys_pressed[pygame.K_UP]:
            change[1] -= SPEED
        if keys_pressed[pygame.K_DOWN]:
            change[1] += SPEED
        #3self.rect.x, 
        self.rect.x += change[0]
        self.rect.y += change[1]

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
        screen.draw.filled_rect(self.rect, (255, 255, 255))
        self.movement()
        self.update_cd()
        screen.blit(self.image, self.rect)
        pygame.display.update(self.rect)
