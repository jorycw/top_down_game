import pygame
import player as plyr
import math

SPEED = 13

class Projectile:

	def __init__(self, x, y, event):
		self.image = pygame.image.load("resources/projectile.png")
		self.x = x
		self.y = y
		x_, y_ = pygame.mouse.get_pos()
		x_delta = x_ - x
		y_delta = y_ - y
		
		vec_size = math.sqrt(x_delta ** 2 + y_delta ** 2)
		unit_vec = (x_delta / vec_size, y_delta / vec_size)
		self.vector = unit_vec

	def update(self, screen):
		self.x += self.vector[0] * SPEED
		self.y += self.vector[1] * SPEED

		screen.blit(self.image, (self.x, self.y))