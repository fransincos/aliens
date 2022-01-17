import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""representing the alien"""

	def __init__(self, ai_game):
		"""start up the alien"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#load the image of the illegal alien
		self.image = pygame.image.load('images/mexico.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def check_edges(self):
		"""say true if the alien reaches the end of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""move the alien 2 the right oh left"""
		self.x += self.settings.alien_speed * self.settings.army_direction
		
		self.rect.x = self.x
		#positive is to the right, and negative is to the left
		