import random

HIDDEN = "?"
REVEALED_EMPTY = "O"
REVEALED_BOMB = "X"
FLAGGED = "F"

def generate_bomb_location():
  row = random.randint(0, 2)
  col = random.randint(0, 2)
  return row, col

def initialize_board():
  board = []
  for _ in range(3):
    row = [HIDDEN for _ in range(3)]
    board.append(row)
  return board

def is_valid_cell(row, col):
  return 0 <= row < 3 and 0 <= col < 3

def reveal_cell(board, row, col, bomb_row, bomb_col):
  if not is_valid_cell(row, col):
    return

  if board[row][col] != HIDDEN and board[row][col] != FLAGGED:
    return

  if row == bomb_row and col == bomb_col:
    board[row][col] = REVEALED_BOMB
    return

  adjacent_bombs = 0
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if is_valid_cell(i, j) and (i, j) != (row, col) and board[i][j] == REVEALED_BOMB:
        adjacent_bombs += 1

  board[row][col] = str(adjacent_bombs) if adjacent_bombs > 0 else REVEALED_EMPTY
  if adjacent_bombs == 0:
    for i in range(row - 1, row + 2):
      for j in range(col - 1, col + 2):
        reveal_cell(board, i, j, bomb_row, bomb_col)

def display_board(board):
  for row in board:
    print(" ".join(row))

def is_game_won(board):
  for row in board:
    for cell in row:
      if cell == HIDDEN:
        return False
  return True

def is_game_lost(board):
  for row in board:
    for cell in row:
      if cell == REVEALED_BOMB:
        return True
  return False

def main():
  board = initialize_board()
  bomb_row, bomb_col = generate_bomb_location()

  while True:
    display_board(board)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    action = input("Enter action (reveal: R, flag: F): ").upper()

    if not is_valid_cell(row, col):
      print("Invalid cell coordinates. Try again.")
      continue

    if action == "R":
      if board[row][col] != FLAGGED:  # Don't reveal flagged cells
        reveal_cell(board, row, col, bomb_row, bomb_col)
    elif action == "F":
      board[row][col] = FLAGGED if board[row][col] != FLAGGED else HIDDEN
    else:
      print("Invalid action. Please enter 'R' or 'F'.")
      continue

    if is_game_won(board):
      print("Congratulations! You won the game.")
      break
    elif is_game_lost(board):
      print("You hit a bomb! Game over.")
      break

if __name__ == "__main__":
  main()
