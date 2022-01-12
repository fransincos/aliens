import sys

import pygame

from settings import Settings

class AlienInvasion:
	"""Overall class managing the big boy stuff: game assets and behavior"""

	def __init__(self):
		"""startup the game and make the resources!"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		#Backgound color
		self.bg_color = (self.settings.bg_color)

	def run_game(self):
		"""The main game loop"""
		while True:
			#watch for keyboard and mouse events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			#redraw the screen during each pass through the loop
			self.screen.fill(self.bg_color)

			#make the most recently drawn screen visible
			pygame.display.flip()

if __name__ == '__main__':
	#make an instance to run the game
	ai = AlienInvasion()
	ai.run_game()