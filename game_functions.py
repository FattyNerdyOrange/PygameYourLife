import pygame
import sys
from char import *
from enemy import *
from time import sleep
from pygame.locals import *


def check_events(ai_settings, screen, char, stats, sb, play_button, quit_button, background, enemies):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, stats, ai_settings, screen, char)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, char)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			
			check_play_button(ai_settings, stats, sb, play_button, background, char, enemies, mouse_x, mouse_y)
			check_quit_button(stats, quit_button, mouse_x, mouse_y)
			#玩家通过点击鼠标射击敌人
			if stats.game_active:
				enemy_shot(ai_settings, stats, sb, enemies, mouse_x, mouse_y)

def enemy_shot(ai_settings, stats, sb, enemies, mouse_x, mouse_y):
	"""玩家点击鼠标射击敌人"""
	for enemy in enemies:	
		enemy_shot = enemy.rect.collidepoint(mouse_x, mouse_y)
		#射中的敌人消失
		if enemy_shot :
			stats.score += ai_settings.enemy_points * len(enemies)
			sb.prep_score()
			enemies.remove(enemy)
			#播放音效
			pygame.mixer.init()
			sound = pygame.mixer.Sound('sound/firebullets.wav')
			sound.play()
	check_high_score(stats, sb)
	
def check_high_score(stats, sb):
	"""检查是否诞生了新的最高得分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

	
def check_play_button(ai_settings, stats, sb, play_button, background, char, enemies, mouse_x, mouse_y):
	
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# 重置游戏设置
		ai_settings.initialize_dynamic_settings()
		#重置玩家位置
		background.bg_reset()
		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		# 重置记分牌图像
		sb.prep_score()
		sb.prep_high_score()
		char.health = 100
		# 清空敌人列表
		enemies.empty()
		pygame.mouse.set_visible(False)
		# 第一次从标题启动
		stats.menu_start_flag=True

def check_quit_button(stats, quit_button, mouse_x, mouse_y):
	"""ME.玩家点击quit按钮时结束游戏"""
	button_clicked = quit_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		sys.exit()		
			
def check_keydown_events(event, stats, ai_settings, screen, char):
	"""响应按键"""
	#此处有一bug，如果是在按住方向键过程中死亡，则继续按住方向键不松开的话，即便游戏结束画面弹出且玩家不松开按键的情况下，依然可以继续移动
	if event.key == pygame.K_RIGHT and stats.game_active:
		char.moving_right = True

	elif event.key == pygame.K_LEFT and stats.game_active:
		char.moving_left = True
		
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event, char):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		char.moving_right = False
	elif event.key == pygame.K_LEFT:
		char.moving_left = False
		
def enemy_drop(ai_settings, screen, char, background, enemies):
	"""一次性最多可以有10个敌人在屏幕上"""
	if len(enemies) < ai_settings.enemies_allowed:
		new_enemy = Enemy(ai_settings, screen)
		enemies.add(new_enemy)
	
	
def update_enemies(ai_settings, screen, sb, stats, char, background, enemies, play_button, quit_button):
	
	#更新敌人位置 
	enemies.update(ai_settings, char, background)
		
	#删除已消失的敌人
	for enemy in enemies.copy():
		if enemy.rect.bottom == 0:
			enemies.remove(enemy)
			
	#敌人撞击到玩家后消失
	for enemy in enemies :
		if pygame.Rect.colliderect(enemy.rect, char.rect):
			enemies.remove(enemy)
			char_hit(ai_settings, screen, sb, stats, char, enemies, play_button, quit_button)
			
def update_screen(ai_settings, screen, stats, sb, play_button, quit_button, aim, background, char, enemies):

	enemy_drop(ai_settings, screen, char, background, enemies)
	screen.blit(background.image, (background.bg_x,0))
	
			
	for enemy in enemies.sprites():
		enemy.draw_enemy()		
		
	
	#准星
	screen.blit(aim.cursor, (aim.mouse_x, aim.mouse_y))
	aim.update()
	
	#人物的移动实际上是背景的滚动
	background.update(char)
	# char.blitme()
	
	# 显示得分
	sb.show_score()
	
	#显示生命条
	sb.prep_health(char)
	
	#如果游戏是从开始菜单开始的，就绘制标题，绘制Play按钮，绘制Quit按钮
	if stats.menu_start_flag == False:
				
		myfont = pygame.font.Font(None, 70)
		textImage1 = pygame.image.load('images/bg1.bmp')
		screen.blit(textImage1, (0,0))
		textImage = myfont.render("Your Life", True, (158,220,240))
		screen.blit(textImage, (295, 100))
		
		play_button.draw_button()
		quit_button.draw_button()	
		pygame.mouse.set_visible(True)

	
	#如果游戏是从死亡界面开始的
	if stats.game_over_flag and stats.menu_start_flag and stats.game_active == False:
		play_button.draw_button()
		quit_button.draw_button()	
		pygame.mouse.set_visible(True)
		
		myfont = pygame.font.Font(None, 70)
		textImage = myfont.render("Game Over", True, (60,60,60))
		screen.blit(textImage, (275, 100))
		

	
	# # 让最近绘制的屏幕可见
	# pygame.display.flip()

def char_hit(ai_settings, screen, sb, stats, char, enemies, play_button, quit_button):
		
	if char.health > 0:
		char.health -= ai_settings.enemy_damage
		# #播放失去生命值音效
		# pygame.mixer.init()
		# sound = pygame.mixer.Sound('')
		# sound.play()
		
		
		# 更新记分牌
		sb.prep_health(char)

	#玩家死亡
	if char.health <= 0:
		stats.game_active = False
		stats.game_over_flag = True
		
		# #ME.播放游戏结束音效
		# pygame.mixer.music.stop()
		# pygame.mixer.init()
		# sound = pygame.mixer.Sound('')
		# sound.play()
		
def char_walking(screen, mysprite, char):
	
	framerate = pygame.time.Clock()
	group = pygame.sprite.Group()
	group.add(mysprite)
	framerate.tick(120)
		
	ticks = pygame.time.get_ticks()
			
	group.update(ticks)
	group.draw(screen)
	pygame.display.update()
