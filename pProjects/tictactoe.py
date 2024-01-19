board = [['1','|','2','|','3'],
		 ['-','+','-','+','-'],
		 ['4','|','5','|','6'],
		 ['-','+','-','+','-'],
		 ['7','|','8','|','9']
		 ]

winStates = [[0, 1, 2],
			 [3, 4, 5],
			 [6, 7, 8],
			 [0, 3, 6],
			 [1, 4, 7],
			 [2, 5, 8],
			 [0, 4, 8],
			 [2, 4, 6]]
			
gameState = ["","","","","","","","",""]
global roundWon
roundWon = False
global playerTurn
playerTurn = 0

#draws the board
def drawBoard():
	for i in range(len(board)):
		print(''.join(board[i]))

#determines whos turn it is		
def turn():
	if (playerTurn % 2 == 0):
		return "x"
	if (playerTurn % 2 == 1):
		return "o"

#checks for win conditions	
def Results():
    global roundWon
    for i in range(0,7):
        winCondition = winStates[i]
        a = gameState[winCondition[0]]
        b = gameState[winCondition[1]]
        c = gameState[winCondition[2]]
        if a == "" or b == "" or c == "":
            continue
        if a == b and b == c:
            roundWon = True
            break
    if roundWon:
        print("")
        drawBoard()
        print("")
        print(turn()," has won!")
    if "" not in gameState:
        print("")
        drawBoard()
        print("")
        print("It's a tie!")
        roundWon = True
    
#runs each round		
def playingGame():
    print("")
    global playerTurn
    drawBoard()
    print("")
    print("It is ", turn(), " turn.")
    repeat = True
    while repeat:
        try: 
            position = int(input(""))
        except:
            print("that isn't an integer")
        else:
            repeat = False
    gameState[position - 1] = turn()
    for i in range(len(board)):
        v = 0;
        for spot in board[i]:
            if spot == str(position):
                board[i][v] = turn()
                break
            v += 1
    Results()
    playerTurn += 1

print("Tic-Tac-Toe")
	
while roundWon != True:
	playingGame()

input("Press Enter to exit")