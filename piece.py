import numpy

class Piece:

    def __init__(self, position, board, team):
        self.position = position        #tuple
        self.isDead = False
        self.isEndangered = False
        self.board = board
        self.team = team
        self.eat = []

    def moves(self):
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
        self.eat = []
        moves = []
        x0, y0 = self.position

        for direction in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]:
            movx, movy = direction
            if 8 > self.position[0] + movx >= 0 and 8 > self.position[1] + movy >= 0:
                x, y = self.position[0], self.position[1]
                newposition = (x + movx, y + movy)

                if self.board[newposition] is None:
                    self.position = newposition
                    moves.append(newposition)
                elif self.board[newposition].team != self.team:
                    self.eat.append(self.board[newposition])
                    moves.append(newposition)
                    break
                else:
                    break
            self.position = (x0, y0)
        return moves

    #Override
    def ValidMoves(self):
        pass

class Bishop(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'B'

    def moves(self):
        self.eat = []  # reset canEat
        moves = []
        x0, y0 = self.position

        for direction in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            movx, movy = direction
            while 8 > self.position[0] + movx >= 0 and 8 > self.position[1] + movy >= 0:
                x, y = self.position[0], self.position[1]
                newposition = (x + movx, y + movy)

                if self.board[newposition] is None:
                    self.position = newposition
                    moves.append(newposition)
                elif self.board[newposition].team != self.team:
                    self.eat.append(self.board[newposition])
                    moves.append(newposition)
                    break
                else:
                    break
            self.position = (x0, y0)
        return moves

class Rook(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'R'

    def moves(self):
        self.eat=[]                             #reset canEat
        moves = []
        x0, y0 = self.position

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:                        #pour chaque direction
            movx, movy = direction                                              #on avance tant que ya pas de pièce
            while 8 > self.position[0]+movx >= 0 and 8 > self.position[1]+movy >= 0:          #puis break quand
                x, y = self.position[0], self.position[1]                                   # on rencontre obstacle
                newposition = (x+movx, y+movy)                                          #(qu'on peut manger ou non)

                if self.board[newposition] is None:
                    self.position = newposition
                    moves.append(newposition)
                elif self.board[newposition].team != self.team:
                    self.eat.append(self.board[newposition])
                    moves.append(newposition)
                    break
                else:
                    break
            self.position = (x0, y0)
        return moves

    #[(x + i, y) for i in range(1, 8 - x)] + \
     #          [(x - i, y) for i in range(1, x + 1)] + \
    #           [(x, y + i) for i in range(1, 8 - y)] + \
    #          [(x, y - i) for i in range(1, y + 1)]


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
        self.eat = []
        moves = []
        x0, y0 = self.position

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            movx, movy = direction
            while 8 > self.position[0] + movx >= 0 and 8 > self.position[1] + movy >= 0:
                x, y = self.position[0], self.position[1]
                newposition = (x + movx, y + movy)

                if self.board[newposition] is None:
                    self.position = newposition
                    moves.append(newposition)
                elif self.board[newposition].team != self.team:
                    self.eat.append(self.board[newposition])
                    moves.append(newposition)
                    break
                else:
                    break
            self.position = (x0, y0)
        return moves
