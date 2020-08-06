import tkinter as app
from tkinter import filedialog, Text
import os

root = app.Tk()

# boundaries for our app
canvas = app.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

# a frame where we can input something
frame = app.Frame(root, bg="pink")
frame.place(relwidth=1, relheight=0.1)




root.mainloop()