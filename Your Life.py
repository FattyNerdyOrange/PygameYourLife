import pygame
from settings import Settings
import game_functions as gf
from char import *
from bg import *
from mouse import * 
from enemy import *
from pygame.sprite import Group
from scoreboard import Scoreboard
from button import *
from game_stats import *

# from timeclock import *

def run_game():
	

	pygame.init()   
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Your Life")
	
	#设置背景图片
	background=Bg(ai_settings, screen)
	
	#鼠标设置为准心
	aim=Mouse(ai_settings, screen)

	#创建主角
	char = Char(ai_settings, screen)
	mysprite = MySprite(screen, char)
	
	
	#创建敌人
	enemies = Group() 
	
	# #创建计时器
	# timer = Timeclock()
	
	# 创建Play按钮
	play_button = Play_Button(ai_settings, screen, "Play")
	
	# 创建Quit按钮
	quit_button = Quit_Button(ai_settings, screen, "Quit")
	
	# 创建存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)	
	sb = Scoreboard(ai_settings, screen, stats, char)	
	
	#添加背景音乐循环播放
	pygame.mixer.music.load('music/game_over.wav')
	pygame.mixer.music.play(-1, 0.0)
	while True:
		
		gf.check_events(ai_settings, screen, char, stats, sb, play_button, quit_button, background, enemies)
		gf.update_screen(ai_settings, screen, stats, sb, play_button, quit_button, aim, background, char, enemies)
				
			
		if stats.game_active:	
			gf.update_enemies(ai_settings, screen, sb, stats, char, background, enemies,  play_button, quit_button)
			
			#不同阶段玩家形态不同，敌人也不同
			if background.bg_x >-400 and background.bg_x<=0:
				
				#添加文字说明
				myfont = pygame.font.Font(None,100)
				myfont.set_underline(True)
				myfont.set_bold(True)
				textImage= myfont.render("babyhood", True, (255,255,0))
				screen.blit(textImage, (210,100))
				
				#更新主角
				char.update_default(screen, background)
				mysprite.update_stage1(char)
				mysprite.load("images/baby_72x36x3.png", 72, 36, 3) 
				gf.char_walking(screen, mysprite, char)
				
			elif background.bg_x <-400 and background.bg_x >-1200:
				
				#添加文字说明
				myfont = pygame.font.Font(None, 100)
				myfont.set_underline(True)
				myfont.set_bold(True)
				textImage= myfont.render("childhood", True, (255,255,0))
				screen.blit(textImage, (210,100))
				
				#更新敌人图片
				for enemy in enemies :
					enemy.image = pygame.image.load('images/duck.png').convert_alpha()
				
				#更新主角图片
				char.update_stage1(screen, background)
				mysprite.update_stage1(char)
				mysprite.load("images/child_48x72x4.png", 48, 72, 4)
				gf.char_walking(screen, mysprite, char)
			
			elif background.bg_x <-1200 and background.bg_x >-2000:
				
				#添加文字说明
				myfont = pygame.font.Font(None, 100)
				myfont.set_underline(True)
				myfont.set_bold(True)
				textImage= myfont.render("youth", True, (255,255,0))
				screen.blit(textImage, (280,100))
				
				for enemy in enemies :
					enemy.image = pygame.image.load('images/mathbook.png').convert_alpha()				
				
				char.update_stage2(screen, background)
				mysprite.update_stage1(char)
				mysprite.load("images/teenager_48x112x4.png", 48, 112, 4)
				gf.char_walking(screen, mysprite, char)			
			
			elif background.bg_x <-2000 and background.bg_x >-2800:
				
				#添加文字说明
				myfont = pygame.font.Font(None, 100)
				myfont.set_underline(True)
				myfont.set_bold(True)
				textImage= myfont.render("middle age", True, (255,255,0))
				screen.blit(textImage, (210,100))
				
				for enemy in enemies :
					enemy.image = pygame.image.load('images/paperclip.png').convert_alpha()			
			
				char.update_stage3(screen, background)
				char.blitme()
				
			elif background.bg_x <-2800 and background.bg_x >-3600:
				#添加文字说明
				myfont = pygame.font.Font(None, 100)
				myfont.set_underline(True)
				myfont.set_bold(True)
				textImage= myfont.render("old age", True, (255,255,0))
				screen.blit(textImage, (280,100))
				
				for enemy in enemies :
					enemy.image = pygame.image.load('images/drug.png').convert_alpha()			
				
				char.update_stage4(screen, background)
				mysprite.update_stage1(char)
				mysprite.load("images/bold_48x96x2.png", 48, 96, 2)
				gf.char_walking(screen, mysprite, char)			
			
			elif background.bg_x <-3600 and background.bg_x >-4800:
				
				for enemy in enemies :
					enemy.image = pygame.image.load('images/star.png').convert_alpha()				
				
				char.update_stage5(screen, background)
				char.blitme()
				#添加文字，创建对象
				myfont = pygame.font.Font(None, 50)
				#修饰文字
				myfont.set_underline(True)	
				myfont.set_bold(True)
				myfont.set_italic(True)
				
				textImage1 = myfont.render("Congratulations!", True, (144,238,0))
				textImage2 = myfont.render("You have gone through your entire life!", True, (144,238,0))
				textImage3 = myfont.render("Thanks for playing!", True, (144,238,0))
			
				screen.blit(textImage1, (220,100))
				screen.blit(textImage2, (30,150))
				screen.blit(textImage3, (220,200))
				
				#虽然玩家还可以移动，并且敌人继续掉落，但游戏结束了，即便你继续射击敌人也不会有分数，玩家也不会死亡
				ai_settings.enemy_points = 0
				ai_settings.enemy_damage = 0
				
							
		pygame.display.update()
		
run_game()
