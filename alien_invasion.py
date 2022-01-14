import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullets

from afterglow import Afterglow

class AlienInvasion:
	"""Overall class managing the big boy stuff: game assets and behavior"""

	def __init__(self):
		"""startup the game and make the resources!"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		
		self.bullets = pygame.sprite.Group()
		
		self.afterglows = pygame.sprite.Group()
		#Backgound color
		self.bg_color = (self.settings.bg_color)

	def run_game(self):
		"""The main game loop"""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullets()
			self._update_afterglows()
			#redraw the screen during each pass through the loop
			self.screen.fill(self.bg_color)
			self.ship.blitme()
			for bullet in self.bullets.copy():
				if bullet.rect.top <= 0:
					self.bullets.remove(bullet)
			for afterglow in self.afterglows.copy():
				if afterglow.rect.top <= 700:
					self.afterglows.remove(afterglow)
			

	def _check_events(self):
		"""respond to keypresses and maus clicks"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""respond to keydown events"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
			self._show_afterglow()

	def _check_keyup_events(self, event):
		"""respond to keyup events"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		"""fire the bullet!"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullets(self)
			self.bullets.add(new_bullet)

	def _show_afterglow(self):
		"""the boom boom behind the bullet"""
		if len(self.afterglows) < self.settings.afterglows_allowed:
			new_afterglow = Afterglow(self)
			self.afterglows.add(new_afterglow)

	def _update_afterglows(self):
		"""update and get rid of boom boom effect"""
		self.afterglows.update()

	def _update_bullets(self):
		"""update position of and get rid of bullets"""
		self.bullets.update()

	def _update_screen(self):
		"""update the screen with every change"""
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for afterglow in self.afterglows.sprites():
			afterglow.draw_afterglow()
		#the unintuitivley named update screen command
		pygame.display.flip()

if __name__ == '__main__':
	#make an instance to run the game
	ai = AlienInvasion()
	ai.run_game()