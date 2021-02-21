import numpy as np

class Piece:

    def __init__(self, position, board, team):
        self.position = position        #tuple
        self.isDead = False
        self.isEndangered = False
        self.board = board
        self.team = team
        self.decisions = np.array([[0] * 8] * 8, Piece)
        """
        1 = peut bouger
        0 = peut pas bouger
        2 = peut manger
        -1 = va se faire manger
        """
        self.directions = []

    def resetDecisions(self):
        self.decisions = np.array([[0] * 8] * 8, Piece)
        self.isEndangered = False

    def updateDecisions(self, continuous:bool = True):
        self.resetDecisions()
        x0, y0 = self.position
        for direction in self.directions:   #pour chaque direction
            movx, movy = direction
            while 8 > self.position[0] + movx >= 0 and 8 > self.position[1] + movy >= 0:    #on avance tant que ya pas de pièce
                x, y = self.position[0], self.position[1]
                newposition = (x + movx, y + movy)
                newpiece = self.board.board[newposition]
                if newpiece is None:                                     #then break when
                    for ennemy in self.board.teamsAlive[not self.team]:
                        self.position = newposition
                        if ennemy.decisions[newposition] != 0:              #if can move here
                            self.decisions[newposition] = -1
                        else:
                            self.decisions[newposition] = 1
                        #if self.board.moves[newposition] is not None:           #Daniel
                        #    self.board.moves[newposition].append(self)
                        #else:
                        #    self.board.moves[newposition] = self
                elif newpiece.team != self.team:
                    self.decisions[newposition] = 2             #if can eat
                    newpiece.isEndangered = True                #ennemy is endangered
                    break
                else:
                    break
                if not continuous:
                    break
            self.position = (x0, y0)

    def remove_moves(self, newpos):
        raise NotImplementedError("Subclass must implement abstract method")

    def isValidMove(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def willBeEaten(self, newPos):
        raise NotImplementedError("Subclass must implement abstract method")

    def update(self, position):                     #updating board as well
        self.board.board[self.position] = None
        self.position = position
        #self.isEndangered = self.willBeEaten(position)      #check if eaten on new position [FOR LATER]
        if self.board.board[position] is not None:
            self.board.board[position].isDead = True
        self.board.board[position] = self

    def eat(self, position):
        self.board.board[position].isDead = True

    def testmove(self, position):
        self.name='%'
        self.position = position
        # self.isEndangered = self.willBeEaten(position)      #check if eaten on new position [FOR LATER]
        if self.decisions[position] != 0:
            if self.decisions[position] == 2:
                self.eat(position)
            self.board.board[position] = self
        else:
            print("Zebi réfléchis")

class Pawn(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'P'

    def updateDecisions(self):
        pass

    #Override
    def ValidMoves(self):
        pass

class Knight(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'N'
        self.directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

    def updateDecisions(self):
        return super(Knight, self).updateDecisions(False)

    def remove_moves(self, newpos):
        L = self.board.updateDecisions
        for i in range(len(L)):
            for j in range(len(L[i])):
                try:
                    L[i][j].remove(self)
                except:
                    pass

    #Override
    def ValidMoves(self):
        pass

class Bishop(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'B'
        self.directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def updateDecisions(self):
        return super(Bishop, self).updateDecisions()

    def remove_moves(self, newpos):
        new, old = newpos, self.position
        delta = (new[0]-old[0], new[1]-old[1])
        if delta[0]*delta[1] > 0:
            directions = [(1, -1), (-1, 1)]

class Rook(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'R'
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def updateDecisions(self):
        return super(Rook, self).updateDecisions()

    def remove_moves(self):
        pass

    #[(x + i, y) for i in range(1, 8 - x)] + \
     #          [(x - i, y) for i in range(1, x + 1)] + \
    #           [(x, y + i) for i in range(1, 8 - y)] + \
    #          [(x, y - i) for i in range(1, y + 1)]


class King(Piece):
    def __init__(self, position, board, team):
        super().__init__(position, board, team)
        self.name = 'K'
        self.directions = [(-1,-1)]

    def updateDecisions(self):
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

    def updateDecisions(self):
        return super(Queen, self).updateDecisions()
