import pygame
from pygame.sprite import Sprite

class Bg(Sprite):
	def __init__(self, ai_settings, screen):
		super(Bg, self).__init__()
		
		self.screen = screen
		self.ai_settings = ai_settings
		self.bg_x=0
		float(self.bg_x)
		
		self.image=pygame.image.load("images/backgroundpic.png")
		self.rect=self.image.get_rect()
		
	def update(self, char):
		"""根据移动标志调整位置"""
		#self.bg_x是左上角的坐标，要在图片的右边到达屏幕时停下，需要减掉一个屏幕的宽度，即800
		if char.moving_right and self.bg_x > -4000 :
			self.bg_x -= char.ai_settings.char_speed_factor
		if char.moving_left and self.bg_x < 0 :
			self.bg_x += char.ai_settings.char_speed_factor

	def bg_reset(self):
		"""用于重新开始游戏时重置角色位置"""
		self.bg_x=0
