
#simple Tic Tac Toe
# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(str(square + 1))
    return board


def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def display_instructions(board):
    print("Welkom, dit is tiktaktoe")
    print("dit bord heeft "  + str(len(board)) + " vakjes")
    
    


board = new_board()
display_instructions(board)
display_board(board)

#Create a function named display-instructions which will show the instructions
#Doesn't have to be a 50 page manual ;)
#Make sure you call this function somewhere logical 😊  
