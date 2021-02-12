import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk,filedialog
import tkinter.messagebox as tkMessageBox
import tkinter as tk
from tkinter import ttk

def returnFolder():
    folderSelected=filedialog.askdirectory()
    txtDir.delete(0,tk.END)
    txtDir.insert(0,folderSelected)

def showMessage(title,content):
    tkMessageBox.showinfo(title,content)


# window window
window = tk.Tk()
#geometry=widthxheight
window.geometry('600x600')
window.resizable(width=False, height=False)
window.title('Quart CFDI Wizard')

# create a notebook
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)
notebook.pack()

# create frames
fConfiguración = ttk.Frame(notebook, width=590, height=590)
fProceso = ttk.Frame(notebook, width=590, height=590)

fConfiguración.pack(fill='both', expand=True)
fProceso.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(fConfiguración, text='Coniguración')
notebook.add(fProceso, text='Proceso CFDI')

#Add content to Configuración

#Título-Instrucciones
lblInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblInst["font"] = ft
lblInst["fg"] = "#333333"
lblInst["justify"] = "center"
lblInst["text"] = "Instrucciones:"
lblInst.place(x=40,y=70,width=100,height=25)
  
#Contenido-Instrucciones
lblContInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblContInst["font"] = ft
lblContInst["fg"] = "#333333"
lblContInst["justify"] = "left"
lblContInst["text"] = "Establece el directorio donde estarán los archivos FIEL, descarga y lectura de cfdi.zip"
lblContInst.place(x=45,y=100,width=500,height=20)
  
#lbl-Directorio
lblDir=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblDir["font"] = ft
lblDir["fg"] = "#333333"
lblDir["justify"] = "center"
lblDir["text"] = "Directorio:"
lblDir.place(x=70,y=140,width=100,height=30)
    
#Caja de texto-directorio
txtDir=tk.Entry(fConfiguración)
txtDir["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtDir["font"] = ft
txtDir["fg"] = "#333333"
txtDir["justify"] = "left"
txtDir.place(x=160,y=140,width=272,height=30)
#txtDir.insert(0,'Hola')
    
#Browser-directorio
btnBrowser=tk.Button(fConfiguración,command=returnFolder)
btnBrowser['text']='...'
btnBrowser.place(x=440,y=140,width=50,height=30)
    
window.mainloop()


  