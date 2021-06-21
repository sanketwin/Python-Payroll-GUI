from tkinter import *

root = Tk()

root.title("My first GUI")


root.geometry("1600x900+0+0")
Frame1 = Frame(root, bd=3, relief=RIDGE, bg="white").place(
    x=10, y=70, width=900, height=680)

title = Label(Frame1, text="Employee Details").place(x=0, y=0, relwidth=1)

root.mainloop()
