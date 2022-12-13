# виджет radiobutton

import tkinter as tk
from tkinter import ttk


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'


def show_day():
    print(combo.get(), combo_int.get())


def set_day():
    combo.set('Friday')

weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
list_int = [1, 2, 3, 4, 5, 6, 7]

win = tk.Tk()
win.geometry(f'800x600+100+200')
win.title('Tkinter Guide')
win.config(bg='#00b5ef')

combo = ttk.Combobox(win, values=weekDays)
combo.current(0)
combo.pack()

combo_int = ttk.Combobox(win, values=list_int)
combo_int.current(0)
combo_int.pack()

combo_point = ttk.Combobox(win, values=[Point(2,5), Point(1,4)])
combo_point.pack()

ttk.Button(win, text='show day', command=show_day).pack()
ttk.Button(win, text='set day', command=set_day).pack()

win.mainloop()
