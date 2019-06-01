import tkinter as tk
win = tk.Tk()
tk.Label(win, text= 'First Name').grid(row = 0)
tk.Label(win, text= 'Last Name').grid(row = 1)

e1 = tk.Entry(win)
e2 = tk.Entry(win)

e1.grid(row=0, column = 1)
e2.grid(row=1, column = 1)

win.mainloop()
