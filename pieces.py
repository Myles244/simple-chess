import pygame
from board import *

class ChessPiece:
	def __init__(self,image_file_name, position):
		self.image = pygame.image.load(image_file_name)
		self.position=position

	def draw(self,screen):
		screen.blit(self.image,(self.position[0]*SQUARE_SIZE,self.position[1]*SQUARE_SIZE))

class WhitePawn(ChessPiece):
	def __init__(self,position):
		super().__init__("images/white_pawn.svg",position)

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


	