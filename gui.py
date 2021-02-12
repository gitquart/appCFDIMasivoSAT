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
    tkMessageBox.showinfo(title=title,message=content)

def solicitarCFDI():
    
    showMessage('Mensaje','')



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

fConfiguración.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(fConfiguración, text='Configuración y proceso CFDI')

#Add content to Configuración

#Título-Instrucciones
lblInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblInst["font"] = ft
lblInst["fg"] = "#333333"
lblInst["justify"] = "center"
lblInst["text"] = "Instrucciones:"
lblInst.place(x=40,y=70,width=100,height=25)
  
#Contenido-Instrucciones
lblContInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=9)
lblContInst["font"] = ft
lblContInst["fg"] = "#333333"
lblContInst["justify"] = "left"
texto="1.Establece el directorio donde estarán los archivos FIEL, descarga y lectura de cfdi.zip"
lblContInst["text"] = texto
lblContInst.place(x=45,y=100,width=500,height=25)
  
#lbl-Directorio
lblDir=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblDir["font"] = ft
lblDir["fg"] = "#333333"
lblDir["justify"] = "center"
lblDir["text"] = "Directorio:"
lblDir.place(x=70,y=140,width=100,height=25)
    
#Caja de texto-directorio
txtDir=tk.Entry(fConfiguración)
txtDir["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtDir["font"] = ft
txtDir["fg"] = "#333333"
txtDir["justify"] = "left"
txtDir.place(x=160,y=140,width=272,height=25)
    
#Browser-directorio
btnBrowser=tk.Button(fConfiguración,command=returnFolder)
btnBrowser['text']='...'
btnBrowser.place(x=440,y=140,width=50,height=25)

#Contenido-Instrucciones 2
lblContInst2=tk.Label(fConfiguración)
ft = tkFont.Font(size=9)
lblContInst2["font"] = ft
lblContInst2["fg"] = "#333333"
lblContInst2["justify"] = "left"
texto='2. Dentro del directorio elegido, crea la carpeta "FIEL" con los siguientes archivos:\n\n'
texto+='A) Archivo *.cer\nB) Archivo *.key\nC) Archivo "datos.txt" donde debes anotar,en dos líneas, RFC y constreseña de FIEL\n\n'
texto+='3. Introducir el rango de fechas del CFDI a recuperar\n'
texto+='4. Hacer click en el botón "Soicitar CFDI" y sigue los mensajes posteriores'
lblContInst2["text"] = texto
lblContInst2.place(x=40,y=200,width=500,height=120)

#Rango de fechas
#lbl Inicial
lblFechaInicio=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblFechaInicio["font"] = ft
lblFechaInicio["fg"] = "#333333"
lblFechaInicio["justify"] = "left"
lblFechaInicio["text"] = "Fecha inicial:"
lblFechaInicio.place(x=50,y=340,width=100,height=25)

#Caja de texto-fecha inicio
txtFechaInicio=tk.Entry(fConfiguración)
txtFechaInicio["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtFechaInicio["font"] = ft
txtFechaInicio["fg"] = "#333333"
txtFechaInicio["justify"] = "left"
txtFechaInicio.place(x=150,y=340,width=100,height=25)

#lbl Final
lblFechaFin=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblFechaFin["font"] = ft
lblFechaFin["fg"] = "#333333"
lblFechaFin["justify"] = "left"
lblFechaFin["text"] = "Fecha fin:"
lblFechaFin.place(x=60,y=380,width=100,height=25)

#Caja de texto-fecha fin
txtFechaFin=tk.Entry(fConfiguración)
txtFechaFin["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtFechaFin["font"] = ft
txtFechaFin["fg"] = "#333333"
txtFechaFin["justify"] = "left"
txtFechaFin.place(x=150,y=380,width=100,height=25)

#Btn solicitar
btnSolicitar=tk.Button(fConfiguración,command=solicitarCFDI,text='Solicitar CFDI')
btnSolicitar.place(x=230,y=420,width=100,height=25)


    
window.mainloop()


  