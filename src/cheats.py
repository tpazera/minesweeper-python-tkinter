def cheat(self, event):
    if self.cheatIterator == 0:
        if event.char == 'x':
            self.cheatCode[self.cheatIterator] = event.char
            self.cheatIterator += 1
        else:
            self.cheatCode = [0, 0, 0, 0, 0]
            self.cheatIterator = 0
    elif self.cheatIterator == 1:
        if event.char == 'y':
            self.cheatCode[self.cheatIterator] = event.char
            self.cheatIterator += 1
        else:
            self.cheatCode = [0, 0, 0, 0, 0]
            self.cheatIterator = 0
    elif self.cheatIterator == 2:
        if event.char == 'z':
            self.cheatCode[self.cheatIterator] = event.char
            self.cheatIterator += 1
        else:
            self.cheatCode = [0, 0, 0, 0, 0]
            self.cheatIterator = 0
    elif self.cheatIterator == 3:
        if event.char == 'z':
            self.cheatCode[self.cheatIterator] = event.char
            self.cheatIterator += 1
        else:
            self.cheatCode = [0, 0, 0, 0, 0]
            self.cheatIterator = 0
    elif self.cheatIterator == 4:
        if event.char == 'y':
            self.cheatCode[self.cheatIterator] = event.char
            self.cheatIterator += 1
        else:
            self.cheatCode = [0, 0, 0, 0, 0]
            self.cheatIterator = 0

    print(self.cheatCode)
    if self.cheatCode == ['x', 'y', 'z', 'z', 'y']:
        if self.enabledCheat == False:
            self.enabledCheat = True
            self.cheatIterator = 0
            self.cheatCode = [0, 0, 0, 0, 0]
            for x in self.buttons:
                if self.gameField[x[1][0]][x[1][1]] == 9:
                    x[0].config(image=self.cheatTile)