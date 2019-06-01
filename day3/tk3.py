import tkinter
win = tkinter.Tk()
objw = tkinter.Canvas(win, width=40, height = 60)
objw.pack()
c_height = 20
c_width = 200
c_y = c_height/2
objw.create_line(0, c_y, c_width, c_y)
#button = tkinter.Button(win, text="hey", width=30)
#button.pack()
win.mainloop()
