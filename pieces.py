import pygame
from board import *
import numpy as np

class ChessPiece:
	def __init__(self,image_file_name, position, is_white):
		self.image = pygame.image.load(image_file_name)
		self.position=np.array(position)
		self.is_white=is_white

	def draw(self,screen):
		screen.blit(self.image,(self.position[1]*SQUARE_SIZE,self.position[0]*SQUARE_SIZE))

	def possible_moves(self, piece_map):
		raise NotImplementedError(self)
	
	def move_to(self,new_position):
		self.position=new_position
	

class Pawn(ChessPiece):
	def __init__(self,position,is_white):
		if is_white:
			super().__init__("images/white_pawn.svg",position,is_white)
		else:
			super().__init__("images/black_pawn.svg",position,is_white)
		self.first_move=True

	def possible_moves(self,piece_map):

		moves=[]

		#white pieces move up ie in the negative one direction opposite is true for black pieces
		direction=1-2*self.is_white

		#move forward two if the space is empty and its my first move
		if self.first_move:
			if piece_map[self.position[0]+2*direction][self.position[1]]==0:
				moves+=[(self.position[0]+2*direction,self.position[1])]

		#moveforward if the space is empty
		if piece_map[self.position[0]+direction][self.position[1]]==0:
			moves+=[(self.position[0]+direction,self.position[1])]

		#take diagonally if the space has a peice of the oposite colour for white peice opsoite colours are negative ie direction*peicemap>0 same is true for blacks
		if direction*piece_map[self.position[0]+direction][self.position[1]-1]>0:
			moves+=[(self.position[0]+direction,self.position[1]-1)]
		if direction*piece_map[self.position[0]+direction][self.position[1]+1]>0:
			moves+=[(self.position[0]+direction,self.position[1]+1)]
		return moves
	
	def move_to(self, new_position):
		self.first_move=False
		return super().move_to(new_position)

class King(ChessPiece):
	def __init__(self,position,is_white):
		if is_white:
			super().__init__("images/white_king.svg",position,is_white)
		else:
			super().__init__("images/black_king.svg",position,is_white)

class Queen(ChessPiece):
	def __init__(self,position,is_white):
		if is_white:
			super().__init__("images/white_queen.svg",position,is_white)
		else:
			super().__init__("images/black_queen.svg",position,is_white)

class Bishop(ChessPiece):
	def __init__(self,position,is_white):
		if is_white:
			super().__init__("images/white_bishop.svg",position,is_white)
		else:
			super().__init__("images/black_bishop.svg",position,is_white)

class Knight(ChessPiece):
	def __init__(self,position,is_white):
		if is_white:
			super().__init__("images/white_knight.svg",position,is_white)
		else:
			super().__init__("images/black_knight.svg",position,is_white)

class Rook(ChessPiece):
	def __init__(self,position,is_white):
		if is_white:
			super().__init__("images/white_rook.svg",position,is_white)
		else:
			super().__init__("images/black_rook.svg",position,is_white)

	