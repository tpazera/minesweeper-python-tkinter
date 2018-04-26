from src.game import *

app = 0

def loadInterface():
    global app
    app = App()
    app.mainloop()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Saper - Tomasz Pazera")
        self.resizable(False, False)
        self.geometry("{}x{}".format(460,600))
        self.changeWindow(StartPage)

    def changeWindow(self, frame):
        newFrame = frame(self)
        if hasattr(self, "_frame"):
            self._frame.destroy()
        self._frame = newFrame
        self._frame.grid(padx=25, pady=25)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wrapperFrame = tk.Frame(self)
        wrapperFrame.grid()
        tk.Message(wrapperFrame, text="Saper!\nTomasz Pazera", justify="center", font="System 14 bold", aspect=500).grid(row=0, column=0, pady=(0, 20))
        tk.Button(wrapperFrame, text="Start", command=lambda: master.changeWindow(GamePage)).grid(row=1, column=0, pady=(0, 20)) #lambda #3
        tk.Button(wrapperFrame, text="Ranking", command=lambda: master.changeWindow(RankingPage)).grid(row=2, column=0, pady=(0, 20)) #lambda #4
        tk.Button(wrapperFrame, text="Credits", command=lambda: master.changeWindow(CreditsPage)).grid(row=3, column=0, pady=(0, 20)) #lambda #5
        tk.Button(wrapperFrame, text="Quit", command=self.master.destroy).grid(row=4, column=0, columnspan=15, pady=(0, 30))
        tk.Label(wrapperFrame, width=50).grid()


class GamePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wrapperFrame = tk.Frame(self)
        wrapperFrame.grid()

        formFrame = tk.Frame(wrapperFrame)
        formFrame.grid(row=0, column=0)

        gameFrame = tk.Frame(wrapperFrame)
        gameFrame.grid(row=1, column=0)


        footerFrame = tk.Frame(wrapperFrame)
        footerFrame.grid(row=2, column=0)

        heightFrame = tk.Frame(formFrame)
        heightFrame.grid(row=0, column=0)
        heightLabel = tk.Label(heightFrame, text="Height: ", width=6).grid(row=0, column=0, padx=5, pady=5)
        heightEntry = tk.Entry(heightFrame)
        heightEntry.insert(tk.END, '10')
        heightEntry.grid(row=0, column=1, padx=5)

        widthFrame = tk.Frame(formFrame)
        widthFrame.grid(row=1, column=0)
        widthLabel = tk.Label(widthFrame, text="Width: ", width=6).grid(row=1, column=0, padx=5, pady=5)
        widthEntry = tk.Entry(widthFrame)
        widthEntry.insert(tk.END, '10')
        widthEntry.grid(row=1, column=1, padx=5)

        bombFrame = tk.Frame(formFrame)
        bombFrame.grid(row=2, column=0)
        bombLabel = tk.Label(bombFrame, text="Mines: ", width=6).grid(row=2, column=0, padx=5, pady=5)
        bombEntry = tk.Entry(bombFrame)
        bombEntry.insert(tk.END, '20')
        bombEntry.grid(row=2, column=1, padx=5)

        radio1 = tk.Radiobutton(formFrame, text="Custom", value=1, command = lambda : self.changeDifficulty(1, heightEntry, widthEntry, bombEntry)) #lambda #6
        radio1.grid(row=0, column=2)
        radio2 = tk.Radiobutton(formFrame, text="Begginer", value=2, command=lambda: self.changeDifficulty(2, heightEntry, widthEntry, bombEntry)).grid(row=1, column=2) #lambda #7
        radio3 = tk.Radiobutton(formFrame, text="Intermediate", value=3, command=lambda: self.changeDifficulty(3, heightEntry, widthEntry, bombEntry)).grid(row=2, column=2) #lambda #8
        radio4 = tk.Radiobutton(formFrame, text="Expert", value=4, command=lambda: self.changeDifficulty(4, heightEntry, widthEntry, bombEntry)).grid(row=3, column=2) #lambda #9
        radio1.invoke()

        startButton = tk.Button(formFrame, text="Start", command=lambda: self.startGame(heightEntry.get(), widthEntry.get(), bombEntry.get(), gameFrame)).grid(row=4, column=0, columnspan=3,  padx=5, pady=(5, 15))  #lambda #10

        returnButton = tk.Button(footerFrame, text="Return to start page", command=lambda: master.changeWindow(StartPage)).grid(row=3, column=0, columnspan=2, padx=5, pady=15)  #lambda #11

        tk.Label(wrapperFrame, width=50).grid()
        tk.Label(gameFrame).grid(column=0, row=0)

    def startGame(self, h, w, b, gameFrame):
        print("H:", h, "W:", w, "B:", b)
        global app
        try: #exception #1
            game = Game("Minesweeper")
            game.checkParameters(int(h), int(w), int(b), gameFrame, app)
        except ValueError:
            tk.messagebox.showinfo("Bad parameters", "Please input a valid size of a board and a number of mines!")

    def changeDifficulty(self, x, he, we, be):
        he.config(state='normal')
        we.config(state='normal')
        be.config(state='normal')
        he.delete(0, tk.END)
        we.delete(0, tk.END)
        be.delete(0, tk.END)
        if x == 1:
            he.insert(0, '10')
            we.insert(0, '10')
            be.insert(0, '20')
        else:
            if x == 2:
                he.insert(0, '5')
                we.insert(0, '5')
                be.insert(0, '10')
            elif x == 3:
                he.insert(0, '10')
                we.insert(0, '10')
                be.insert(0, '25')
            elif x == 4:
                he.insert(0, '15')
                we.insert(0, '15')
                be.insert(0, '50')
            he.config(state='disabled')
            we.config(state='disabled')
            be.config(state='disabled')


class RankingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wrapperFrame = tk.Frame(self)
        wrapperFrame.grid()
        underWorking = tk.Label(wrapperFrame, text="Not ready yet!")
        underWorking.grid(row=0,column=0)
        returnButton = tk.Button(wrapperFrame, text="Return to start page", command=lambda: master.changeWindow(StartPage)) #lambda #12
        returnButton.grid(row=1,column=0)
        tk.Label(wrapperFrame, width=50).grid()



class CreditsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        wrapperFrame = tk.Frame(self)
        wrapperFrame.grid()
        informationLabel = tk.Label(wrapperFrame, text="Saper - projekt zaliczeniowy\nPrzedmiot: Języki symboliczne\nAutor: Tomasz Pazera, gl06, Informatyka II rok")
        informationLabel.grid(row=0,column=0)
        returnButton = tk.Button(wrapperFrame, text="Return to start page", command=lambda: master.changeWindow(StartPage)) #lambda #13
        returnButton.grid(row=1,column=0)
        tk.Label(wrapperFrame, width=50).grid()
