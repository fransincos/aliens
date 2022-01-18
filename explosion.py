import pygame

from pygame.sprite import Sprite

class Explosion(Sprite):
	"""BOOM"""

	def __init__(self, ai_game):
		"""blow up effect on bullet collision with alien"""
		super().__init__()
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/explode.bmp')
		self.rect = self.image.get_rect()
		

	def draw_explosion(self):
		"""draw the bullet to the screen"""
		self.screen.blit(self.image, self.rect)