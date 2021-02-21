import numpy as np
from piece import *


class Board:
    def __init__(self):
        self.board = np.array([[None] * 8] * 8, Piece)
        #self.moves = np.array([[None]*8]*8, list(Piece))
        self.teamsAlive = [[], []]

    def init(self):
        for i in range(8):
            self.board[1][i] = Pawn((1, i), self, 1)
            self.board[6][i] = Pawn((6, i), self, 0)
        self.board[0][0] = Rook((0, 0), self, 1)
        self.board[7][0] = Rook((7, 0), self, 0)
        self.board[0][7] = Rook((0, 7), self, 1)
        self.board[7][7] = Rook((7, 7), self, 0)
        self.board[0][1] = Knight((0, 1), self, 1)
        self.board[7][1] = Knight((7, 1), self, 0)
        self.board[0][6] = Knight((0, 6), self, 1)
        self.board[7][6] = Knight((7, 6), self, 0)
        self.board[0][2] = Bishop((0, 2), self, 1)
        self.board[7][2] = Bishop((7, 2), self, 0)
        self.board[0][5] = Bishop((0, 5), self, 1)
        self.board[7][5] = Bishop((7, 5), self, 0)
        self.board[0][4] = King((0, 4), self, 1)
        self.board[7][4] = King((7, 4), self, 0)
        self.board[0][3] = Queen((0, 3), self, 1)
        self.board[7][3] = Queen((7, 3), self, 0)

        for i in [0,1,6,7]:
            for piece in self.board[i]:
                self.teamsAlive[piece.team].append(piece)
        return self

    def show(self):
        for line in self.board:
            print([piece.name + ('b' if piece.team == 0 else 'w') if piece is not None else "__" for piece in line])

    def who(self,position):
        return self.board[position]
