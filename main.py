# Yahtzee Game

# MODULES
import pygame
import random
import sys
from dice import Dice
from scorebox import ScoreBox



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 400, 700
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption('Yahtzee')
font = pygame.font.SysFont(None, 28) 				# Font
clock = pygame.time.Clock()
run = True
FPS = 60
stored_value = 0 		# If == 0, then you can reroll, else, store value in scorebox box.




# COLORS
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255, 127, 127)



# INITIALIZE OBJECTS
# Dice: Initial value = 0
dice_list = []
x = 50
y = 625
sq = 50
for i in range(5):
	d = Dice(window, WHITE, x, y, sq, 0)
	dice_list.append(d)
	x += 60


# LIST OF ALL TEXT:
text_list = []

t0 = font.render("UPPER SECTION (3 Minimum)", True, WHITE)
t1 = font.render("ACES: Count ONLY Aces (Ones)", True, WHITE)
t2 = font.render("TWOS: Count ONLY Twos", True, WHITE)
t3 = font.render("THREES: Count ONLY Threes", True, WHITE)
t4 = font.render("FOURS: Count ONLY Fours", True, WHITE)
t5 = font.render("FIVES: Count ONLY Fives", True, WHITE)
t6 = font.render("SIXES: Count ONLY Sixes", True, WHITE)
t7 = font.render("BONUS (if == 63, then += 35)", True, WHITE)
t8 = font.render("TOTAL", True, WHITE)
t9 = font.render("LOWER SECTION", True, WHITE)
t10 = font.render("3 of a Kind: (Total all dice)", True, WHITE)
t11 = font.render("4 of a kind: (Total all dice)", True, WHITE)
t12 = font.render("Full House: Score = 25", True, WHITE)
t13 = font.render("Low Straight: Score = 30", True, WHITE)
t14 = font.render("High Straight: Score = 40", True, WHITE)
t15 = font.render("Chance: Total ALL dice", True, WHITE)
t16 = font.render("GRAND TOTAL:", True, WHITE)

text_list.append(t0)
text_list.append(t1)
text_list.append(t2)
text_list.append(t3)
text_list.append(t4)
text_list.append(t5)
text_list.append(t6)
text_list.append(t7)
text_list.append(t8)
text_list.append(t9)
text_list.append(t10)
text_list.append(t11)
text_list.append(t12)
text_list.append(t13)
text_list.append(t14)
text_list.append(t15)
text_list.append(t16)

# Score Card = Two sections...clickable boxes and static text box to the left.
# 6 Upper / 8 Lower / 14 Total clickable boxes
scorebox_list = []


"""
What needs to be omitted from 'scorebox_list[]' is...

	UPPER: Bonus
	UPPER: Total

	LOWER: Grand Total


	Fill square WHITE when you can play there.
		if dice[0] -> dice[4] == '1' -> '6', then YAHTZEE
			thus, fill square white.
			I may be able to do this inside of 'scorebox.py' instead of main,
				as each box holds that function.

"""







x = 325
y = 40
sq = 30

# UPPER: Main
for i in range(8):
	s = ScoreBox(window, WHITE, x, y, sq)
	scorebox_list.append(s)

	y += 30

# UPPER: Bonus
s = ScoreBox(window, WHITE, 325, 195, sq)

# LOWER
y = 310
for i in range(7):
	s = ScoreBox(window, WHITE, x, y, sq)
	scorebox_list.append(s)
	y += 30



# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS)
	window.fill(0)
	MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
	pygame.draw.rect(window, RED, (167, 542, 66, 66)) 	# BIG RED BUTTON


	# FOR EACH EVENT...
	for event in pygame.event.get():
		# IF QUIT...
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	
		# ROLL: If transfered value OR new game.
		if stored_value == 0:

			# BUTTON: If clicked on button... 		# Q: ROLL DICE: Q: How do I do this with SPACEBAR, rather than MOUSEBUTTONDOWN?
			if 167 <= MOUSE_X <= 233 and 542 <= MOUSE_Y <= 608 and event.type == pygame.MOUSEBUTTONDOWN:

				# RESET DICE TOTAL, before rolling.
				dice_total 	= 0

				# Roll the 5 dice.
				for i in range(len(dice_list)):

					# ROLL: Dice
					dice_list[i].roll()

					# ADD: Die roll to total value.
					dice_total += dice_list[i].number

				# STORE VALUE: Once stored value is transfered to a box, we may reroll again.
				stored_value = dice_total

		# If stored_value != 0, transfer the value to a scorebox box.
		else:

			# CHECK: scorebox_list[]
			for i in range(len(scorebox_list)):

				# If mouse on a scorebox box AND clicked AND OPEN box...
				if scorebox_list[i].x <= MOUSE_X <= scorebox_list[i].x+60 and scorebox_list[i].y < MOUSE_Y < scorebox_list[i].y+30:
					if event.type == pygame.MOUSEBUTTONDOWN:
						if scorebox_list[i].number == 0:

						# CHECK: If mouse is over a box that is EMPTY.
						# If mouse OVER box...

							# THEN: Put value IN scorebox box.
							scorebox_list[i].number = stored_value

							# RESET: After transfering value over.
							stored_value = 0

							# Interupt loop AFTER we select a scorebox box.
							break


	# DRAW ALL TEXT
	x = y = 15
	for i in range(len(text_list)):
		window.blit(text_list[i], (x, y))

		y += 30

	# DRAW SCOREBOX
	for i in range(len(scorebox_list)):
		scorebox_list[i].draw()

	# DRAW DICE
	for i in range(len(dice_list)):
		dice_list[i].draw()


	# UPDATE: Pygame
	pygame.display.update()
