from random import randint

board = []
derp = 0
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
total_turns = int(raw_input("How many guesses will it take you to find my battleship?"))

for turn in range(total_turns):

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    guess_row = guess_row - 1
    guess_col = guess_col - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!!!!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "guess again! thats not even in the grid/ocean!"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print "Turn", turn + 1
        derp = derp + 1
    print_board(board)
    print total_turns
    print derp
    if derp == total_turns:
        print "Game Over"

    
