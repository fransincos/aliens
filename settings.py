class Settings:
	"""A class for the beast ass settings"""

	def __init__(self):
		"""initialize all of the games static settings"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (63, 72, 204)
		
		
		self.ship_limit = 3
		
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (254, 52, 1)
		self.bullets_allowed = 10
		
		self.afterglow_speed = 0.8
		self.afterglow_width = 8
		self.afterglow_height = 8
		self.afterglow_color = (252, 207, 73)
		self.afterglows_allowed = 4

		
		self.army_dropspeed = 5

		self.speedup_scale = 1.3

		self.score_scale = 1.5

		self.init_dynamic_settings()

	def init_dynamic_settings(self):
		"""starddup the moving settings"""
		self.ship_speed = 1.5
		self.bullet_speed = 1.3
		self.alien_speed = 1.0

		self.army_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		"""increase speed"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)