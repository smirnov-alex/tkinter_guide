# виджет checkbox

import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def toggle_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print('флажок 18', over_18_value.get())
    print('флажок реклама', commercial_value.get())


win = tk.Tk()
over_18_value = tk.StringVar()
over_18_value.set('No')
commercial_value = tk.IntVar()
win.geometry(f'800x600+100+200')
win.title('Tkinter Guide')
win.config(bg='#00b5ef')

over_18 = tk.Checkbutton(win, text='Мне есть 18', variable=over_18_value, onvalue='yes', offvalue='no')
commercial = tk.Checkbutton(win, text='Получать рассылку', variable=commercial_value, onvalue=1, offvalue=0)
follow = tk.Checkbutton(win, text='Подписаться на канал', indicatoron=False)
over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='select all', command=select_all).pack()
tk.Button(win, text='deselect all', command=deselect_all).pack()
tk.Button(win, text='toggle all', command=toggle_all).pack()
tk.Button(win, text='Show', command=show).pack()

win.mainloop()
