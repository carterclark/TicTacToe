#Tic Tac Toe

spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  #1-9
ref = ['1', '2', '3', '4', '5', '6', '7', '8', '9']     #1-9                            
num = len(ref)+7
boardRef = ['1', '|', '2', '|', '3', '', '4', '|', '5',
            '|', '6', '', '7', '|', '8', '|', '9']
numPick = []

def makeBoard(x):                        #Make board
    boardList = []
    if x == 0:              #reference board
        i = 0
        refNum = 0
        while i <= num:
            if (i%2) == 0:
                boardList.append(ref[refNum])
                refNum += 1
            elif i == 5 or i == 11:
                boardList.append('')
            else:
                boardList.append('|')
            i += 1
    
        print (boardList[0] + boardList[1] + boardList[2] +
               boardList[3] + boardList[4])
        print (boardList[5] + boardList[6] + boardList[7] +
               boardList[8] + boardList[9] +boardList[10])
        print (boardList[11] + boardList[12] +
               boardList[13] + boardList[14] + boardList[15] +
               boardList[16])
        
    elif x == 1:        #current board
        i = 0
        refNum = 0
        while i <= num:
            if (i%2) == 0:
                boardList.append(spaces[refNum])
                refNum += 1
            elif i == 5 or i == 11:
                boardList.append('')
            else:
                boardList.append('|')
            i += 1
    
        print (boardList[0] + boardList[1] + boardList[2] +
               boardList[3] + boardList[4])
        print (boardList[5] + boardList[6] + boardList[7] +
               boardList[8] + boardList[9] + boardList[10])
        print (boardList[11] + boardList[12] +
               boardList[13] + boardList[14] + boardList[15] +
               boardList[16])


def playerEntry (player): #P1 and P2 entry
    print("\n------------------------------------------------------------\n"
        "\nPick a number 1-9 to pick a square, \n"
          "players cannot pick a square twice, \n"
          "for key reference: \n")
    makeBoard(0)
    pick = input("\n(To end game enter 'end')"
                 "\nNumber entry: ")
    if pick == 'end':
        exit()
    try:
        pick = int(pick)
        if (0 < pick < 10) and pick not in numPick: #check number
            spaces.pop(pick-1)       
            spaces.insert(pick-1, player)
            numPick.append(pick)
            makeBoard(1)
        else:
            print("\nMake sure number entered is "
                "an INTEGER 1-9 and NOT already entered!\n")
            makeBoard(1)
            playerEntry(player)
    except ValueError:
        print("\nMake sure number entered is "
            "an INTEGER 1-9 and NOT already entered!\n")
        makeBoard(1)
        playerEntry(player)
        pass
        

def playGame(end):      #playing the game
    while end == 0:
        if end == 0:
            playerEntry('x')
            end = endState()
        if end == 0:
            playerEntry('o')
            end = endState()
    if end != 0:
        replay = input("Play again? Enter Y or N: ")
        if replay == 'N' or replay == 'n':
            return
        elif replay == 'Y' or replay == 'y':
            playGame(0)
        else:
            print("Entry needs to by a Y or a N")
            playGame(1)
        

def endState():#End game
    #check the x end state
    #rows
    if ((spaces[0] == 'x' and spaces[1] == 'x' and spaces[2]== 'x')
        or (spaces[3] == 'x' and spaces[4] == 'x' and spaces[5] == 'x')
        or (spaces[6] == 'x' and spaces[7] == 'x' and spaces[8] == 'x')

    #columns
        or (spaces[0] == 'x' and spaces[3] == 'x' and spaces[6] == 'x')
        or (spaces[1] == 'x' and spaces[4] == 'x' and spaces[7] == 'x')
        or (spaces[2] == 'x' and spaces[5] == 'x' and spaces[8] == 'x')

    #diagonal
        or (spaces[0] == 'x' and spaces[4] == 'x' and spaces[8] == 'x')
        or (spaces[2] == 'x' and spaces[4] == 'x' and spaces[6] == 'x')):
        print('X wins')
        return 1
    
    #check the o end state
    #rows
    if ((spaces[0] == 'o' and spaces[1] == 'o' and spaces[2]== 'o')
        or (spaces[3] == 'o' and spaces[4] == 'o' and spaces[5] == 'o')
        or (spaces[6] == 'o' and spaces[7] == 'o' and spaces[8] == 'o')

    #columns
        or (spaces[0] == 'o' and spaces[3] == 'o' and spaces[6] == 'o')
        or (spaces[1] == 'o' and spaces[4] == 'o' and spaces[7] == 'o')
        or (spaces[2] == 'o' and spaces[5] == 'o' and spaces[8] == 'o')

    #diagonal
        or (spaces[0] == 'o' and spaces[4] == 'o' and spaces[8] == 'o')
        or (spaces[2] == 'o' and spaces[4] == 'o' and spaces[6] == 'o')):
        print('O wins')
        return 1
    else:
        return 0
playGame(0)
