from tkinter import *



def doNothing():
    print("ok ok ok doing nothing . . . .")


root = Tk()


# Menu

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
editMenu = Menu(menu)

menu.add_cascade(label="File", menu=subMenu)


subMenu.add_command(label="Now project . . ", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)





# Toolbar

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar,text="Insert image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)

printButt = Button(toolbar,text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()



































