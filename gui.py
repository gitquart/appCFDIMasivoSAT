import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
#geometry=widthxheight
root.geometry('600x600')
root.title('Quart CFDI Wizard')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
fConfiguración = ttk.Frame(notebook, width=590, height=590)
fProceso = ttk.Frame(notebook, width=590, height=590)

fConfiguración.pack(fill='both', expand=True)
fProceso.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(fConfiguración, text='Coniguración')
notebook.add(fProceso, text='Proceso CFDI')


root.mainloop()