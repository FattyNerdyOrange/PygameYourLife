import pygame

class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()
		# 让游戏一开始处于非活动状态
		self.game_active = False
		#判断是否是从开始菜单开始游戏
		self.menu_start_flag = False
		#判断是否是因为玩家死亡而结束游戏
		self.game_over_flag = True
		# 在任何情况下都不应重置最高得分
		self.high_score = 0
		
	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.score = 0	
