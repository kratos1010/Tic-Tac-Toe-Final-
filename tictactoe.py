#Initializes the board
theBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#Valid moves
moves = ["1", "2", "3"]

#Prints board
def print_board():

    for row in range(len(theBoard)):
        print "%s|%s|%s" % (theBoard[row][0], theBoard[row][1], theBoard[row][2])
        if row < len(theBoard) - 1:
            print "-" * 5    
            
#Checks for P1 win conditions
def check_winx():

    for row in range(len(theBoard)):
        rowCheck = "%s%s%s" % (theBoard[row][0], theBoard[row][1], theBoard[row][2])
        
        if rowCheck == "XXX":
            winx()
            
        else:
            pass
        
    for col in range(len(theBoard)):
        colCheck = "%s%s%s" % (theBoard[0][col], theBoard[1][col], theBoard[2][col])
        
        if colCheck == "XXX":
            winx()
            
        else:
            pass
    if theBoard[0][0] + theBoard[1][1] + theBoard [2][2] == "XXX" or theBoard[0][2] + theBoard[1][1] + theBoard [0][2] == "XXX":
        winx()
    else:
        pass
            
#Checks for P2 win conditions
def check_wino():
    
    for row in range(len(theBoard)):
        rowCheck = "%s%s%s" % (theBoard[row][0], theBoard[row][1], theBoard[row][2])
        
        if rowCheck == "OOO":
            wino()
        else:
            pass
        
    for col in range(len(theBoard)):
        colCheck = "%s%s%s" % (theBoard[0][col], theBoard[1][col], theBoard[2][col])

        if colCheck == "OOO":
            wino()
        else:
            pass
    
    if theBoard[0][0] + theBoard[1][1] + theBoard [2][2] == "OOO" or theBoard[0][2] + theBoard[1][1] + theBoard [0][2] == "OOO":
        wino()
    else:
        pass

#Checks for draw
def check_draw():
    if " " not in theBoard[0] and " " not in theBoard[1] and " " not in theBoard[2]:
        print "It's a draw!"
        newgame()
    else:
        pass


            
#Asks P1 for a move
def get_movex():
    print "Player 1, what row?"
    row = raw_input()
    
    if row not in moves:
        print "Invalid input. Try again."
        get_movex()
    else:
        print "Player 1, what col?"
        col = raw_input()
    
        if col not in moves:
            print "Invalid input. Try again."
            get_movex()
        else:
            if theBoard[int(row) - 1][int(col) - 1] == "X" or theBoard[int(row) - 1][int(col) - 1] == "O":
                print "Sorry, it's taken. Try again."
                get_movex()
            else:
                theBoard[int(row) - 1][int(col) - 1] = "X"

#Asks P2 for a move
def get_moveo():
    print "Player 2, what row?"
    row = raw_input()
    
    if row not in moves:
        print "Invalid input. Try again."
        get_moveo()
    else:   
        print "Player 2, what col?"
        col = raw_input()
    
        if col not in moves:
            print "Invalid input. Try again."
            get_moveo()
        else:
            if theBoard[int(row) - 1][int(col) - 1] == "X" or theBoard[int(row) - 1][int(col) - 1] == "O":
                print "Sorry, it's taken. Try again."
                get_moveo()
            else:
                theBoard[int(row) - 1][int(col) - 1] = "O"
#P1 Win
def winx():
    print_board()
    print "Good game! Player 1 wins!"
    newgame()
#P2 Win    
def wino():
    print_board()
    print "Good game! Player 2 wins!"
    newgame()
    
#Start New Game
def newgame():
    print "Do you want to play again?"
    ans = raw_input("Y/N > ")
    if ans == "Y":
        start_game()
    else:
        print "Goodbye!"
        quit()
    
#starts the game, can I initialize the board here?
#Also need to set win to false here.
def start_game():
    print "Let's play tic tac toe. Player 1 is X, Player 2 is O.\n"
    
    print_board()
    
    while True:
        get_movex()
        check_winx()
        check_draw()
        print_board()
        get_moveo()
        check_wino()
        check_draw()
        print_board()

start_game()
