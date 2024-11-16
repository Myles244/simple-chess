from board import *
from pieces import *
import numpy as np

class ChessGame:
	def __init__(self):

		#a 2d array of the piece at each square in the board
		self.piece_map=[
			[-4,-3,-2,-5,-6,-2,-3,-4],
			[-1,-1,-1,-1,-1,-1,-1,-1],
			[ 0, 0, 0, 0, 0, 0, 0, 0],
			[ 0, 0, 0, 0, 0, 0, 0, 0],
			[ 0, 0, 0, 0, 0, 0, 0, 0],
			[ 0, 0, 0, 0, 0, 0, 0, 0],
			[ 1, 1, 1, 1, 1, 1, 1, 1],
			[ 4, 3, 2, 5, 6, 2, 3, 4]
			]

		#store the pieces in a list
		self.white_pieces = []
		self.black_pieces = []

		#the pawns
		for i in range(8):
			self.white_pieces.append(WhitePawn((6,i)))
			self.black_pieces.append(BlackPawn((1,i)))

		#the kings
		self.white_pieces.append(WhiteKing((7,3)))
		self.black_pieces.append(BlackKing((0,3)))

		#the queens
		self.white_pieces.append(WhiteQueen((7,4)))
		self.black_pieces.append(BlackQueen((0,4)))

		#the bishops
		self.white_pieces.append(WhiteBishop((7,2)))
		self.white_pieces.append(WhiteBishop((7,5)))
		self.black_pieces.append(BlackBishop((0,2)))
		self.black_pieces.append(BlackBishop((0,5)))

		#the knights
		self.white_pieces.append(WhiteKnight((7,1)))
		self.white_pieces.append(WhiteKnight((7,6)))
		self.black_pieces.append(BlackKnight((0,1)))
		self.black_pieces.append(BlackKnight((0,6)))

		#the rooks
		self.white_pieces.append(WhiteRook((7,0)))
		self.white_pieces.append(WhiteRook((7,7)))
		self.black_pieces.append(BlackRook((0,0)))
		self.black_pieces.append(BlackRook((0,7)))

	#draw the pieces on the creen
	def draw(self,screen):
		for piece in self.white_pieces:
			piece.draw(screen)
		for piece in self.black_pieces:
			piece.draw(screen)

	#return a list of possible moves for the piece at a give square including itslef
	def get_possible_moves(self,square,white_to_move):
		if white_to_move:
			for piece in self.white_pieces:
				if np.all(piece.position == square):
					return [square]+piece.possible_moves(self.piece_map)
		else:
			for piece in self.black_pieces:
				if np.all(piece.position == square):
					return [square]+piece.possible_moves(self.piece_map)
		return []
	
	#move the piece at the start position if it exists to the end position
	def move(self, white_to_move,start_position, end_position):
		
		#remove piece if their is one being taken
		if self.piece_map[end_position[0]][end_position[1]]!=0:
			if white_to_move:
				for piece in self.black_pieces:
					if np.all(piece.position == end_position):
						self.black_pieces.remove(piece)
			else:
				for piece in self.white_pieces:
					if np.all(piece.position == end_position):
						self.white_pieces.remove(piece)

		#update piece map
		self.piece_map[end_position[0]][end_position[1]]=self.piece_map[start_position[0]][start_position[1]]

		#move the piece
		if white_to_move:
			for piece in self.white_pieces:
				if np.all(piece.position == start_position):
					piece.move_to(end_position)
		else:
			for piece in self.black_pieces:
				if np.all(piece.position == start_position):
					piece.move_to(end_position)
		