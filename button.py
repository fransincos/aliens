import pygame.font

class Button:
	"""initialize button attributes"""
	def __init__(self, ai_game, msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 200, 50
		self.button_color = (0, 255, 155)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Corbel', 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""show the play game message"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""make the button and message"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class EasyButton:
	"""easy button attributes"""
	def __init__(self, ai_game, msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 250, 100
		self.button_color = (0, 200, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Corbel', 55)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		 
		self.rect.topleft = self.screen_rect.topleft

		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""show the play game message"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""make the button and message"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class MedButton:
	"""initialize button attributes"""
	def __init__(self, ai_game, msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 250, 100
		self.button_color = (237, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Corbel', 55)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.midtop = self.screen_rect.midtop

		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""show the play game message"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""make the button and message"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class HardButton:
	"""initialize button attributes"""
	def __init__(self, ai_game, msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 250, 100
		self.button_color = (237, 185, 27)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('Corbel', 55)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.topright = self.screen_rect.topright

		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""show the play game message"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""make the button and message"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)