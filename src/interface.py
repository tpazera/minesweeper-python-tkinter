import tkinter as tk
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
        #self.tk_setPalette(background='#333')
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
        tk.Button(wrapperFrame, text="Start", command=lambda: master.changeWindow(GamePage)).grid(row=1, column=0, pady=(0, 20)) #lambda #1
        tk.Button(wrapperFrame, text="Settings", command=lambda: master.changeWindow(SettingsPage)).grid(row=2, column=0, pady=(0, 20)) #lambda #2
        tk.Button(wrapperFrame, text="Credits", command=lambda: master.changeWindow(GamePage)).grid(row=3, column=0, pady=(0, 20)) #lambda #3
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

        radio1 = tk.Radiobutton(formFrame, text="Custom", value=1, command = lambda : self.changeDifficulty(1, heightEntry, widthEntry, bombEntry))
        radio1.grid(row=0, column=2)
        radio2 = tk.Radiobutton(formFrame, text="Begginer", value=2, command=lambda: self.changeDifficulty(2, heightEntry, widthEntry, bombEntry)).grid(row=1, column=2)
        radio3 = tk.Radiobutton(formFrame, text="Intermediate", value=3, command=lambda: self.changeDifficulty(3, heightEntry, widthEntry, bombEntry)).grid(row=2, column=2)
        radio4 = tk.Radiobutton(formFrame, text="Expert", value=4, command=lambda: self.changeDifficulty(4, heightEntry, widthEntry, bombEntry)).grid(row=3, column=2)
        radio1.invoke()

        startButton = tk.Button(formFrame, text="Start", command=lambda: self.startGame(heightEntry.get(), widthEntry.get(), bombEntry.get(), gameFrame)).grid(row=4, column=0, columnspan=3,  padx=5, pady=(5, 15))  #lambda #4

        returnButton = tk.Button(footerFrame, text="Return to start page", command=lambda: master.changeWindow(StartPage)).grid(row=3, column=0, columnspan=2, padx=5, pady=15)  #lambda #5

        tk.Label(wrapperFrame, width=50).grid()
        tk.Label(gameFrame, height=25).grid(column=0, row=0)

    def startGame(self, h, w, b, gameFrame):
        print("H:", h, "W:", w, "B:", b)
        global app
        try: #exception #1
            checkParameters(int(h), int(w), int(b), gameFrame, app)
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


class SettingsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_2_label = tk.Label(self, text="This is page two")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: master.changeWindow(StartPage))
        page_2_label.grid()
        start_button.grid()
