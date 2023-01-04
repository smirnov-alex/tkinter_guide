import tkinter as tk
import time
import threading

window = tk.Tk()


def start_threading():
    button_1.config(state=tk.DISABLED)
    thread = threading.Thread(target=say_hello)
    print(threading.main_thread().name)
    print(thread.name)
    thread.start()
    button_1.config(state=tk.NORMAL)


def say_hello():
    time.sleep(10)
    print('Hello')

button_1 = tk.Button(window, text='Сказать "Привет" через 10 секунд', command=start_threading)
button_1.grid(row=0, column=0, padx=20, pady=20)

window.mainloop()

