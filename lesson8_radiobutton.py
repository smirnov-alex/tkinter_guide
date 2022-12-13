# виджет radiobutton

import tkinter as tk

nations = {
    4: 'Эльфы',
    5: 'Люди',
    6: 'Орки',
}
def select_level():
    level = level_var.get()
    s = f'Вы выбрали {level} уровень'
    level_text.set(s)
    if level == 1:
        print('Easy')
    elif level == 2:
        print('Middle')
    elif level == 3:
        print('Hard')

def select_nation():
    nation = nation_var.get()
    nation_text.set(f'Вы выбрали расу {nations[nation]}')
    print(nations[nation])

win = tk.Tk()
win.geometry(f'800x600+100+200')
win.title('Tkinter Guide')
win.config(bg='#00b5ef')

level_var = tk.IntVar()
nation_var = tk.IntVar()
level_text = tk.StringVar()
nation_text = tk.StringVar()
tk.Label(win, text='Выберите уровень сложности').pack()
tk.Radiobutton(win, text='Easy', variable=level_var, value=1, command=select_level).pack()
tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_level).pack()
tk.Radiobutton(win, text='Hard', variable=level_var, value=3, command=select_level).pack()
tk.Label(win, textvariable=level_text).pack()

tk.Label(win, text='Выберите расу').pack()
for nation in sorted(nations):
    tk.Radiobutton(win, text=nations[nation], variable=nation_var, value=nation, command=select_nation).pack()
tk.Label(win, textvariable=nation_text).pack()

win.mainloop()
