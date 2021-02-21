import numpy

class Piece:

    def __init__(self, position, board, team):
        self.position = position        #tuple
        self.isDead = False
        self.isEndangered = False
        self.board = board
        self.team = team
        self.eat = []
        self.directions = []

    def moves(self, continuous:bool = True):
        self.eat = []   # reset canEat
        moves = []
        x0, y0 = self.position
        for direction in self.directions:   #pour chaque direction
            movx, movy = direction
            while 8 > self.position[0] + movx >= 0 and 8 > self.position[1] + movy >= 0:    #on avance tant que ya pas de pièce
                x, y = self.position[0], self.position[1]
                newposition = (x + movx, y + movy)

                if self.board[newposition] is None:     #then break when
                    self.position = newposition
                    moves.append(newposition)      # meeting an obstacle
                elif self.board[newposition].team != self.team:
                    self.eat.append(self.board[newposition])       #(either we can eat or not)
                    moves.append(newposition)
                    break
                else:
                    break
                if not continuous:
                    break
            self.position = (x0, y0)
        return moves

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

    def testmove(self, position):
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

    #Override
    def ValidMoves(self):
        pass

class Knight(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'N'
        self.directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

    def moves(self):
        return super(Knight, self).moves(False)

    #Override
    def ValidMoves(self):
        pass

class Bishop(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'B'
        self.directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def moves(self):
        return super(Bishop, self).moves()

class Rook(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'R'
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def moves(self):
        return super(Rook, self).moves()

    #[(x + i, y) for i in range(1, 8 - x)] + \
     #          [(x - i, y) for i in range(1, x + 1)] + \
    #           [(x, y + i) for i in range(1, 8 - y)] + \
    #          [(x, y - i) for i in range(1, y + 1)]


class King(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'K'
        self.directions = [(-1,-1)]

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
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def moves(self):
        return super(Queen, self).moves()
