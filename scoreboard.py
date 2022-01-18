import pygame.font

from pygame.sprite import Group

from ship import Ship

import json

class Scoreboard:
	"""The scoh info"""

	def __init__(self, ai_game):
		"""starddup the score attributes"""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont('Corbel', 48)

		self.prep_hiscore()
		self.prep_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""render the score as an img"""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_hiscore(self):
		"""render hiscore as img"""
		hiscore = round(self.stats.hiscore, -1)
		hiscore_str = "{:,}".format(hiscore)
		self.hiscore_image = self.font.render(hiscore_str, True,
			self.text_color)

		self.hiscore_rect = self.hiscore_image.get_rect()
		self.hiscore_rect.midtop = self.screen_rect.midtop

	def prep_level(self):
		"""render the level ur on as an image"""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
			self.text_color)

		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""make the three little shits in the left corner"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		"""display the score on the screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.hiscore_image, self.hiscore_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def check_hiscore(self):
		"""czech the high scoh"""
		if self.stats.score > self.stats.hiscore:
			self.stats.hiscore = self.stats.score
			self.prep_hiscore()
