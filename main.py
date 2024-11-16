# Example file showing a basic pygame "game loop"
import pygame
import numpy as np

from board import *
from pieces import *
from logic import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Simple Chess")

game=ChessGame()

selected_square=(8,8)

while running:
	
	# poll for events
	# pygame.QUIT event means the user clicked X to close your window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			selected_square=np.array(pygame.mouse.get_pos())//SQUARE_SIZE

	# fill the screen with a color to wipe away anything from last frame
	draw_chess_board(screen,selected_square)

	# RENDER YOUR GAME HERE
	game.draw(screen)

	# flip() the display to put your work on screen
	pygame.display.flip()

	clock.tick(60)  # limits FPS to 60

pygame.quit()
