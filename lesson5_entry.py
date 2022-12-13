# виджет Entry

import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty entry')


def delete_entry():
    name.delete(0, tk.END)
    password.delete(0, tk.END)


def submit():
    print(name.get())
    print(password.get())
    delete_entry()


win = tk.Tk()
icon = tk.PhotoImage(file='Radiotower.png')
win.iconphoto(False, icon)
win.geometry(f'800x600+100+200')
win.title('Tkinter Guide')
win.config(bg='#00b5ef')
tk.Label(win, text='name', bg='#00b5ef').grid(row=0, column=0, stick='w')
tk.Label(win, text='password', bg='#00b5ef').grid(row=1, column=0, stick='w')
name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)
tk.Button(win, text='get', command=get_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=3, column=1, stick='we')
tk.Button(win, text='submit', command=submit).grid(row=4, column=1, stick='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'Alex')).grid(row=5, column=1, stick='we')

# параметры колонок и строк
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=150)

win.mainloop()
