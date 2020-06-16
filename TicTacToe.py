# The TicTacToe excercise
# amedeo learning Python

import random


def display_board(board):  # display the board' game
    # this is really crap, need to do better later
    ncol = '      0    1    2'
    print(f"\n{ncol}")
    for nrow, row in zip(board_range, board):
        print(nrow, ' ', row)
    print()


def player_input(player, mark):  # collect user choice
    x = y = 'WRONG'
    # input_range
    while x.isdigit() == False or y.isdigit() == False:
        # TO DO handle no or 1 input to avoid crash
        while True:
            try:
                x, y = input(
                    f"Player {player} ({mark}) select a cell (2 digits in the range (0-2)): ").split()
                break
            except ValueError:
                print("Oops!   That was no valid number.  Try again...")

        # check data type input, waiting 2 digits
        if x.isdigit() == False or y.isdigit() == False:
            print("Input is not a cell (pair of digits")
        elif int(x) not in board_range:
            print(f"Cell coordonate {x} out of range {board_range}")
            x = 'WRONG'
        elif int(y) not in board_range:
            print(f"Cell coordonate {y} out of range {board_range}")
            y = 'WRONG'
        else:
            # check if the cell is empty
            x, y = int(x), int(y)
            if cell_is_empty(x, y):
                return x, y
            else:
                print(
                    f'The cell {x} {y} is not empty (content is {board[x][y]})')
                x = y = 'WRONG'


def cell_is_empty(x, y):
    return board[x][y] == '-'


def win_chek(board, mark):
    # the win mask string for the mark
    win_mask = mark * 3
    # check if there is a winner line or column
    for n in board_range:
        if win_mask == ''.join(board[n]) or win_mask == board[0][n] + board[1][n] + board[2][n]:
            return True

    # build 2 diagonals strings and check if there is a win
    d1 = d2 = ''
    for x in board_range:
        d1 += board[x][x]
        d2 += board[x][2-x]
    return win_mask == d1 or win_mask == d2


def player_mark_choice():
    mark = 'e'
    while True:
        mark = input('Please select the Player 1 marker: "X" or "O" > ')
        if mark == 'X':
            return 'X', 'O'
        elif mark == 'O':
            return 'O', 'X'


def ok_to_cont(what):
    msg = {'New': "Start a new game?", 'Continue': "Do you wanto to continue?"}

    # answer = input('Do you wanto to continue? [Y|n] > ')
    answer = input(f"{msg[what]} [Y|n] > ")
    # y|Y or no input are to continue
    return answer.upper() == 'Y' or answer == ''


def choose_first():
    # use random to decide who is going to play first
    return random.randint(1, 2)


#
# # --- main ---
#
msg = """\n  Welcome to Tic Tac Toe

Select the mark for player 1 and 2 between O and X.
Each player has to provide the cell coordonate
providing a pair of number in the range 0-2.\n"""

# start message
print(msg)
game_on = True

# main loop to repeat the game
while game_on:
    # let do some inits here
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    board_range = range(0, 3)
    player_mark = ['-', 'O', 'X']
    empty_cells = 9

    # Players' mark choice
    player_mark[1], player_mark[2] = player_mark_choice()
    print(f"Player 1 mark: {player_mark[1]} \nPlayer 2 mark: {player_mark[2]}")
    # who is going to play first?
    the_player = choose_first()
    print(
        f'Player {the_player} with mark {player_mark[the_player]} is going to start\n')
    # Ask if want continue and init game_on
    # game_on = True if players want continue and board is not full
    game_on = ok_to_cont('Continue')

    while game_on and empty_cells > 0:
        display_board(board)
        # get the cell
        x, y = player_input(the_player, player_mark[the_player])
        board[x][y] = player_mark[the_player]
        # check if winner choice
        if win_chek(board, player_mark[the_player]):
            display_board(board)
            print(f"\nPlayer {the_player} wins this game\n")
            break

        # flipflop player ...1>2>1>2...
        the_player = the_player % 2 + 1
        # decrease empty cells. If there is a winner
        # with last cell choice this will stay 1
        empty_cells -= 1
        game_on = ok_to_cont('Continue')

    if empty_cells == 0:
        print("\nNo winner - Game END\n")
        display_board(board)

    # Play again?
    game_on = ok_to_cont('New')
