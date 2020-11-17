# Score Card boxes to store values after each roll.

# MODULES
import pygame
import random



# SCORE CARD CLASS
class ScoreBox:


	# INITIALIZE
	def __init__(self, window, color, x, y, sq, number=0):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.sq = sq
		self.number = number 	# Init: 0 = Dash ('-').
		# self.text = text


	# DRAW SCORE CARD: Hollow
	def draw(self):
		# SCORECARD: Box
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.sq*2, self.sq), 1)

		# NUMBER in center using 'Font'.
		font = pygame.font.SysFont(None, 32)
		num = font.render(str(self.number), True, self.color)
		self.window.blit(num, (self.x + 25, self.y + 4))

		# # DRAW SECTION TEXT: Based off (x, y) of 
		# section = font.render(self.text, True, self.color)
		# self.window.blit(section, (self.x - 300, self.y + 4))


	# AFTER ROLL: Available places to mark off.
	def highlight(self):
		# update 'self.number' with 'random'.
		self.number = random.randint(1, 6)
