import tkinter.messagebox


def leftClickLambda(self, i, j, w, h):
    return lambda Button: self.leftClick(i, j, w, h)  # lambda #1


def rightClickLambda(self, i, j, w, h):
    return lambda Button: self.rightClick(i, j, w, h)  # lambda #2


def leftClick(self, i, j, w, h):
    if self.userField[i][j] != 'F' and self.userField[i][j] != 'Q':
        self.buttons[i * w + j][0].unbind("<Button 1>")
        self.buttons[i * w + j][0].unbind("<Button 3>")
        # buttons[i * w + j][0].configure(state=tk.DISABLED)
        if self.gameField[i][j] == 9:
            enabledCheat = False
            tkinter.messagebox.showinfo("You lose!", "Unfortunately you stop on a mine!")
            for x in self.buttons:
                x[0].unbind("<Button 1>")
                x[0].unbind("<Button 3>")
                if self.gameField[x[1][0]][x[1][1]] == 9:
                    x[0].config(image=self.pbombTile)
                else:
                    x[0].config(image=self.nearbyTile[self.gameField[x[1][0]][x[1][1]]])
            self.buttons[i * w + j][0].config(image=self.bombTile)
        elif self.gameField[i][j] == 0:
            self.checkEmptyNeigbours(i, j, w, h)
        else:
            self.userField[i][j] = 'O'
            self.buttons[i * w + j][0].config(image=self.nearbyTile[self.gameField[i][j]])
            self.checkForWin(w, h)
            self.checkForWin2(w, h)


def checkEmptyNeigbours(self, i, j, w, h):
    if i < 0 or j < 0 or i > h- 1 or j > w - 1 or self.userField[i][j] != 'X':
        return
    if self.gameField[i][j] == 0 and self.userField[i][j] != 'F':
        self.userField[i][j] = 'O'
        self.buttons[i * w + j][0].config(image=self.nearbyTile[0])
        self.buttons[i * w + j][0].unbind("<Button 1>")
        self.buttons[i * w + j][0].unbind("<Button 3>")
        # buttons[i * w + j][0].configure(state=tk.DISABLED)
        self.checkEmptyNeigbours(i, j - 1, w, h)
        self.checkEmptyNeigbours(i - 1, j, w, h)
        self.checkEmptyNeigbours(i + 1, j, w, h)
        self.checkEmptyNeigbours(i, j + 1, w, h)
    elif self.userField[i][j] != 'F':
        self.userField[i][j] = 'O'
        self.buttons[i * w + j][0].config(image=self.nearbyTile[self.gameField[i][j]])
        self.buttons[i * w + j][0].unbind("<Button 1>")
        self.buttons[i * w + j][0].unbind("<Button 3>")
        # buttons[i * w + j][0].configure(state=tk.DISABLED)


def rightClick(self, i, j, w, h):
    if self.userField[i][j] == 'X':
        self.userField[i][j] = 'F'
        self.buttons[i * w + j][0].config(image=self.flagTile)
        countFlags = 0
        for i in range(0, h):
            for j in range(0, w):
                if self.userField[i][j] == 'F':
                    countFlags += 1
        self.flagInfo.config(text='Flags: ' + str(countFlags))
    elif self.userField[i][j] == 'F':
        self.userField[i][j] = 'Q'
        self.buttons[i * w + j][0].config(image=self.qmarkTile)
        countFlags = 0
        for i in range(0, h):
            for j in range(0, w):
                if self.userField[i][j] == 'F':
                    countFlags += 1
        self.flagInfo.config(text='Flags: ' + str(countFlags))
    elif self.userField[i][j] == 'Q':
        self.userField[i][j] = 'X'
        if self.enabledCheat:
            self.buttons[i * w + j][0].config(image=self.cheatTile)
        else:
            self.buttons[i * w + j][0].config(image=self.emptyTile)
    self.checkForWin(w, h)
    self.checkForWin2(w, h)