from random import randint

board = []

for i in range(5):
  board.append(['O'] * 5)


def print_board(board_in):
    for row in board:
        print ' '.join(row)


def random_row(board_in):
  return randint(0, len(board_in) - 1)
  # or we could use return randint(0, 4)

def random_col(board_in):
  return randint(0, len(board_in) - 1)
	# or we could use return randint(0, 4)

random_row(board)
random_col(board)

print_board(board)