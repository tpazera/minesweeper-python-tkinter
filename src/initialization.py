import tkinter.messagebox
import tkinter as tk
import random


def checkParameters(self, h, w, b, gameFrame, app):
    if h < 2 or w < 2 or h > 15 or w > 15 or b < 0 or b > h * w:
        tkinter.messagebox.showinfo("Bad parameters", "Please input a valxDid size of a board and a number of mines!")
    else:
        gameFrame.focus_force()
        application = app
        self.loadImages()

        try:  # exception #2
            self.tileField.destroy()
            self.statusField.destroy()
        except AttributeError:
            print("First launch!")

        self.tileField = tk.Frame(gameFrame)
        self.tileField.grid(row=1, column=0)
        statusField = tk.Frame(gameFrame)
        statusField.grid(row=0, column=0)
        tk.Label(statusField, text="Mines: " + str(b), width=10).grid(row=0, column=0, padx=5, pady=5)
        self.flagInfo = tk.Label(statusField, text="Flags: 0", width=10)
        self.flagInfo.grid(row=0, column=1, padx=5, pady=5)

        self.h, self.w, self.b = h, w, b
        self.generateLists(h, w, b) #generating userField, gameField
        self.buttons = self.generateTiles(h, w, self.tileField)

        application.bind("<Key>", self.cheat)


def loadImages(self):
    self.emptyTile = tk.PhotoImage(file="assets/empty.gif")
    self.bombTile = tk.PhotoImage(file="assets/bomb.gif")
    self.pbombTile = tk.PhotoImage(file="assets/pbomb.gif")
    self.flagTile = tk.PhotoImage(file="assets/flag.gif")
    self.qmarkTile = tk.PhotoImage(file="assets/qmark.gif")
    self.cheatTile = tk.PhotoImage(file="assets/cheat.gif")
    self.nearbyTile = [tk.PhotoImage(file = "assets/n" + str(i) + ".gif") for i in range (0,9)] #list comprehension #1
    print("Images loaded!")


def generateLists(self, h, w, b):
    userField = [[0] * w for i in range(h)] #list_comprehension #2
    gameField = [x for x in userField] #list comprehension #3
    userField = [['X'] * w for i in range(h)]
    bombs = b
    while (bombs > 0):
        x = random.randint(0, h-1)
        y = random.randint(0, w-1)
        if gameField[x][y] != 9:
            gameField[x][y] = 9
            bombs -= 1
    self.bombs = b

    self.gameField = gameField
    self.userField = userField

    for i in range(0, h):
        for j in range(0, w):
            if gameField[i][j] != 9:
                if i == 0 and j == 0: #lewy górny kafelek
                    neighbours = 0
                    if self.findNeighbours(i, j + 1):
                        neighbours += 1
                    if self.findNeighbours(i + 1, j):
                        neighbours += 1
                    if self.findNeighbours(i + 1, j + 1):
                        neighbours += 1
                elif i == h-1 and j == w-1: #prawy dolny kafelek
                    neighbours = 0
                    if self.findNeighbours(i-1, j - 1):
                        neighbours += 1
                    if self.findNeighbours(i - 1, j):
                        neighbours += 1
                    if self.findNeighbours(i, j - 1):
                        neighbours += 1
                elif i == 0 and j == w-1: #prawy górny kafelek
                    neighbours = 0
                    if self.findNeighbours(i, j - 1):
                        neighbours += 1
                    if self.findNeighbours(i + 1, j - 1):
                        neighbours += 1
                    if self.findNeighbours(i + 1, j):
                        neighbours += 1
                elif i == h-1 and j == 0: #lewy dolny kafelek
                    neighbours = 0
                    if self.findNeighbours(i - 1, j):
                        neighbours += 1
                    if self.findNeighbours(i - 1, j + 1):
                        neighbours += 1
                    if self.findNeighbours(i, j + 1):
                        neighbours += 1
                else:
                    if i == 0: #pierwszy wiersz
                        neighbours = 0
                        if self.findNeighbours(i, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i, j + 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j + 1):
                            neighbours += 1
                    elif i == h-1: #ostatni wiersz
                        neighbours = 0
                        if self.findNeighbours(i, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i, j + 1):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j + 1):
                            neighbours += 1
                    elif j == 0: #pierwsza kolumna
                        neighbours = 0
                        if self.findNeighbours(i - 1, j):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j + 1):
                            neighbours += 1
                        if self.findNeighbours(i, j + 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j + 1):
                            neighbours += 1
                    elif j == w-1: #ostatnia kolumna
                        neighbours = 0
                        if self.findNeighbours(i - 1, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j):
                            neighbours += 1
                        if self.findNeighbours(i, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j):
                            neighbours += 1
                    else:
                        neighbours = 0
                        if self.findNeighbours(i - 1, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j):
                            neighbours += 1
                        if self.findNeighbours(i - 1, j + 1):
                            neighbours += 1
                        if self.findNeighbours(i, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i, j + 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j - 1):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j):
                            neighbours += 1
                        if self.findNeighbours(i + 1, j + 1):
                            neighbours += 1

                gameField[i][j] = neighbours

    for i in range(0, h):
        for j in range(0, w):
            print(gameField[i][j], end='')
        print("")


def findNeighbours(self, x, y):
    try: #exception #3
        if self.gameField[x][y] == 9:
            return True
    except IndexError:
        pass


def generateTiles(self, h, w, tileField):
    buttons = []
    tileField.emptyTile = tk.PhotoImage(file="assets/empty.gif")
    for i in range(0, h):
        for j in range(0, w):
            buttonTMP = tk.Button(tileField, image=tileField.emptyTile, compound=tk.TOP, bg="grey")
            buttonTMP.bind('<Button-1>', self.leftClickLambda(i, j, w, h))
            buttonTMP.bind('<Button-3>', self.rightClickLambda(i, j, w, h))
            buttons.append([buttonTMP, (i, j)])
    for x in buttons:
        x[0].grid(row=x[1][0], column=x[1][1])
    return buttons