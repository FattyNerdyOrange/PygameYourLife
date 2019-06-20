from math import *
import pygame, sys
from pygame.sprite import Sprite
import random

class Enemy(Sprite):
	
	def __init__(self, ai_settings, screen):
		super(Enemy, self).__init__()
		self.ai_settings=ai_settings
		self.screen=screen
		self.image = pygame.image.load('images/dinasour.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#初始位置从上方随机生成，并且高度不同这样掉下来的顺序就不同了
		self.rect.centerx=random.randint(0, 800)
		self.rect.bottom=0
		self.rect.bottom -= random.randint(0,300)
		self.y = float(self.rect.bottom)		
		
		
	def update(self, ai_settings, char, background):
		
		#垂直落下
		self.y += ai_settings.enemy_speed_factor
		self.rect.bottom = self.y
		
		#如果到达底部则返回初始位置（这里还需要添加一个碰到玩家的情况）
		if self.rect.bottom >= self.screen_rect.bottom:
			self.rect.centerx=random.randint(0, 800)
			self.rect.bottom=0
			self.rect.bottom -= random.randint(0,25)
			
		#如果玩家移动，敌人要保持不动（水平方向）
		if char.moving_right and background.bg_x > -4000 :
			self.rect.x -= ai_settings.char_speed_factor
		if char.moving_left and background.bg_x < 0 :
			self.rect.x += ai_settings.char_speed_factor

	def draw_enemy(self):
		self.screen.blit(self.image, self.rect)
	
