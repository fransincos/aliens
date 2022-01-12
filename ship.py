import pygame

class Ship:
	"""da ship!"""

	def __init__(self, ai_game):
		"""boot up da shipa nd the start position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect

		#load the ship image and get the rektangL
		self.image = pygame