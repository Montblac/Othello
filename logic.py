# Samuel Leyva 54565096
# Othello Game Logic

class Opening:
    def GameRows(self):
        while True:
            try:
                rows = int(input())
                if rows < 4 or rows > 16:
                    raise ValueError
                elif rows % 2 != 0:
                    raise EvenError
                else:
                    return rows
            except ValueError:
                print('Out of Row Range.')
            except EvenError:
                print('Number must be an even integer.')

    def GameColumns(self):
        while True:
            try:
                columns = int(input())
                if columns < 4 or columns > 16:
                    raise ValueError
                elif columns % 2 != 0:
                    raise EvenError
                else:
                    return columns
            except ValueError:
                print('Out of Column Range.')
            except EvenError:
                print('Number must be an even integer.')

    def FirstMove(self):
        while True:
            try:
                player = input()
                if player != 'B' and player != 'W':
                    raise ValueError
                else:
                    return player
            except:
                print('Sorry, invalid player.')

    def Arrangement(self):
        while True:
            try:
                arrangement = input()
                if arrangement != 'B' and arrangement != 'W':
                    raise ValueError
                else:
                    return arrangement
            except:
                print('Sorry, invalid cell arrangement.')

    def Condition(self):
        while True:
            try:
                condition = input()
                if condition != '<' and condition != '>':
                    raise ValueError
                else:
                    return condition
            except:
                print('Sorry, invalid win conditions.')
                
    def GameInfo(self):
        info = {}

        info['Rows'] = self.GameRows()
        info['Columns'] = self.GameColumns()
        info['FirstMove'] = self.FirstMove()
        info['Arrangement'] = self.Arrangement()
        info['WinCondition'] = self.Condition()

        return info


class GameBoard:
    def __init__(self, GameInfo):
        self.gameinfo = GameInfo
        self.rows = None
        self.columns = None

    def createColumns(self):
        column = []
        for n in range(self.gameinfo['Columns']):
            column.append(0)
        self.columns = column

    def createRows(self):
        rows = []
        for integer in range(self.gameinfo['Rows']):
            rows.append(list(self.columns))
        self.rows = rows

    def createArrangement(self):
        columns = self.gameinfo['Columns']
        rows = self.gameinfo['Rows']
        if self.gameinfo['Arrangement'] == 'White':
            self.rows[int(rows / 2) - 1][int(columns / 2) - 1] = 'W'
            self.rows[int(rows / 2)][int(columns / 2)] = 'W'
            self.rows[int(rows / 2) - 1][int(columns / 2)] = 'B'
            self.rows[int(rows / 2)][int(columns / 2) - 1] = 'B'
        elif self.gameinfo['Arrangement'] == 'Black':
            self.rows[int(rows / 2) - 1][int(columns / 2) - 1] = 'B'
            self.rows[int(rows / 2)][int(columns / 2)] = 'B'
            self.rows[int(rows / 2) - 1][int(columns / 2)] = 'W'
            self.rows[int(rows / 2)][int(columns / 2) - 1] = 'W'

    def createBoard(self):
        self.createColumns()
        self.createRows()
        self.createArrangement()
    
        return self.rows
    

class GameState:
    def __init__(self, GameInfo, GameBoard, Turn):
        self.gameinfo = GameInfo
        self.gameboard = GameBoard
        self.turn = Turn

        self.logicTurn()


    def logicTurn(self):
        if self.turn == 'White':
            self.turn = 'W'
        else:
            self.turn = 'B'

    def PlayerTurn(self):
        if self.turn == 'W':
            self.turn = 'B'
        elif self.turn == 'B':
            self.turn = 'W'
        return self.turn

    def GameScore(self):
        score = {'White': 0, 'Black': 0}
        
        for row in self.gameboard:
            for element in row:
                if element == 'W':
                    score['White'] += 1
                elif element == 'B':
                    score['Black'] += 1
        return score
    
    def Winner(self):
        score = self.GameScore()
        player = None

        if self.gameinfo['WinCondition'] == '>':
            if score['White'] > score['Black']:
                player = 'W'

            elif score['Black'] > score['White']:
                player = 'B'
                
            else:
                player = 'NONE'
                
        elif self.gameinfo['WinCondition'] == '<':
            if score['White'] < score['Black']:
                player = 'W'
                
            elif score['Black'] < score['White']:
                player = 'B'
                
            else:
                player = 'NONE'

        return player
               
    def PlayerMove(self, cell):
        while True:
            try:
                moveColumn, moveRow = cell

                flipList = self.ValidMove(moveRow, moveColumn)

                self.gameboard[int(moveRow)][int(moveColumn)] = self.turn
                self.FlipDisc(flipList)
                break
                  
            except:
                pass
                
        return self.gameboard


    def FlipDisc(self, flipList):
        for item in flipList:
            if type(item[0]) == int:
                if self.gameboard[item[0]][item[1]] == 'W':
                    self.gameboard[item[0]][item[1]] = 'B'
                elif self.gameboard[item[0]][item[1]] == 'B':
                    self.gameboard[item[0]][item[1]] = 'W'
                else:
                    continue
            else:
                self.FlipDisc(item)
            
    def ValidMove(self, moveRow, moveColumn):
        
        if not self.ValidRow(moveRow) \
           or not self.ValidColumn(moveColumn) \
           or self.gameboard[moveRow][moveColumn] != 0:
            raise MoveError
        
        gameboardCopy = list(self.gameboard)
        
        start = [moveRow, moveColumn]
        
        dirList = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
        flipList = []

        for direction in dirList:
            if self.ValidRow(moveRow + direction[0]) \
               and self.ValidColumn(moveColumn + direction[1]) \
               and gameboardCopy[moveRow + direction[0]][moveColumn + direction[1]] != self.turn:
                if gameboardCopy[moveRow + direction[0]][moveColumn + direction[1]] == 0:
                    continue
                
                else:
                    row = moveRow + direction[0]
                    column = moveColumn + direction[1]
                    end = None
                    
                    while self.ValidRow(row) and self.ValidColumn(column):
                        if gameboardCopy[row][column] == 0:
                            break
                        
                        elif gameboardCopy[row][column] == self.turn:


                            row -= direction[0]
                            column -= direction[1]
                            
                            while end != start:
                                flipList.append([row, column])
                                row -= direction [0]
                                column -= direction[1]
                                end = [row, column]
                                
                            break
                        else:
                            row += direction[0]
                            column += direction[1]
            else:
                continue
            
        if flipList == []:
            raise MoveError
        
        else:
            return flipList

    def ValidRow(self, moveRow):
        return 0 <= moveRow < self.gameinfo['Rows']

    def ValidColumn(self, moveColumn):
        return 0 <= moveColumn < self.gameinfo['Columns']

    def PossibleMove(self):
        moveList = []

        for c in range(self.gameinfo['Columns']):
            for r in range(self.gameinfo['Rows']):
                try:
                    if self.ValidMove(r, c) != []:
                        moveList.append([r, c])
                        
                except:
                    continue
                
        if moveList != []:
            return True
        else:
            return False
                    

        
# Exceptions ----------------------------

class EvenError(Exception):
    pass

class MoveError(Exception):
    pass
