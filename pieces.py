import pygame
from board import *
import numpy as np

class ChessPiece:
	def __init__(self,image_file_name, position, is_white,piece_type):
		self.image = pygame.image.load(image_file_name)
		self.position=np.array(position)
		self.is_white=is_white
		self.piece_type=piece_type

	def draw(self,screen):
		screen.blit(self.image,(self.position[1]*SQUARE_SIZE,self.position[0]*SQUARE_SIZE))

	def possible_moves(self, piece_map):
		raise NotImplementedError(self)
	
	def move_to(self,new_position):
		self.position=new_position
	

class Pawn(ChessPiece):
	def __init__(self,position,is_white):
		image_file_name="images/white_pawn.svg" if is_white else "images/black_pawn.svg"
		super().__init__(image_file_name,position,is_white,1)
		self.first_move=True

	def possible_moves(self,piece_map,pawn_in_movement):

		moves=[]

		#white pieces move up ie in the negative one direction opposite is true for black pieces
		direction=1-2*self.is_white

		#if thier is room
		if self.position[0]+direction<=7 and self.position[0]+direction>=0:

			#move forward two if the space is empty and its my first move
			if self.first_move:
				if piece_map[self.position[0]+2*direction][self.position[1]]==0:
					moves+=[(self.position[0]+2*direction,self.position[1])]

			#moveforward if the space is empty
			if piece_map[self.position[0]+direction][self.position[1]]==0:
				moves+=[(self.position[0]+direction,self.position[1])]

			#take diagonally if the space has a peice of the oposite colour for white peice opsoite colours are negative ie direction*peicemap>0 same is true for blacks
			#also check for enpausant
			if self.position[1]>=1:
				if direction*piece_map[self.position[0]+direction][self.position[1]-1]>0 or (self.position[0]+direction==pawn_in_movement[0][0] and self.position[1]-1==pawn_in_movement[0][1]):
					moves+=[(self.position[0]+direction,self.position[1]-1)]

			if self.position[1]<=6:
				if direction*piece_map[self.position[0]+direction][self.position[1]+1]>0  or (self.position[0]+direction==pawn_in_movement[0][0] and self.position[1]+1==pawn_in_movement[0][1]):
					moves+=[(self.position[0]+direction,self.position[1]+1)]
			


		return moves
	
	def move_to(self, new_position):
		self.first_move=False
		return super().move_to(new_position)

class King(ChessPiece):
	def __init__(self,position,is_white):
		image_file_name="images/white_king.svg" if is_white else "images/black_king.svg"
		super().__init__(image_file_name,position,is_white,6)

class Queen(ChessPiece):
	def __init__(self,position,is_white):
		image_file_name="images/white_queen.svg" if is_white else "images/black_queen.svg"
		super().__init__(image_file_name,position,is_white,5)

class Bishop(ChessPiece):
	def __init__(self,position,is_white):
		image_file_name="images/white_bishop.svg" if is_white else "images/black_bishop.svg"
		super().__init__(image_file_name,position,is_white,2)

class Knight(ChessPiece):
	def __init__(self,position,is_white):
		image_file_name="images/white_knight.svg" if is_white else "images/black_knight.svg"
		super().__init__(image_file_name,position,is_white,3)

class Rook(ChessPiece):
	def __init__(self,position,is_white):
		image_file_name="images/white_rook.svg" if is_white else "images/black_rook.svg"
		super().__init__(image_file_name,position,is_white,4)

	