import pygame
from copy import deepcopy

RED = (205, 83, 52)
WHITE = (233, 236, 239)

def minimax(position, depth, max_player, game, alpha, beta):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    # MaxNode
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max( alpha, maxEval)

            if beta <= alpha:
                break
            
            if maxEval == evaluation:
               best_move = move
            
        return maxEval, best_move

    # MinNode
    else: 
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game, alpha, beta)[0]
            maxEval = min(minEval, evaluation) 
            beta = min( beta, maxEval)

            if beta <= alpha:
                break
            if minEval == evaluation:
               best_move = move

        return maxEval, best_move

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)

        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves        

