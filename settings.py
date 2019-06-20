class Settings():
	def __init__(self):
		"""初始化游戏的静态设置"""
		self.screen_width=800
		self.screen_height=600
		
		"""角色设置"""
		self.char_speed_factor=2
		
		"""敌人设置"""
		self.enemy_speed_factor=3
		self.enemies_allowed=10
		self.enemy_damage=20
		
		"""背景颜色"""
		self.bg_color=(255,255,255)

	def initialize_dynamic_settings(self):
		
		"""初始化随游戏进行而变化的设置"""
		# 记分
		self.enemy_points = 50
