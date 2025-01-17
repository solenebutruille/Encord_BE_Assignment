from pieces.piece import Piece
from utils.constants import GRID_WIDTH

class Q(Piece):
    piece_type = "Q"

    def max_column(self):
        return GRID_WIDTH - 2
    
    def piece_shape(self):
        return [[0,0], [0, 1], [1, 0], [1,1]]

class Z(Piece):
    piece_type = "Z"
    def max_column(self):
        return GRID_WIDTH - 3
    
    def piece_shape(self):
        return [[0,1], [0, 2], [1, 0], [1,1]]
    
class S(Piece):
    piece_type = "S"

    def max_column(self):
        return GRID_WIDTH - 3
    
    def piece_shape(self):
        return [[0,0], [0, 1], [1, 1], [1,2]]

class T(Piece):
    piece_type = "T"

    def max_column(self):
        return GRID_WIDTH - 3
    
    def piece_shape(self):
        return [[0,1], [1, 0], [1, 1], [1,2]]

class I(Piece):
    piece_type = "I"

    def max_column(self):
        return GRID_WIDTH - 4
    
    def piece_shape(self):
        return [[0,0], [0, 1], [0, 2], [0,3]]
    
class L(Piece):
    piece_type = "L"

    def max_column(self):
        return GRID_WIDTH - 2
    
    def piece_shape(self):
        return [[0,0], [0, 1], [1, 0], [2,0]]
    
class J(Piece):
    def max_column(self):
        return GRID_WIDTH - 2
    
    def piece_shape(self):
        return [[0,0], [0, 1], [1, 1], [2,1]]