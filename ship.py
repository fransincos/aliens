import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
	"""da ship!"""

	def __init__(self, ai_game):
		"""boot up da shipa nd the start position"""
		super().__init__()
		
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#load the ship image and get the rektangL
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#starddit at the bottom middle of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#store a decimal value for a ships x position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		#movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""update the ship's posiition based on the movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 750:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		#update rect object from self.x and self.y
		self.rect.x = self.x
		self.rect.y = self.y

	def center_ship(self):
		"""recenter the ship after eating shit"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	def blitme(self):
		"""draw where the ship is"""
		self.screen.blit(self.image, self.rect)