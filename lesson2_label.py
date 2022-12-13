# Виджет Label
import tkinter as tk
win = tk.Tk()
icon = tk.PhotoImage(file='Radiotower.png')
win.iconphoto(False, icon)
win.geometry(f'300x400+100+200')
win.title('Tkinter Guide')
win.config(bg='#00b5ef')

label_1 = tk.Label(win, text='Привет',
                   bg='#c3e400',
                   fg='#ffffff',       # цвет шрифта
                   font=('Arial', 14, 'bold'),  # параметры шрифта
                   # padx=20,          # внутренние паддинги (как в html)
                   # pady=40,          # внутренние паддинги (как в html)
                   width=10,           # указывается в кол-ве знаков
                   height=5,           # указывается в кол-ве знаков
                   anchor='center',    # привязка к краю (стороны света)
                   relief=tk.GROOVE,   # отображение границы (рамки)
                   bd=5,               # ширина рамки (border)
                   justify=tk.CENTER)  # выравнивание текста внутри
label_1.pack()

win.mainloop()
