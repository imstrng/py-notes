from tkinter import *



def doNothing():
    print("ok ok ok doing nothing . . . .")







root = Tk()

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)
edit = Menu(menu)
hhelp = Menu(menu)

menu.add_cascade(label="File", menu=file)
menu.add_cascade(label="Edit", menu=edit)
menu.add_cascade(label="Help", menu=hhelp)

file.add_command(label="Now project . . ", command=doNothing)
file.add_command(label="New", command=doNothing)
file.add_separator()
file.add_command(label="Exit", command=doNothing)

edit.add_command(label="Redo", command=doNothing)
edit.add_command(label="Undo", command=doNothing)

hhelp.add_command(label="About", command=doNothing)


root.mainloop()



