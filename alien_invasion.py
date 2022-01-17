import sys

import pygame

from settings import Settings

from gamestats import GameStats

from ship import Ship

from bullet import Bullets

from afterglow import Afterglow

from alien import Alien

from time import sleep

from button import Button

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

		self.stats = GameStats(self)

		self.ship = Ship(self)	
		self.bullets = pygame.sprite.Group()	
		self.afterglows = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_army()
		
		self.play_button = Button(self, "PLAY")
		#Backgound color
		self.bg_color = (self.settings.bg_color)

	def run_game(self):
		"""The main game loop"""
		while True:
			self._check_events()			
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_afterglows()
				self._update_aliens()
			self._update_screen()
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
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

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

	def _check_play_button(self, mouse_pos):
		"""check pos of the mouse click"""
		
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self.stats.reset_stats()
			self.stats.game_active = True
			self.aliens.empty()
			self.bullets.empty()

			self._create_army()
			self.ship.center_ship()
	
	def _ship_hit(self):
		"""respond to a ship getting fucked up by an alien"""
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.aliens.empty()
			self.bullets.empty()
			self._create_army()
			self.ship.center_ship()
			sleep(0.5)
		else:
			self.stats.game_active = False

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
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)
		if not self.aliens:
			self.bullets.empty()
			self._create_army()
	
	def _check_aliens_bottom(self):
		"""check if any aliens have reached the bottom"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _update_aliens(self):
		"""update alien position"""	
		self._check_army_edges()
		self.aliens.update()

		#look for alien and ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		self._check_aliens_bottom()
	def _create_army(self):
		"""make the army of mexicos"""
		#alien and the number of them allowed through this awesome formula
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size

		# the rows of aliens that can fit on a screen
		ship_height = self.ship.rect.height 
		availible_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = availible_space_y // (2 * alien_height)
		availible_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = availible_space_x // (2 * alien_width)		
		
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		"""create alien and place in row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + (2 * alien_width) * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + (2 * alien.rect.height) * row_number
		self.aliens.add(alien)

	def _check_army_edges(self):
		"""make the right decison on edge contact"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_army_direction()
				break

	def _change_army_direction(self):
		"""move down and change direction!"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.army_dropspeed
		self.settings.army_direction *= -1
	

	def _update_screen(self):
		"""update the screen with every change"""
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for afterglow in self.afterglows.sprites():
			afterglow.draw_afterglow()
		self.aliens.draw(self.screen)
		if not self.stats.game_active:
			self.play_button.draw_button()
		#the unintuitivley named update screen command
		pygame.display.flip()





if __name__ == '__main__':
	#make an instance to run the game
	ai = AlienInvasion()
	ai.run_game()