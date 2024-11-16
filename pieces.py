import pygame
from board import *
import numpy as np

class ChessPiece:
	def __init__(self,image_file_name, position):
		self.image = pygame.image.load(image_file_name)
		self.position=np.array(position)

	def draw(self,screen):
		screen.blit(self.image,(self.position[1]*SQUARE_SIZE,self.position[0]*SQUARE_SIZE))

	def possible_moves(self, piece_map):
		raise NotImplementedError(self)
	
	def move_to(self,new_position):
		self.position=new_position
	

class WhitePawn(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_pawn.svg",position)

	def possible_moves(self,piece_map):
		moves=[]

		#moveforward if the space is empty
		if piece_map[self.position[0]-1][self.position[1]]==0:
			moves+=[(self.position[0]-1,self.position[1])]

		#taek diagonally if the space is full
		if piece_map[self.position[0]-1][self.position[1]-1]<0:
			moves+=[(self.position[0]-1,self.position[1]-1)]
		if piece_map[self.position[0]-1][self.position[1]+1]<0:
			moves+=[(self.position[0]-1,self.position[1]+1)]
		return moves

class BlackPawn(ChessPiece):
	def __init__(self,position):
		super().__init__("images/black_pawn.svg",position)

class WhiteKing(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_king.svg",position)

class BlackKing(ChessPiece):
	def __init__(self,position):
		super().__init__("images/black_king.svg",position)

class WhiteQueen(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_queen.svg",position)

class BlackQueen(ChessPiece):
	def __init__(self,position):
		super().__init__("images/black_queen.svg",position)

class WhiteBishop(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_bishop.svg",position)

class BlackBishop(ChessPiece):
	def __init__(self,position):
		super().__init__("images/black_bishop.svg",position)

class WhiteKnight(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_knight.svg",position)

class BlackKnight(ChessPiece):
	def __init__(self,position):
		super().__init__("images/black_knight.svg",position)

class WhiteRook(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_rook.svg",position)

class BlackRook(ChessPiece):
	def __init__(self,position):
		super().__init__("images/black_rook.svg",position)


	