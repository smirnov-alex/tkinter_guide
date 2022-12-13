# введение в TKinter

import tkinter as tk

# инициализация главного окна
win = tk.Tk()
h = 500
w = 600
# иконка главного окна
icon = tk.PhotoImage(file='Radiotower.png')
win.iconphoto(False, icon)
# заголовок главного окна
win.title('Simply RET 2.0')
# размеры окна и положение окна на экране
win.geometry(f'{h}x{w}+10+10')
# изменение размеров окна по ширине и высоте
win.resizable(True, True)
# задать максимальные и минимальные размеры окна
win.minsize(300, 400)
win.maxsize(800, 600)
# фоновый цвет окна
win.config(bg='#00b5ef')
# бесконченый цикл главного окна
win.mainloop()
