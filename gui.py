# Samuel Leyva 54565096
# GUI

import math
import tkinter
import logic
from win32api import GetSystemMetrics

defaultFont = ('Calibri', 18)
color = '#BAB8B8'

class OptionWindow:
    def __init__(self):
        self.optionWindow = tkinter.Tk()
        self.optionWindow.title('Settings')
        self.optionWindow.configure(background = '#BAB8B8')

        print("Width =", GetSystemMetrics(0))
        print("Height =", GetSystemMetrics(1))

        w = 400 #280
        h = 300 #230
        
        ws = self.optionWindow.winfo_screenwidth()
        hs = self.optionWindow.winfo_screenheight()
        xs = (ws / 2) - (w / 2)
        ys = (hs / 2) - (h / 2)
        self.optionWindow.geometry('%dx%d+%d+%d' % (w, h, xs, ys))


        # Frames
        textFrame = tkinter.Frame(master = self.optionWindow, background = '#BAB8B8')
        textFrame.grid(row = 0, column = 0, padx = 10, pady = 5)

        optionFrame = tkinter.Frame(master = self.optionWindow, background = '#BAB8B8')
        optionFrame.grid(row = 0, column = 1, padx = 10, pady = 5)

        buttonFrame = tkinter.Frame(master = self.optionWindow, background = '#BAB8B8')
        buttonFrame.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = (1,4))


        # Labels
        rowLabel = tkinter.Label(
            master = textFrame, text = 'Number of Rows:',
            font = defaultFont)
        rowLabel.grid(
            row = 1, column = 0, pady = 4,
            sticky = tkinter.W + tkinter.S)
        rowLabel.configure(background = '#BAB8B8')

        columnLabel = tkinter.Label(
            master = textFrame, text = 'Number of Columns:',
            font = defaultFont)
        columnLabel.grid(
            row = 2, column = 0, pady = 4,
            sticky = tkinter.W + tkinter.S)
        columnLabel.configure(background = '#BAB8B8')

        firstLabel = tkinter.Label(
            master = textFrame, text = 'First Move:',
            font = defaultFont)
        firstLabel.grid(
            row = 3, column = 0, pady = 4,
            sticky = tkinter.W + tkinter.S)
        firstLabel.configure(background = '#BAB8B8')

        arrangementLabel = tkinter.Label(
            master = textFrame, text = 'Disc Arrangement:',
            font = defaultFont)
        arrangementLabel.grid(
            row = 4, column = 0, pady = 4,
            sticky = tkinter.W + tkinter.S)
        arrangementLabel.configure(background = '#BAB8B8')

        conditionLabel = tkinter.Label(
            master = textFrame, text = 'Win Condition:',
            font = defaultFont)
        conditionLabel.grid(
            row = 5, column = 0, pady = 4,
            sticky = tkinter.W + tkinter.S)
        conditionLabel.configure(background = '#BAB8B8')


        # Dropdown Menus
        self.row = tkinter.StringVar(optionFrame)
        optionRow = tkinter.OptionMenu(
            optionFrame, self.row,
            "4", "6", "8", "10", "12", "14", "16")
        optionRow.grid(
            row = 1, column = 0, pady = 3,
            sticky = tkinter.E + tkinter.S)
        optionRow.config(
            background = '#BAB8B8', width = 10,
            justify = tkinter.CENTER)
        self.rowChoice = None

        self.column = tkinter.StringVar(optionFrame)
        optionColumn = tkinter.OptionMenu(
            optionFrame, self.column,
            "4", "6", "8", "10", "12", "14", "16")
        optionColumn.grid(
            row = 2, column = 0, pady = 3,
            sticky = tkinter.E + tkinter.S)
        optionColumn.config(
            background = '#BAB8B8', width = 10,
            justify = tkinter.CENTER)
        self.columnChoice = None

        self.first = tkinter.StringVar(optionFrame)
        optionFirst = tkinter.OptionMenu(
            optionFrame, self.first, "White", "Black")
        optionFirst.grid(
            row = 3, column = 0, pady = 3,
            sticky = tkinter.E + tkinter.S)
        optionFirst.config(
            background = '#BAB8B8', width = 10,
            justify = tkinter.CENTER)
        self.firstChoice = None

        self.arrangement = tkinter.StringVar(optionFrame)
        optionArrangement = tkinter.OptionMenu(
            optionFrame, self.arrangement, "White", "Black")
        optionArrangement.grid(
            row = 4, column = 0, pady = 3,
            sticky = tkinter.E + tkinter.S)
        optionArrangement.config(
            background = '#BAB8B8', width = 10,
            justify = tkinter.CENTER)
        self.arrangementChoice = None

        self.condition = tkinter.StringVar(optionFrame)
        optionCondition = tkinter.OptionMenu(
            optionFrame, self.condition, "Most", "Least")
        optionCondition.grid(
            row = 5, column = 0, pady = 3,
            sticky = tkinter.E + tkinter.S)
        optionCondition.config(
            background = '#BAB8B8', width = 10,
            justify = tkinter.CENTER)
        self.conditionChoice = None


        # Buttons
        startGame = tkinter.Button(
            master = buttonFrame, text = 'Start',
            command = self.handleStartButton, font = defaultFont)
        startGame.grid(
            row = 0, column = 0)
        startGame.configure(highlightbackground = '#BAB8B8')


        # Other
        self.optionWindow.resizable(0, 0)


    def settings(self):
        self.rowChoice = int(self.row.get())
        self.columnChoice = int(self.column.get())
        self.firstChoice = self.first.get()
        self.arrangementChoice = self.arrangement.get()
        self.conditionChoice = self.condition.get()

        settings = {
            'Rows':self.rowChoice,
            'Columns':self.columnChoice,
            'FirstMove':self.firstChoice,
            'Arrangement':self.arrangementChoice,
            'WinCondition':self.conditionChoice}
        
        return settings


    def handleStartButton(self):
        self.settings()
        self.optionWindow.destroy()


    def start(self) -> None:
        self.optionWindow.mainloop()


class GameWindow:
    def __init__(self, info):
        self.info = info
        self.board = logic.GameBoard(self.info).createBoard()
        self.turn = info['FirstMove']
        self.state = logic.GameState(self.info, self.board, self.turn)

        self.score = self.state.GameScore()

        self.cells = {}
        self.spots = {}

        self.gameWindow = tkinter.Tk()
        self.gameWindow.title('Othello')
        self.gameWindow.rowconfigure(0, weight = 1)
        self.gameWindow.columnconfigure(0, weight = 1)


        # Frames
        dataFrame = tkinter.Frame(
            master = self.gameWindow, background = '#BA0000')
        dataFrame.grid(
            row = 1, column = 0,
            sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)

        dataFrame.rowconfigure(0, weight = 1)
        dataFrame.columnconfigure(0, weight = 1)
        dataFrame.rowconfigure(1, weight = 1)
        dataFrame.columnconfigure(1, weight = 1)


        # Labels
        self.whiteVar = tkinter.StringVar()
        self.whiteVar.set('White: {}'.format(self.score['White']))
        scoreWhite = tkinter.Label(
            master = dataFrame, font = ('Calibri', 20),
            fg = 'WHITE', textvariable = self.whiteVar)
        scoreWhite.configure(background = '#BA0000')
        scoreWhite.grid(
            row = 0, column = 0)

        self.blackVar = tkinter.StringVar()
        self.blackVar.set('Black: {}'.format(self.score['Black']))
        scoreBlack = tkinter.Label(
            master = dataFrame, font = ('Calibri', 20),
            fg = 'WHITE', textvariable = self.blackVar)
        scoreBlack.configure(background = '#BA0000')
        scoreBlack.grid(
            row = 1, column = 0)

        self.turnVar = tkinter.StringVar()
        self.turnVar.set('Turn: {}'.format(self.turn))
        turnLabel = tkinter.Label(
            master = dataFrame, font = ('Calibri', 20),
            fg = 'WHITE', textvariable = self.turnVar,
            width = 10)
        turnLabel.configure(background = '#BA0000')
        turnLabel.grid(
            row = 0, column = 1)


        # Canvas
        self.canvas = tkinter.Canvas(
            master = self.gameWindow, width = 600,
            height = 600, bg = 'GREY',
            highlightbackground = 'BLACK')
        self.canvas.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self.canvas.rowconfigure(0, weight = 1)
        self.canvas.columnconfigure(0, weight = 1)

        self.canvas.bind('<Configure>', self.updateBoard)
        self.canvas.bind('<Button-1>', self.onClick)


        # Other
        self.changeWinCondition()
        self.drawBoard()
        self.drawArrangement()


    def drawBoard(self):
        ''' Draws the board with specified dimensions and saves each cell info
        '''
        cwidth = (float(self.canvas.winfo_width()) / self.info['Columns'])
        cheight = (float(self.canvas.winfo_height()) / self.info['Rows'])        

        for column in range(self.info['Columns']):
            for row in range(self.info['Rows']):
                x = column * cwidth
                y = row * cheight
                
                self.canvas.create_rectangle(
                    x, y, x + cwidth, y + cheight,
                    width = 3, outline = 'BLACK')
                
                self.cells[(column, row)] = (x, y, x + cwidth, y + cheight)


    def drawArrangement(self):
        ''' Draws the initial arrangement of discs
        '''
        
        if self.info['Arrangement'] == 'White':
            
            cx1 = int(self.info['Columns'] / 2) - 1
            cy1 = int(self.info['Rows'] / 2) - 1
            
            x1, y1, x2, y2 = self.cells[(cx1, cy1)]
            self.spots[(cx1, cy1)] = (x1, y1, x2, y2, 'White')
            
            self.drawSpot((cx1, cy1))

            cx2 = int(self.info['Columns'] / 2)
            cy2 = int(self.info['Rows'] / 2)

            x1, y1, x2, y2 = self.cells[(cx2, cy2)]
            self.spots[(cx2, cy2)] = (x1, y1, x2, y2, 'White')
            
            self.drawSpot((cx2, cy2))

            cx3 = int(self.info['Columns'] / 2) - 1
            cy3 = int(self.info['Rows'] / 2)
            
            x1, y1, x2, y2 = self.cells[(cx3, cy3)]
            self.spots[(cx3, cy3)] = (x1, y1, x2, y2, 'Black')
            
            self.drawSpot((cx3, cy3))

            cx4 = int(self.info['Columns'] / 2)
            cy4 = int(self.info['Rows'] / 2) - 1

            x1, y1, x2, y2 = self.cells[(cx4, cy4)]
            self.spots[(cx4, cy4)] = (x1, y1, x2, y2, 'Black')
            
            self.drawSpot((cx4, cy4))

        else:
            cx1 = int(self.info['Columns'] / 2) - 1
            cy1 = int(self.info['Rows'] / 2) - 1
            
            x1, y1, x2, y2 = self.cells[(cx1, cy1)]
            self.spots[(cx1, cy1)] = (x1, y1, x2, y2, 'Black')
            
            self.drawSpot((cx1, cy1))

            cx2 = int(self.info['Columns'] / 2)
            cy2 = int(self.info['Rows'] / 2)

            x1, y1, x2, y2 = self.cells[(cx2, cy2)]
            self.spots[(cx2, cy2)] = (x1, y1, x2, y2, 'Black')
            
            self.drawSpot((cx2, cy2))

            cx3 = int(self.info['Columns'] / 2) - 1
            cy3 = int(self.info['Rows'] / 2)
            
            x1, y1, x2, y2 = self.cells[(cx3, cy3)]
            self.spots[(cx3, cy3)] = (x1, y1, x2, y2, 'White')
            
            self.drawSpot((cx3, cy3))

            cx4 = int(self.info['Columns'] / 2)
            cy4 = int(self.info['Rows'] / 2) - 1

            x1, y1, x2, y2 = self.cells[(cx4, cy4)]
            self.spots[(cx4, cy4)] = (x1, y1, x2, y2, 'White')
            
            self.drawSpot((cx4, cy4))


    def updateSpots(self):

        for spot in self.spots:
            self.drawSpot(spot)

    def updateScore(self):
        self.score = self.state.GameScore()
        self.whiteVar.set('White: {}'.format(self.score['White']))
        self.blackVar.set('Black: {}'.format(self.score['Black']))

    def updateBoard(self, event: tkinter.Event):
        self.canvas.delete(tkinter.ALL)
        self.drawBoard()
        self.updateSpots()

    def updateState(self):
        self.state = logic.GameState(self.info, self.board, self.turn)

    def onClick(self, event: tkinter.Event):
        ''' Checks if click is in range, draws a spot in cell,
            updates active cell dictionary 
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        for cell in self.cells:
            if self.xWithin(event.x, cell):
                if self.yWithin(event.y, cell):
                
                    column, row = cell

                    try:
                        if self.state.ValidMove(row, column) != []:

                            flipList = self.state.ValidMove(row, column)
                            self.board = self.state.PlayerMove(cell)

                            for coordinates in flipList:
                                row, column = coordinates

                                x1, y1, x2, y2 = self.cells[(column, row)]

                                x1, y1 = Calculate.fracCoordinate(x1, y1, width, height)
                                x2, y2 = Calculate.fracCoordinate(x2, y2, width, height)

                                self.spots[(column, row)] = (x1, y1, x2, y2, self.turn)
                                self.drawSpot((column, row))                            
                           
                            x1, y1, x2, y2 = self.cells[cell]
                           
                            x1, y1 = Calculate.fracCoordinate(x1, y1, width, height)
                            x2, y2 = Calculate.fracCoordinate(x2, y2, width, height)

                            self.spots[cell] = (x1, y1, x2, y2, self.turn)
                            self.drawSpot(cell)

                            self.updateScore()
                            self.changeTurn()
                            self.updateState()
                            
                            if not self.state.PossibleMove():
                                self.changeTurn()
                                self.updateState()
                                if not self.state.PossibleMove():
                                    winner = self.state.Winner()

                                    if winner == 'W':
                                        winner = 'White'
                                    elif winner == 'B':
                                        winner = 'Black'
                                    else:
                                        winner = None
                                        
                                    self.gameWindow.quit()
                                    WinnerWindow(winner).show()
                            
                            self.turnVar.set('Turn: {}'.format(self.turn))

                    except:
                        pass



        # Testing Area -----------------            
        #print(self.turn)

    def drawSpot(self, cell):
        ''' Draws a spot in a designated cell
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        if 'White' in self.spots[cell]:
            self.canvas.create_oval(
                self.spots[cell][0] * width + 10,
                self.spots[cell][1] * height + 10,
                self.spots[cell][2] * width - 10,
                self.spots[cell][3] * height - 10,
                fill = 'WHITE')

        else:
            self.canvas.create_oval(
                self.spots[cell][0] * width + 10,
                self.spots[cell][1] * height + 10,
                self.spots[cell][2] * width - 10,
                self.spots[cell][3] * height - 10,
                fill = 'BLACK')


    def xWithin(self, x, cell) -> bool:
        ''' Returns True if x is within cell range
        '''
        return self.cells[cell][0] < x < self.cells[cell][2]


    def yWithin(self, y, cell) -> bool:
        ''' Returns True if y is within cell range
        '''
        return self.cells[cell][1] < y < self.cells[cell][3]


    def changeTurn(self) -> str:
        ''' Changes the turn to the opposite player
        '''
        if self.turn == 'White':
            self.turn = 'Black'
        else:
            self.turn = 'White'

    def changeWinCondition(self) -> dict:
        ''' Changes the value of the win condition
        '''
        if self.info['WinCondition'] == 'Most':
            self.info['WinCondition'] = '>'
        else:
            self.info['WinCondition'] = '<'
            

    def start(self) -> None:
        ''' Starts the game window
        '''
        self.gameWindow.mainloop()


            
class Calculate:
    def center(x1, y1, x2, y2) -> tuple:
        ''' Calculates the center of a rectangle
        '''
        return ((x2 + x1) / 2, (y2 + y1) / 2)

    def pixelCoordinate(frac_x, frac_y, width, height) -> tuple:
        ''' Converts fractional coordinate to pixel coordinate
        '''
        return (frac_x * width, frac_y * height)

    def fracCoordinate(pixel_x, pixel_y, width, height) -> tuple:
        ''' Converts pixel coordinate to fractional coordinate
        '''
        return (pixel_x / width, pixel_y / height)


class WinnerWindow:
    def __init__(self, winner):
        self.winnerWindow = tkinter.Toplevel()

        self.winnerVar = tkinter.StringVar()
        self.winnerVar.set('Winner is {}!'.format(winner))
        winnerLabel = tkinter.Label(
            master = self.winnerWindow, font = ('Calibri', 20),
            textvariable = self.winnerVar, width = 20, height = 10 )
        winnerLabel.grid(sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        winnerLabel.configure(background = 'GREY')
        
        self.winnerWindow.rowconfigure(0, weight = 1)
        self.winnerWindow.columnconfigure(0, weight = 1)
                               
        self.winnerWindow.resizable(0, 0)

    def show(self) -> None:
        self.winnerWindow.grab_set()
        self.winnerWindow.wait_window()



def runOthello():
    opening = OptionWindow()
    opening.start()
    info = opening.settings()
    
    game = GameWindow(info)
    game.start()

               
if __name__ == '__main__':
    runOthello()





        
        
