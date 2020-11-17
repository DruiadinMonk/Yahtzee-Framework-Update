# Dice for rolling

# MODULES
import pygame
import random



# DICE CLASS
class Dice:

	# INITIALIZE
	def __init__(self, window, color, x, y, sq, number):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.sq = sq
		self.number = number


	# DRAW DICE: Hollow
	def draw(self):
		# DICE
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.sq, self.sq), 1)

		# NUMBER in center using 'Font'.
		font = pygame.font.SysFont(None, 72)
		num = font.render(str(self.number), True, self.color)
		self.window.blit(num, (self.x + 12, self.y + 2))

		# if self.number == 0:
		# 	draw '-'.


	# ROLL DICE
	def roll(self):
		# update 'self.number' with 'random'.
		self.number = random.randint(1, 6)
