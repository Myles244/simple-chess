# Example file showing a basic pygame "game loop"
import pygame
from graphics import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Simple Chess")

while running:
	
	# poll for events
	# pygame.QUIT event means the user clicked X to close your window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# fill the screen with a color to wipe away anything from last frame
	draw_chess_board(screen)

	# RENDER YOUR GAME HERE

	# flip() the display to put your work on screen
	pygame.display.flip()

	clock.tick(60)  # limits FPS to 60

pygame.quit()
