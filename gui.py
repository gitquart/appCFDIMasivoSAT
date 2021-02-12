import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
#geometry=widthxheight
root.geometry('600x600')
root.resizable(width=False, height=False)
root.title('Quart CFDI Wizard')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
fConfiguración = ttk.Frame(notebook, width=590, height=590)
fProceso = ttk.Frame(notebook, width=590, height=590)

fConfiguración.pack(fill='both', expand=True)
fProceso.pack(fill='both', expand=True)

#Add content to Configuración

GLabel_478=tk.Label(root)
ft = tkFont.Font(size=10)
GLabel_478["font"] = ft
GLabel_478["fg"] = "#333333"
GLabel_478["justify"] = "center"
GLabel_478["text"] = "Instrucciones:"
GLabel_478.place(x=40,y=70,width=100,height=25)

#Instrucciones
GLabel_599=tk.Label(root)
ft = tkFont.Font(size=10)
GLabel_599["font"] = ft
GLabel_599["fg"] = "#333333"
GLabel_599["justify"] = "center"
GLabel_599["text"] = "Establece el directorio donde estarán los archivos FIEL, descarga y lectura de cfdi.zip"
GLabel_599.place(x=40,y=100,width=500,height=80)




GLabel_883=tk.Label(root)
ft = tkFont.Font(size=10)
GLabel_883["font"] = ft
GLabel_883["fg"] = "#333333"
GLabel_883["justify"] = "center"
GLabel_883["text"] = "Directorio:"
GLabel_883.place(x=70,y=170,width=100,height=30)

GLineEdit_878=tk.Entry(root)
GLineEdit_878["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
GLineEdit_878["font"] = ft
GLineEdit_878["fg"] = "#333333"
GLineEdit_878["justify"] = "left"
GLineEdit_878["text"] = "Entry"
GLineEdit_878.place(x=160,y=170,width=272,height=30)

# add frames to notebook
notebook.add(fConfiguración, text='Coniguración')
notebook.add(fProceso, text='Proceso CFDI')


root.mainloop()