import pygame


class Mouse():
	def __init__(self, ai_settings, screen):
		
		self.screen = screen
		self.ai_settings = ai_settings
		#Ìæ»»Êó±êÍ¼±ê
		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
		self.cursor = pygame.image.load("images/aim.png").convert_alpha()
		#Òş²ØÊó±ê
		pygame.mouse.set_visible(False)
		
		
	def update(self):

		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
		self.mouse_x -= 12
		self.mouse_y -= 12
	
	
