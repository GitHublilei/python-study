from tkinter import *

top = Tk()


def clicked():
    print('I was clicked!')


def callback(event):
    print(event.x, event.y)


top.bind('<Button-1>', callback)

Button(text='Click me too!', command=clicked).pack()

Label(text="I'm in the first window!").pack()

second = Toplevel()

Label(second, text="I'm in the second window!").pack()

for i in range(10):
    Button(text=i).pack()

help(Pack.config)

mainloop()
