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
        res = []
        for i in range(4):
            if

class Bishop(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'B'

#Daniel
class Rook(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'R'

class King(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'K'

class Queen(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'Q'

