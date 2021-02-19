class Piece:

    def __init__(self, position, board, team):
        self.position = position
        self.isDead = False
        self.isEndangered = False
        self.board = board
        self.team = team

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def ValidMoves(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def isValidMove(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def willBeEaten(self, newPos):
        raise NotImplementedError("Subclass must implement abstract method")

    def update(self, position):
        self.position=position
        self.isEndangered=self.willBeEaten(position)
        if self.board.someone(position) is not None:
            self.board.someone(position).isDead = True

class Pawn(Piece):
    def __init__(self,position, board, team):
        super().__init__(position, board, team)
        self.name = 'P'

class Knight(Piece):                      #Quentin
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'N'

    def move(self):
        res=[]
        x = self.position[0]
        y = self.position[1]
        return [[x + i, x + j] for i in (-2, -1, 1, 2) for j in (-2, -1, 1, 2) if i != 2 and j != 2 and 0 <= x + i < 8 and 0 <= x + j < 8]


class Bishop(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'B'

    def move(self):
        x = self.position[0]
        y = self.position[1]
        return [[x + i, y + i] for i in range(1, 8) if 8>x+i>=0 and 8>y+i>=0] + \
               [[x - i, y - i] for i in range(1, 8) if 8>x-i>=0 and 8>y-i>=0] + \
               [[x + i, y - i] for i in range(1, 8) if 8>x+i>=0 and 8>y-i>=0] + \
               [[x - i, y + i] for i in range(1, 8) if 8>x-i>=0 and 8>y+i>=0]


#Daniel
class Rook(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'R'

    def move(self):
        x = self.position[0]
        y = self.position[1]
        return [[x+i, y] for i in range(1, 8-x)] + \
               [[x-i, y] for i in range(1, x+1)] + \
               [[x, y+i] for i in range(1, 8-y)] + \
               [[x, y-i] for i in range(1, y+1)]

class King(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'K'

    def move(self):
        x = self.position[0]
        y = self.position[1]
        return [[x+i, y] for i in (-1,1)] + \
               [[x, y+i] for i in (-1,1)] + \
               [[x+i, y+j] for i in (-1,1) for j in (-1,1)]

class Queen(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'Q'

    def move(self):
        return Rook.move() + Bishop.move()

