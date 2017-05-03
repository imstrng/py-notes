from tkinter import *


root = Tk()

def printName():
    print('This is a test')



def doSomething(event):
    print('something . . . something')


button_1 = Button(root, text="Print something", command=printName)
button_1.pack()


button_2 = Button(root, text="Do something")
button_2.bind("<Button-1>",doSomething)
button_2.pack()


root.mainloop()


