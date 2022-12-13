# Виджет Button
import tkinter as tk
import random


def say_hello():
    print('hello')


def add_label():
    label = tk.Label(win, text='new label')
    label.pack()


def counter():
    global count
    count += 1
    button_4['text'] = f'Счетчик: {count}'

count = 0
colors = ['#00b5ef', '#ff59a3', '#c3e400', '#ff6633', '#ffaf0f', '#1ee7ca', '#c882ff']

win = tk.Tk()
icon = tk.PhotoImage(file='Radiotower.png')
win.iconphoto(False, icon)
win.geometry(f'300x400+100+200')
win.title('Tkinter Guide')
win.config(bg='#00b5ef')

button_1 = tk.Button(win, text='HELLO',
                     command=say_hello)
button_2 = tk.Button(win, text='add new label',
                     command=add_label)
button_3 = tk.Button(win, text='Цвет фона',
                     command=lambda: win.config(bg=random.choice(colors)))
button_4 = tk.Button(win, text=f'Счетчик: {count}',
                     command=counter,
                     activebackground='blue',
                     bg='red',
                     state=tk.NORMAL)

button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()

win.mainloop()
