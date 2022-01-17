class GameStats:
	"""stattracker"""

	def __init__(self, ai_game):
		"""initialize settings"""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False
	def reset_stats(self):
		"""initialize statistics that may change during the game"""
		self.ships_left = self.settings.ship_limit