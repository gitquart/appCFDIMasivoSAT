import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk,filedialog
import tkinter.messagebox as tkMessageBox
import tkinter as tk
from tkinter import ttk

from requests.api import get
import utils as tool
import datetime


def returnFolder():
    folderSelected=filedialog.askdirectory()
    txtDir.delete(0,tk.END)
    txtDir.insert(0,folderSelected)

def showMessage(title,content):
    tkMessageBox.showinfo(title=title,message=content)

def solicitarCFDI():
    fechaInicio=txtFechaInicio.get()
    fechaFin=txtFechaFin.get()
    fecha_inicial = datetime.datetime(2015, 1, 1)
    fecha_final = datetime.datetime(2015, 12, 31)
    lsvalor=[]
    lsvalor=tool.solicitaDescarga(fecha_inicial,fecha_final)
    showMessage('Mensaje','hOLA')

def verificarCFDI():
    showMessage('Mensaje','hOLA')

   



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
lblInst.place(x=40,y=30,width=100,height=25)
  
#Contenido-Instrucciones
lblContInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=9)
lblContInst["font"] = ft
lblContInst["fg"] = "#333333"
lblContInst["justify"] = "left"
texto="1.Crea una carpeta 'FIEL' con los siguientes archivos y elígela en el directorio debajo:\n\n"
texto+='A) Archivo *.cer\nB) Archivo *.key\nC) Archivo "datos.txt" donde debes anotar,en dos líneas, RFC y constreseña de FIEL\n'
lblContInst["text"] = texto
lblContInst.place(x=45,y=70,width=500,height=90)
  
#lbl-Directorio
posYDirectorio=170
lblDir=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblDir["font"] = ft
lblDir["fg"] = "#333333"
lblDir["justify"] = "center"
lblDir["text"] = "Directorio:"
lblDir.place(x=70,y=posYDirectorio,width=100,height=25)
    
#Caja de texto-directorio
txtDir=tk.Entry(fConfiguración)
txtDir["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtDir["font"] = ft
txtDir["fg"] = "#333333"
txtDir["justify"] = "left"
txtDir.place(x=160,y=posYDirectorio,width=272,height=25)
    
#Browser-directorio
btnBrowser=tk.Button(fConfiguración,command=returnFolder)
btnBrowser['text']='...'
btnBrowser.place(x=440,y=posYDirectorio,width=50,height=25)

#Contenido-Instrucciones 2
lblContInst2=tk.Label(fConfiguración)
ft = tkFont.Font(size=9)
lblContInst2["font"] = ft
lblContInst2["fg"] = "#333333"
lblContInst2["justify"] = "left"
texto='2. Introducir el rango de fechas del CFDI a recuperar\n'
texto+='3. Hacer click en el botón "Soicitar CFDI" y sigue los mensajes posteriores\n\n'
texto+='Escribe las fechas en formato dd/mm/yyyy'
lblContInst2["text"] = texto
lblContInst2.place(x=20,y=195,width=500,height=120)

#Rango de fechas
#lbl Inicial
posYFechaInicial=300
lblFechaInicio=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblFechaInicio["font"] = ft
lblFechaInicio["fg"] = "#333333"
lblFechaInicio["justify"] = "left"
lblFechaInicio["text"] = "Fecha inicial:"
lblFechaInicio.place(x=50,y=posYFechaInicial,width=100,height=25)

#Caja de texto-fecha inicio
txtFechaInicio=tk.Entry(fConfiguración)
txtFechaInicio["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtFechaInicio["font"] = ft
txtFechaInicio["fg"] = "#333333"
txtFechaInicio["justify"] = "left"
txtFechaInicio.place(x=150,y=posYFechaInicial,width=100,height=25)

#lbl Final
posYFechaFin=330
lblFechaFin=tk.Label(fConfiguración)
ft = tkFont.Font(size=10)
lblFechaFin["font"] = ft
lblFechaFin["fg"] = "#333333"
lblFechaFin["justify"] = "left"
lblFechaFin["text"] = "Fecha fin:"
lblFechaFin.place(x=60,y=posYFechaFin,width=100,height=25)

#Caja de texto-fecha fin
txtFechaFin=tk.Entry(fConfiguración)
txtFechaFin["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtFechaFin["font"] = ft
txtFechaFin["fg"] = "#333333"
txtFechaFin["justify"] = "left"
txtFechaFin.place(x=150,y=posYFechaFin,width=100,height=25)

#Btn solicitar
btnSolicitar=tk.Button(fConfiguración,command=solicitarCFDI,text='Solicitar CFDI')
btnSolicitar.place(x=110,y=380,width=100,height=25)

#ID's respuesta de solicitud
#LBL ID1
posYID1=420
ft = tkFont.Font(size=10)
lblID1=tk.Label(fConfiguración)
lblID1["font"] = ft
lblID1["fg"] = "#333333"
lblID1["justify"] = "left"
lblID1["text"] = "ID Solicitud 1:"
lblID1.place(x=50,y=posYID1,width=100,height=25)

#Caja de texto ID 1
txtID1=tk.Entry(fConfiguración)
txtID1["borderwidth"] = "1px"
txtID1["font"] = ft
txtID1["fg"] = "#333333"
txtID1["justify"] = "left"
txtID1.place(x=150,y=posYID1,width=170,height=25)

#lbl ID 2
posYID2=450
lblID2=tk.Label(fConfiguración)
lblID2["font"] = ft
lblID2["fg"] = "#333333"
lblID2["justify"] = "left"
lblID2["text"] = "ID Solicitud 2:"
lblID2.place(x=50,y=posYID2,width=100,height=25)

#Caja de texto-ID 2
txtID2=tk.Entry(fConfiguración)
txtID2["borderwidth"] = "1px"
txtID2["font"] = ft
txtID2["fg"] = "#333333"
txtID2["justify"] = "left"
txtID2.place(x=150,y=posYID2,width=170,height=25)

#Btn Verificar y descargar CFDI
btnVerificar=tk.Button(fConfiguración,command=verificarCFDI,text='Verificar y Descargar CFDI')
btnVerificar.place(x=350,y=380,width=150,height=25)

#Caja de texto-ID Verificación
txtIDVerificar=tk.Entry(fConfiguración)
txtIDVerificar["borderwidth"] = "1px"
txtIDVerificar["font"] = ft
txtIDVerificar["fg"] = "#333333"
txtIDVerificar["justify"] = "left"
txtIDVerificar.place(x=350,y=420,width=170,height=25)

window.mainloop()


  