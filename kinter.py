import tkinter as tk
from subprocess import call
import os
root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()
root.title("Start Backend Module")



def caller():
    label1 = tk.Label(root, text='Running ...', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    os.chdir('../')
    call(["python",os.path.join(os.getcwd(),'fuprox_desktop_backend','app.py')])
    return {}


button1 = tk.Button(text='Start Backend Module', command=caller, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
