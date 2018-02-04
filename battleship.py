from random import randint

board = []

for i in range(5):
  board.append(['O'] * 5)


def print_board(board_in):
    for row in board:
        print ' '.join(row)

print_board(board)

def random_row(board_in):
  return randint(0, len(board_in) - 1)
  # or we could use return randint(0, 4)

def random_col(board_in):
  return randint(0, len(board_in) - 1)
	# or we could use return randint(0, 4)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input('Guess Row: '))
guess_col = int(raw_input("Guess Col: "))


if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
  board[guess_row][guess_col] = "X"
  print_board(board)

elif guess_col == 'X' and guess_row == 'X':
    print "You guessed that one already."

else:
  if guess_row not in range(5) or \
          guess_col not in range(5):
    print "Oops, that's not even in the ocean."
  else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
  print_board(board)