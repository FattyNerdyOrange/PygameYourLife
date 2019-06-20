class Timeclock():
	"""计时器"""
	def __init__(self):
		
		#初始秒数为0
		self.t = 0

	def delay(self, dt, time):
		self.t += dt
		if self.t >= time :
			self.t = 0
			return True
		else:
			return False


		# #每过1000ms，掉下来一个敌人
	# dt = pygame.time.Clock().get_time()
	# if timer.delay(dt, 1000):
		# for enemy in enemies.sprites():
			# enemy.draw_enemy()
			# #重置时间
			# time.t = 0
