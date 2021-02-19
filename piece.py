import numpy

class Piece:

    def __init__(self, position, board, team):
        self.position = position        #tuple
        self.isDead = False
        self.isEndangered = False
        self.board = board
        self.team = team

    def moves(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def ValidMoves(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def isValidMove(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def willBeEaten(self, newPos):
        raise NotImplementedError("Subclass must implement abstract method")

    def update(self, position):                     #updating board as well
        self.board[self.position] = None
        self.position = position
        #self.isEndangered = self.willBeEaten(position)      #check if eaten on new position [FOR LATER]
        if self.board[position] is not None:
            self.board[position].isDead = True
        self.board[position] = self

    def testmove(self,position):
        self.name='%'
        self.position = position
        # self.isEndangered = self.willBeEaten(position)      #check if eaten on new position [FOR LATER]
        if self.board[position] is not None:
            self.board[position].isDead = True
        self.board[position] = self

class Pawn(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'P'

    def moves(self,turn):
        pass

class Knight(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'N'

    def moves(self):
        x = self.position[0]
        y = self.position[1]
        return [(x + i, y + j) for i in (-2, -1, 1, 2) for j in (-2, -1, 1, 2) if
                i != j and i != -j and 0 <= x + i < 8 and 0 <= y + j < 8]


class Bishop(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'B'

    def moves(self):
        x = self.position[0]
        y = self.position[1]
        return [(x + i, y + i) for i in range(1, 8) if 8 > x + i >= 0 and 8 > y + i >= 0] + \
               [(x - i, y - i) for i in range(1, 8) if 8 > x - i >= 0 and 8 > y - i >= 0] + \
               [(x + i, y - i) for i in range(1, 8) if 8 > x + i >= 0 and 8 > y - i >= 0] + \
               [(x - i, y + i) for i in range(1, 8) if 8 > x - i >= 0 and 8 > y + i >= 0]

class Rook(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'R'

    def moves(self):
        x = self.position[0]
        y = self.position[1]
        return [(x + i, y) for i in range(1, 8 - x)] + \
               [(x - i, y) for i in range(1, x + 1)] + \
               [(x, y + i) for i in range(1, 8 - y)] + \
               [(x, y - i) for i in range(1, y + 1)]


class King(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'K'

    def moves(self):
        x = self.position[0]
        y = self.position[1]
        return [(x + i, y) for i in (-1, 1) if 8 > x + i >= 0 and 8 > y >= 0] + \
               [(x, y + i) for i in (-1, 1) if 8 > x >= 0 and 8 > y + i >= 0] + \
               [(x + i, y + j) for i in (-1, 1) for j in (-1, 1) if 8 > x + i >= 0 and 8 > y + i >= 0]


class Queen(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'Q'

    def moves(self):
        return Rook.moves(self) + Bishop.moves(self)
