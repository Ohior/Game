from random import choice, randint

def getPlayerSymbol(word):
    if player.upper() == 'X':
        return 'X','O'
    else:
        return 'O','X'

def whoGoesFirst():
    num = randint(0,1)
    if num == 0:
        return 'human'
    else:
        return 'ai'

def playAgain(word):
    if word.lower().startswith('y'):
        return True

def makeMove(bo,le,num):
    bo[int(num)]=le

def wayToWin(word,bo):
    ways = ((1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9))
    for way in ways:
        if (bo[int(way[0])] == word) and (bo[int(way[1])] == word) and (bo[int(way[2])] == word):
            return True
    return False

def getBoardCopy(bo):
    board_copy = []
    for b in bo:
        board_copy.append(b)
    return board_copy

def isSpaceEmpty(num,bo):
    if bo[int(num)] == '.':
        return True

def getPlayerMove(num,bo):
    if isSpaceEmpty(num,bo):
        return int(num)
    else:
        return False

def getMoveFromList(movelist,bo):
    possible_moves = []
    for num in movelist:
        if isSpaceEmpty(num,bo):
            possible_moves.append(int(num))
    if len(possible_moves) != 0:
        return choice(possible_moves)
    else:
        return 0
 
def getComputerMove(player_symbol,computer_symbol,board):
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceEmpty(i,copy):
            makeMove(copy,computer_symbol,i)
            if wayToWin(computer_symbol,copy):
                return i

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceEmpty(i,copy):
            makeMove(copy,player_symbol,i)
            if wayToWin(player_symbol,copy):
                return i
    num = getMoveFromList([1,3,7,9,5,2,4,6,8],board)    
    if num != 0: return num    

def isBoardFull(bo):
    for i in range(1,10):
        if isSpaceEmpty(i,bo):return False
    return True

def howManySpaceRemain(bo):
    num = 0
    for b in bo:
        if b == '.':
            num+=1
    return num

def mainGame(num):
    global theBoard, info
    if int(num) == 0:
        theBoard = ['.'] * 10
    elif howManySpaceRemain(theBoard) > 2:
        if not wayToWin('O',theBoard):
            makeMove(theBoard,'X',num)
        if not wayToWin('X',theBoard):
            com_move = getComputerMove('X','O',theBoard)
            makeMove(theBoard,'O',com_move)
    return theBoard

def Winner():
    if wayToWin('X', theBoard):
        return 'X'
    if wayToWin('O', theBoard):
        return 'O'
    else:
        return 'none'

theBoard = ['.']*10
info = 'Play Game'

