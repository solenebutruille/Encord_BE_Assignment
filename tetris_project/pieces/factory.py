from pieces.pieces import Q, Z, S, T, I, L, J

def create_piece(piece_type, piece_column):
    if piece_type == "Q":
        return Q(piece_column)
    elif piece_type == "Z":
        return Z(piece_column)
    elif piece_type == "S":
        return S(piece_column)
    elif piece_type == "T":
        return T(piece_column)
    elif piece_type == "I":
        return I(piece_column)
    elif piece_type == "L":
        return L(piece_column)
    elif piece_type == "J":
        return J(piece_column)
    else:
        raise ValueError(f"Unknown piece type: {piece_type}")