def print_board(board):
    '''print_board(board) -> str
    returns a string that represents the Connect Four
    board given by the input list'''
    boardString = '\n'
    # add the column numbers to the output string
    for col in range(7):
        boardString += str(col) + ' '
    boardString += '\n'
    # loop through the input list
    # add the appropriate characters to the output string
    for row in range(6):
        for col in range(7):
            boardString += board[row][col] + ' '
        boardString += '\n'
    return boardString

def check_line_for_win(board,r,c,dr,dc,piece):
    '''check_line_for_win(board,r,c,dr,dc,piece) -> bool
    returns True if piece has a winning line
    starting at row r, col c and moving in the direction
      given by dr and dc'''
    for i in range(4):
        if board[r+i*dr][c+i*dc] != piece:
            return False
    return True

def check_for_win(board,piece):
    '''check_for_win(board,piece) -> bool
    returns True if piece has a winning line on the board'''
    # check horizontal
    for row in range(6):
        for col in range(4):
            if check_line_for_win(board,row,col,0,1,piece):
                return True
    # check vertical
    for row in range(3):
        for col in range(7):
            if check_line_for_win(board,row,col,1,0,piece):
                return True
    # check NW-SE diag
    for row in range(3):
        for col in range(4):
            if check_line_for_win(board,row,col,1,1,piece):
                return True
    # check NE-SW diag
    for row in range(3,6):
        for col in range(4):
            if check_line_for_win(board,row,col,-1,1,piece):
                return True
    return False
            

def play_connect_four():
    # initialize
    playerNames = []
    playerNames.append(input("Player X, enter your name: "))
    playerNames.append(input("Player O, enter your name: "))
    pieces = ['X','O']
    turn = 0  # whose turn is it
    turns = 0 # number of moves in the game
    # set up a blank board
    boardRow = ['.']*7
    board = []
    for row in range(6):
        board.append(boardRow[:])
    # initialize the column heights
    #  columnHeights[n] is the number of pieces
    #  played in column n
    columnHeights = [0]*7

    # play the game
    while turns < 42:
        print(print_board(board))
        legalPlay = False
        while not legalPlay:
            play = input(playerNames[turn]+", you're "+pieces[turn]+". What column do you want to play in? ")
            if not play.isdigit():
                print("That's not a valid column -- please choose again.")
            else:
                play = int(play)
                if play < 0 or play > 6:
                    print("That's not a valid column -- please choose again.")
                elif columnHeights[play] == 6:
                    print("That column is full -- please choose another.")
                else:
                    legalPlay = True
        # make the play
        height = 5-columnHeights[play]
        board[height][play] = pieces[turn]
        columnHeights[play] += 1
        # check for winner
        winner = check_for_win(board,pieces[turn])
        if winner:
            print(print_board(board))
            print("Congratulations, "+str(playerNames[turn])+", you won!")
            break
        turn = (turn + 1) % 2
        turns += 1
    if turns == 42:  # tie game
        print(print_board(board))
        print("It's a tie!")

play_connect_four()
