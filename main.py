from board import *
import numpy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #init board
    b=Board()
    b.init()
    #piece test
    testpiece=b.board[0,3]

    # change board
    b.board[1][3] = None
    b.board[1][2] = None
    b.show()

    print("\n")

    print(testpiece.moves())

    #move possible
    for move in testpiece.moves():
        testpiece.testmove(move)
    b.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def convert(string):
    if (2 >= len(string) >= 1) and (string[0].upper() in 'ABCDEFH') and (1<=string[1]<=8) :
        return [ord(string[0].upper())-65, int(string[1])-1]
    else:
        print('Pas bon')

