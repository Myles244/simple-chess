import pygame

BOARD_SIZE=800
SQUARE_SIZE=BOARD_SIZE/8

WHITE_SQUARE_COLOUR=(255, 220, 180)
BLACK_SQUARE_COLOUR=(100, 50, 20)

#function to draw a blanc chess board
def draw_chess_board(screen):
	for row in range(8):
		for col in range(8):
			square_colour = WHITE_SQUARE_COLOUR if (row+col)%2==0 else BLACK_SQUARE_COLOUR
			pygame.draw.rect(screen,square_colour,(col*SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))