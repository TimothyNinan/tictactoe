"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if (terminal(board)):
        return 1
    
    numX = 0
    numO = 0

    for row in board:
        for item in row:
            if item == X:
                numX = numX + 1
            elif item == O:
                numO = numO + 1
    
    if numX > numO:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    if terminal(board):
        return 21
    
    moves = set()

    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                moves.add((i,j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise Exception("Invalid action. Board Terminal.")
    
    newBoard = deepcopy(board)

    i = action[0]
    j = action[1]

    if (newBoard[i][j] == EMPTY):
        newBoard[i][j] = player(newBoard)
        return newBoard
    else:
        raise Exception("Invalid move. Choose another spot.")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
