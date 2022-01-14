import pygame

from pygame.sprite import Sprite

class Afterglow(Sprite):
	"""the pew pew pew effect"""

	def __init__(self, ai_game):
		"""create the bullet object at the ships current posicion"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.afterglow_color

		#create a bullet rectangle at (0,0) and set da position
		self.rect = pygame.Rect(0,0, self.settings.afterglow_width, 
			self.settings.afterglow_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#store the bullet position as a float for fine adjustment
		self.y = float(self.rect.y)

	def update(self):
		"""move the bullet up the screen"""
		self.y -= self.settings.afterglow_speed
		self.rect.y = self.y 

	def draw_afterglow(self):
		"""draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)