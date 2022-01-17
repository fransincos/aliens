class Settings:
	"""A class for the beast ass settings"""

	def __init__(self):
		"""initialize all of the game settings"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (63, 72, 204)
		
		self.ship_speed = 1.5
		self.ship_limit = 3
		
		self.bullet_speed = 1.3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (254, 52, 1)
		self.bullets_allowed = 10
		
		self.afterglow_speed = 0.8
		self.afterglow_width = 8
		self.afterglow_height = 8
		self.afterglow_color = (252, 207, 73)
		self.afterglows_allowed = 3

		self.alien_speed = 1
		self.army_dropspeed = 5
		self.army_direction = 1

