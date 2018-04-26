import tkinter.messagebox


def checkForWin(self, w, h):
    correct, flags = 0, 0
    for i in range(0, h):
        for j in range(0, w):
            if self.userField[i][j] == 'F' and self.gameField[i][j] == 9:
                correct += 1
            if self.userField[i][j] == 'F':
                flags += 1
    if correct == self.bombs and self.bombs == flags:
        self.enabledCheat = False
        tkinter.messagebox.showinfo("You win!", "Nice work, you win!")
        for x in self.buttons:
            x[0].unbind("<Button 1>")
            x[0].unbind("<Button 3>")
            if self.gameField[x[1][0]][x[1][1]] == 9:
                x[0].config(image=self.flagTile)
            else:
                x[0].config(image=self.nearbyTile[self.gameField[x[1][0]][x[1][1]]])


def checkForWin2(self, w, h):
    toClick = 0
    clicked = 0
    for i in range(0, h):
        for j in range(0, w):
            if self.gameField[i][j] != 9:
                toClick += 1

    for i in range(0, h):
        for j in range(0, w):
            if self.userField[i][j] == 'O':
                clicked += 1

    if toClick == clicked:
        self.enabledCheat = False
        tkinter.messagebox.showinfo("You win!", "Nice work, you win!")
        for x in self.buttons:
            x[0].unbind("<Button 1>")
            x[0].unbind("<Button 3>")
            if self.gameField[x[1][0]][x[1][1]] == 9:
                x[0].config(image=self.flagTile)
            else:
                x[0].config(image=self.nearbyTile[self.gameField[x[1][0]][x[1][1]]])