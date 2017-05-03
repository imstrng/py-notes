from tkinter import *


class BuckysButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

        self.printButton.pack()
        self.quitButton.pack()


    def printMessage(self):
        print("this works")






root = Tk()
b = BuckysButton(root)
root.mainloop()


