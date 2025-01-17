import sys
from game.tetris import Tetris
from pieces.factory import create_piece

for input in sys.stdin:

    pieces = input.split(",")
    tetris_game = Tetris()

    try:
        for piece in pieces:
            piece_type = piece[0]
            piece_column = int(piece[1])

            p = create_piece(piece_type, piece_column)

            tetris_game.add_piece(p)
        
        print(tetris_game.get_grid_height())
    #    for row in reversed(tetris_game.grid):
    #        print(row)

    except Exception as e:
        print(f"An error occurred: {e}")