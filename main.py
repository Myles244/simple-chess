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

#start the chess game
game=ChessGame()
white_to_move=True
highlighted_squares=[]

def refresh():
	#draws the checkerd chess board to the screen highlighting the selected square
	draw_chess_board(screen,highlighted_squares)

	#draws the pieces on the screen
	game.draw(screen)

	#flip() the display to put your work on screen
	pygame.display.flip()


def handle_click(highlighted_squares=highlighted_squares):

	#calculate which square the click was in
	square=tuple(np.flip(np.array(pygame.mouse.get_pos(),dtype=int)//SQUARE_SIZE).astype(int))

	global white_to_move

	#if they clicked on a previosly highlighted square, if it wasnt the same one they clicked on last time they made a move
	if square in highlighted_squares:
		if square != highlighted_squares[0]:
			game.move(white_to_move,highlighted_squares[0],square)
			highlighted_squares.clear()
			white_to_move = not white_to_move

	#if they clicked on an unhighlighted square, display the possible moves for that square
	else:
		highlighted_squares.clear()
		highlighted_squares += game.get_possible_moves(square,white_to_move)
	return

refresh()
while running:
	# poll for events
	# pygame.QUIT event means the user clicked X to close your window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			handle_click()
			refresh()

	clock.tick(60)  # limits FPS to 60

pygame.quit()
