import tkinter.messagebox
import tkinter as tk
import random

tileField, statusField, flagInfo, cheatTile, emptyTile, bombTile, pbombTile, flagTile, qmarkTile, nearbyTile, userField, gameField, buttons, bombs, generated, cheatCode, cheatIterator, enabledCheat = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, [0, 0, 0, 0, 0], 0, False #global variables (images, lists)
application = 0


def checkParameters(h, w, b, gameFrame, app):
    if h < 2 or w < 2 or h > 15 or w > 15 or b < 0 or b > h*w:
        tkinter.messagebox.showinfo("Bad parameters", "Please input a valid size of a board and a number of mines!")
    else:
        global tileField, userField, gameField, buttons, generated, application, enabledCheat, statusField, flagInfo
        gameFrame.focus_force()
        application = app
        loadImages()
        try: #exception #2
            tileField.destroy()
            statusField.destroy()
        except AttributeError:
            print("First launch!")
        tileField = tk.Frame(gameFrame)
        tileField.grid(row=1, column =0)
        userField, gameField = generateLists(h, w, b)
        buttons = generateTiles(h, w, tileField)
        statusField = tk.Frame(gameFrame)
        statusField.grid(row=0, column=0)
        mineInfo = tk.Label(statusField, text="Mines: " + str(b), width=10).grid(row=0, column=0, padx=5, pady=5)
        flagInfo = tk.Label(statusField, text="Flags: 0", width=10)
        flagInfo.grid(row=0, column=1, padx=5, pady=5)
        application.bind("<Key>", cheat)


def cheat(event):
    global cheatCode, cheatIterator, enabledCheat

    if cheatIterator == 0:
        if event.char == 'x':
            cheatCode[cheatIterator] = event.char
            cheatIterator += 1
        else:
            cheatCode = [0, 0, 0, 0, 0]
            cheatIterator = 0
    elif cheatIterator == 1:
        if event.char == 'y':
            cheatCode[cheatIterator] = event.char
            cheatIterator += 1
        else:
            cheatCode = [0, 0, 0, 0, 0]
            cheatIterator = 0
    elif cheatIterator == 2:
        if event.char == 'z':
            cheatCode[cheatIterator] = event.char
            cheatIterator += 1
        else:
            cheatCode = [0, 0, 0, 0, 0]
            cheatIterator = 0
    elif cheatIterator == 3:
        if event.char == 'z':
            cheatCode[cheatIterator] = event.char
            cheatIterator += 1
        else:
            cheatCode = [0, 0, 0, 0, 0]
            cheatIterator = 0
    elif cheatIterator == 4:
        if event.char == 'y':
            cheatCode[cheatIterator] = event.char
            cheatIterator += 1
        else:
            cheatCode = [0, 0, 0, 0, 0]
            cheatIterator = 0

    print(cheatCode)
    if cheatCode == ['x', 'y', 'z', 'z', 'y']:
        if enabledCheat == False:
            enabledCheat = True
            cheatIterator = 0
            cheatCode = [0, 0, 0, 0, 0]
            for x in buttons:
                if gameField[x[1][0]][x[1][1]] == 9:
                    x[0].config(image=cheatTile)


def loadImages():
    global emptyTile, bombTile, pbombTile, flagTile, qmarkTile, nearbyTile, cheatTile
    emptyTile = tk.PhotoImage(file="assets/empty.gif")
    bombTile = tk.PhotoImage(file="assets/bomb.gif")
    pbombTile = tk.PhotoImage(file="assets/pbomb.gif")
    flagTile = tk.PhotoImage(file="assets/flag.gif")
    qmarkTile = tk.PhotoImage(file="assets/qmark.gif")
    cheatTile = tk.PhotoImage(file="assets/cheat.gif")
    nearbyTile = [tk.PhotoImage(file = "assets/n" + str(i) + ".gif") for i in range (0,9)] #list comprehension #1
    print("Images loaded!")


def generateLists(h, w, b):
    global gameField, bombs
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
    bombs = b

    for i in range(0, h):
        for j in range(0, w):
            if gameField[i][j] != 9:
                if i == 0 and j == 0: #lewy górny kafelek
                    neighbours = 0
                    if findNeighbours(i, j + 1):
                        neighbours += 1
                    if findNeighbours(i + 1, j):
                        neighbours += 1
                    if findNeighbours(i + 1, j + 1):
                        neighbours += 1
                elif i == h-1 and j == w-1: #prawy dolny kafelek
                    neighbours = 0
                    if findNeighbours(i-1, j - 1):
                        neighbours += 1
                    if findNeighbours(i - 1, j):
                        neighbours += 1
                    if findNeighbours(i, j - 1):
                        neighbours += 1
                elif i == 0 and j == w-1: #prawy górny kafelek
                    neighbours = 0
                    if findNeighbours(i, j - 1):
                        neighbours += 1
                    if findNeighbours(i + 1, j - 1):
                        neighbours += 1
                    if findNeighbours(i + 1, j):
                        neighbours += 1
                elif i == h-1 and j == 0: #lewy dolny kafelek
                    neighbours = 0
                    if findNeighbours(i - 1, j):
                        neighbours += 1
                    if findNeighbours(i - 1, j + 1):
                        neighbours += 1
                    if findNeighbours(i, j + 1):
                        neighbours += 1
                else:
                    if i == 0: #pierwszy wiersz
                        neighbours = 0
                        if findNeighbours(i, j - 1):
                            neighbours += 1
                        if findNeighbours(i, j + 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j - 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j):
                            neighbours += 1
                        if findNeighbours(i + 1, j + 1):
                            neighbours += 1
                    elif i == h-1: #ostatni wiersz
                        neighbours = 0
                        if findNeighbours(i, j - 1):
                            neighbours += 1
                        if findNeighbours(i, j + 1):
                            neighbours += 1
                        if findNeighbours(i - 1, j - 1):
                            neighbours += 1
                        if findNeighbours(i - 1, j):
                            neighbours += 1
                        if findNeighbours(i - 1, j + 1):
                            neighbours += 1
                    elif j == 0: #pierwsza kolumna
                        neighbours = 0
                        if findNeighbours(i - 1, j):
                            neighbours += 1
                        if findNeighbours(i - 1, j + 1):
                            neighbours += 1
                        if findNeighbours(i, j + 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j):
                            neighbours += 1
                        if findNeighbours(i + 1, j + 1):
                            neighbours += 1
                    elif j == w-1: #ostatnia kolumna
                        neighbours = 0
                        if findNeighbours(i - 1, j - 1):
                            neighbours += 1
                        if findNeighbours(i - 1, j):
                            neighbours += 1
                        if findNeighbours(i, j - 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j - 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j):
                            neighbours += 1
                    else:
                        neighbours = 0
                        if findNeighbours(i - 1, j - 1):
                            neighbours += 1
                        if findNeighbours(i - 1, j):
                            neighbours += 1
                        if findNeighbours(i - 1, j + 1):
                            neighbours += 1
                        if findNeighbours(i, j - 1):
                            neighbours += 1
                        if findNeighbours(i, j + 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j - 1):
                            neighbours += 1
                        if findNeighbours(i + 1, j):
                            neighbours += 1
                        if findNeighbours(i + 1, j + 1):
                            neighbours += 1

                gameField[i][j] = neighbours

    for i in range(0, h):
        for j in range(0, w):
            print(gameField[i][j], end='')
        print("")

    return (userField,gameField)


def findNeighbours(x,y):
    try: #exception #3
        if gameField[x][y] == 9:
            return True
    except IndexError:
        pass


def generateTiles(h, w, tileField):
    buttons = []
    tileField.emptyTile = tk.PhotoImage(file="assets/empty.gif")
    for i in range(0, h):
        for j in range(0, w):
            buttonTMP = tk.Button(tileField, image=tileField.emptyTile, compound=tk.TOP, bg="grey")
            buttonTMP.bind('<Button-1>', leftClickLambda(i, j, w, h))
            buttonTMP.bind('<Button-3>', rightClickLambda(i, j, w, h))
            buttons.append([buttonTMP, (i, j)])
    for x in buttons:
        x[0].grid(row=x[1][0], column=x[1][1])
    return buttons


def leftClickLambda(i, j, w, h):
    return lambda Button: leftClick(i, j, w, h) #lambda #5


def rightClickLambda(i, j, w, h):
    return lambda Button: rightClick(i, j, w, h) #lambda #6


def leftClick(i, j, w, h):
    global emptyTile, bombTile, pbombTile, flagTile, qmarkTile, nearbyTile, enabledCheat
    if userField[i][j] != 'F' and userField[i][j] != 'Q':
        buttons[i * w + j][0].unbind("<Button 1>")
        buttons[i * w + j][0].unbind("<Button 3>")
        #buttons[i * w + j][0].configure(state=tk.DISABLED)
        if gameField[i][j] == 9:
            enabledCheat = False
            tkinter.messagebox.showinfo("You lose!", "Unfortunately you stop on a mine!")
            for x in buttons:
                x[0].unbind("<Button 1>")
                x[0].unbind("<Button 3>")
                if gameField[x[1][0]][x[1][1]] == 9:
                    x[0].config(image=pbombTile)
                else:
                    x[0].config(image=nearbyTile[gameField[x[1][0]][x[1][1]]])
            buttons[i * w + j][0].config(image=bombTile)
        elif gameField[i][j] == 0:
            checkEmptyNeigbours(i, j, w, h)
        else:
            userField[i][j] = 'O'
            buttons[i * w + j][0].config(image=nearbyTile[gameField[i][j]])
            checkForWin(w, h)
            checkForWin2(w, h)


def checkEmptyNeigbours(i, j, w, h):
    if i < 0 or j < 0 or i > h-1 or j > w-1 or userField[i][j] != 'X':
        return
    if gameField[i][j] == 0 and userField[i][j] != 'F':
        userField[i][j] = 'O'
        buttons[i * w + j][0].config(image=nearbyTile[0])
        buttons[i * w + j][0].unbind("<Button 1>")
        buttons[i * w + j][0].unbind("<Button 3>")
        #buttons[i * w + j][0].configure(state=tk.DISABLED)
        checkEmptyNeigbours(i, j - 1, w, h)
        checkEmptyNeigbours(i - 1, j, w, h)
        checkEmptyNeigbours(i + 1, j, w, h)
        checkEmptyNeigbours(i, j + 1, w, h)
    elif userField[i][j] != 'F':
        userField[i][j] = 'O'
        buttons[i * w + j][0].config(image=nearbyTile[gameField[i][j]])
        buttons[i * w + j][0].unbind("<Button 1>")
        buttons[i * w + j][0].unbind("<Button 3>")
        #buttons[i * w + j][0].configure(state=tk.DISABLED)


def rightClick(i, j, w, h):
    global enabledCheat, statusField, flagInfo
    if userField[i][j] == 'X':
        userField[i][j] = 'F'
        buttons[i * w + j][0].config(image=flagTile)
        countFlags = 0
        for i in range(0, h):
            for j in range(0, w):
                if userField[i][j] == 'F':
                    countFlags += 1
        flagInfo.config(text='Flags: '+str(countFlags))
    elif userField[i][j] == 'F':
        userField[i][j] = 'Q'
        buttons[i * w + j][0].config(image=qmarkTile)
        countFlags = 0
        for i in range(0, h):
            for j in range(0, w):
                if userField[i][j] == 'F':
                    countFlags += 1
        flagInfo.config(text='Flags: ' + str(countFlags))
    elif userField[i][j] == 'Q':
        userField[i][j] = 'X'
        if enabledCheat:
            buttons[i * w + j][0].config(image=cheatTile)
        else:
            buttons[i * w + j][0].config(image=emptyTile)
    checkForWin(w, h)
    checkForWin2(w, h)

def checkForWin(w, h):
    global enabledCheat
    correct, flags = 0, 0
    for i in range(0, h):
        for j in range(0, w):
            if userField[i][j] == 'F' and gameField[i][j] == 9:
                correct += 1
            if userField[i][j] == 'F':
                flags += 1
    if correct == bombs and bombs == flags:
        enabledCheat = False
        tkinter.messagebox.showinfo("You win!", "Nice work, you win!")
        for x in buttons:
            x[0].unbind("<Button 1>")
            x[0].unbind("<Button 3>")
            if gameField[x[1][0]][x[1][1]] == 9:
                x[0].config(image=flagTile)
            else:
                x[0].config(image=nearbyTile[gameField[x[1][0]][x[1][1]]])

def checkForWin2(w, h):
    global enabledCheat
    toClick = 0
    clicked = 0
    for i in range(0, h):
        for j in range(0, w):
            if gameField[i][j] != 9:
                toClick += 1

    for i in range(0, h):
        for j in range(0, w):
            if userField[i][j] == 'O':
                clicked += 1

    if toClick == clicked:
        enabledCheat = False
        tkinter.messagebox.showinfo("You win!", "Nice work, you win!")
        for x in buttons:
            x[0].unbind("<Button 1>")
            x[0].unbind("<Button 3>")
            if gameField[x[1][0]][x[1][1]] == 9:
                x[0].config(image=flagTile)
            else:
                x[0].config(image=nearbyTile[gameField[x[1][0]][x[1][1]]])
