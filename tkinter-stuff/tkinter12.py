from tkinter import *
import tkinter.messagebox

root = Tk()



tkinter.messagebox.showinfo('Windo Title', 'Monkeys can live up to 300 years')


answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print('You clicked: yes')
else:
    print('You clicked: no')


root.mainloop()



































