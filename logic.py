from board import *
from pieces import *
import numpy as np

class ChessGame:
	def __init__(self,white=True):

		#store the pieces in a list
		self.white_pieces = []
		self.black_pieces = []

		#the pawns
		for i in range(8):
			self.white_pieces.append(WhitePawn((i,1+5*white)))
			self.black_pieces.append(BlackPawn((i,6-5*white)))

		#the kings
		self.white_pieces.append(WhiteKing((4,7*white)))
		self.black_pieces.append(BlackKing((4,7-7*white)))

		#the queens
		self.white_pieces.append(WhiteQueen((3,7*white)))
		self.black_pieces.append(BlackQueen((3,7-7*white)))

		#the bishops
		self.white_pieces.append(WhiteBishop((2,7*white)))
		self.white_pieces.append(WhiteBishop((5,7*white)))
		self.black_pieces.append(BlackBishop((2,7-7*white)))
		self.black_pieces.append(BlackBishop((5,7-7*white)))

		#the knights
		self.white_pieces.append(WhiteKnight((1,7*white)))
		self.white_pieces.append(WhiteKnight((6,7*white)))
		self.black_pieces.append(BlackKnight((1,7-7*white)))
		self.black_pieces.append(BlackKnight((6,7-7*white)))

		#the rooks
		self.white_pieces.append(WhiteRook((0,7*white)))
		self.white_pieces.append(WhiteRook((7,7*white)))
		self.black_pieces.append(BlackRook((0,7-7*white)))
		self.black_pieces.append(BlackRook((7,7-7*white)))

	#draw the pieces on the creen
	def draw(self,screen):
		for piece in self.white_pieces:
			piece.draw(screen)
		for piece in self.black_pieces:
			piece.draw(screen)