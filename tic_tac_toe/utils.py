import re
import random


PLAYER_X = 'x'
PLAYER_O = 'o'


class BoardNotValidException(Exception):
    pass


def board_is_valid(board):
    is_valid = False
    if type(board) is str and re.match('^[xo ]{9}$', board):
        is_valid = True
    return is_valid


def play(index, board):
    board_list = list(board)
    board_list[index] = PLAYER_O  # player is always 'o'
    return ''.join(board_list)


def get_played_indexes(player, board):
    """Get indexes of played positions of a player."""
    indexes = []
    for counter, value in enumerate(list(board)):
        if value == player:
            indexes.append(counter)
    return set(indexes)


def get_unplayed_indexes(board):
    indexes = []
    for counter, value in enumerate(list(board)):
        if value == ' ':
            indexes.append(counter)
    return set(indexes)


def game_won(player, board):
    win_groups = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    )
    won = False
    for tup in win_groups:
        if set(tup).issubset(get_played_indexes(player, board)):
            won = True
            break
    return won
    

def compute_move(board):
    if not board_is_valid(board):
        raise BoardNotValidException()
    unplayed_indexes = get_unplayed_indexes(board)
    if len(unplayed_indexes) > 0:
        # TODO: calculate optimal move, return best index
        index = random.choice(list(unplayed_indexes))
        new_board = play(index, board)
    else:
        # Its a tie
        new_board = board
    # check if win, draw or lose
    return new_board
