import pygame
from pygame.sprite import Sprite
from mysprite import *

class Char(Sprite):
	def __init__(self, ai_settings, screen):
		super(Char, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load('images/baby.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)
		
		# 移动标志
		self.moving_right = False
		self.moving_left = False
		
		#血量
		self.health = 100
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update_default(self, screen, background):
		
		self.image = pygame.image.load('images/baby.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
				
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom-10
					
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)		

	def update_stage1(self, screen, background):
		
		self.image = pygame.image.load('images/child.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
				
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
					
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)		
		
	def update_stage2(self, screen, background):
		
		self.image = pygame.image.load('images/teenager.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
				
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
					
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)		

	def update_stage3(self, screen, background):
		
		self.image = pygame.image.load('images/dude.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.ai_settings.char_speed_factor=1
		self.ai_settings.enemy_speed_factor=2
				
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
					
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)		
	
	def update_stage4(self, screen, background):
		
		self.image = pygame.image.load('images/bold.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.ai_settings.char_speed_factor=2
		self.ai_settings.enemy_speed_factor=3
			
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
					
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)		
		
	def update_stage5(self, screen, background):
		
		self.image = pygame.image.load('images/old.png')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.ai_settings.char_speed_factor=1
		self.ai_settings.enemy_speed_factor=2
				
		#放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
					
		# 在属性center中存储小数值
		self.center = float(self.rect.centerx)		
