import tkinter as tk
from tkinter.constants import ACTIVE
import tkinter.font as tkFont
from tkinter import ttk,filedialog
import tkinter.messagebox as tkMessageBox
import tkinter as tk
from tkinter import ttk
import utils as tool
import datetime
from InternalControl import cInternalControl
import sys

objControl=cInternalControl()

VERSION='SQL'

def returnFolder():
    folderSelected=filedialog.askdirectory()
    txtDir.delete(0,tk.END)
    txtDir.insert(0,folderSelected)


def showMessage(title,content):
    tkMessageBox.showinfo(title=title,message=content)

def preguntaSolicitarCFDI():
    fechaInicio=txtFechaInicio.get()
    fechaFin=txtFechaFin.get()
    directory=txtDir.get()
    if fechaInicio!='' and fechaFin!='' and directory!='' :
        res=tkMessageBox.askyesno(title='Advertencia',message='El procedimiento "Solicitar CFDI" sólo se puede hacer una vez.\n ¿Deseas continuar?')
        if res:
            try:
                solicitarCFDI()
            except:
                showMessage('Error: ',sys.exc_info()[0])    

    else:
        showMessage('Mensaje','Por favor, verifica que las fechas o el directorio no estén vacíos')    

def solicitarCFDI():
    #Dates on txtDates : dd/mm/yyyy
    #lsFolderName saves importantd data along its way to name the folder where the zip and xls will be saved
    #lsFolder elements (by order):[tipo,fechaCompleta,rfc_solicitante,fileName] 
    fechaInicio=txtFechaInicio.get()
    fechaFin=txtFechaFin.get()
    directory=txtDir.get()
    tipo=var.get()
    chunksFI=fechaInicio.split('/')
    chunksFF=fechaFin.split('/')
    fecha_inicial = datetime.datetime(int(chunksFI[2]), int(chunksFI[1]), int(chunksFI[0]))
    fecha_final = datetime.datetime(int(chunksFF[2]),int(chunksFF[1]),int(chunksFF[0]))
    strFechaInicial=str(fecha_inicial.day)+str(fecha_inicial.month)+str(fecha_inicial.year)
    strFechaFin=str(fecha_final.day)+str(fecha_final.month)+str(fecha_final.year)
    strFechaCompleta=strFechaInicial+'_'+strFechaFin
    res=tool.solicitaDescarga(fecha_inicial,fecha_final,directory,tipo,strFechaCompleta,VERSION)
    #lsValor[1]-> ID solicitud returned, could be Emisor or Receptor
    showMessage('Mensaje',res[1])
            


# window window
window = tk.Tk()
#geometry=widthxheight
window.geometry('650x600')
window.resizable(width=False, height=False)
window.title('Quart CFDI Wizard - SQL Version')

# create a notebook
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)
notebook.pack()

# create frames
fConfiguración = ttk.Frame(notebook, width=600, height=590)
fConfiguración.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(fConfiguración, text='Configuración y proceso CFDI')

#Add content to Configuración

#Título-Versión SQL
lblVersion=tk.Label(fConfiguración)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblVersion["font"] = ft
lblVersion["fg"] = "blue"
lblVersion["justify"] = "center"
lblVersion["text"] = "SQL VERSION"
lblVersion.place(x=250,y=20,width=100,height=35)

#Título-Instrucciones
lblInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblInst["font"] = ft
lblInst["fg"] = "#333333"
lblInst["justify"] = "center"
lblInst["text"] = "Instrucciones:"
lblInst.place(x=40,y=50,width=100,height=35)
  
#Contenido-Instrucciones
lblContInst=tk.Label(fConfiguración)
ft = tkFont.Font(size=9,weight=tkFont.BOLD)
lblContInst["font"] = ft
lblContInst["fg"] = "#333333"
lblContInst["justify"] = "left"
texto="1.Selecciona una carpeta que contenga los siguientes archivos y elígela en el directorio debajo:\n\n"
texto+='A) Archivo *.cer\nB) Archivo *.key\nC) Archivo "datos.txt" donde debes anotar,en dos líneas, RFC y contraseña de FIEL\n'
lblContInst["text"] = texto
lblContInst.place(x=45,y=100,width=550,height=90)
  
#Section - Directorio  
#lbl-Directorio
posYDirectorio=190
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

#Fin Section - Directorio

#Section- Emisor o Receptor
#Contenido-Instrucciones 2
lblContInst2=tk.Label(fConfiguración)
ft = tkFont.Font(size=9,weight=tkFont.BOLD)
lblContInst2["font"] = ft
lblContInst2["fg"] = "#333333"
lblContInst2["justify"] = "left"
texto='2. Elegir descargar CFDI como Emisor o Receptor'
lblContInst2["text"] = texto
lblContInst2.place(x=40,y=230,width=300,height=40)

#Emisor Radio button
ft = tkFont.Font(size=10)
var = tk.StringVar()
rdbtnEmisor = tk.Radiobutton(fConfiguración, text="Emisor", variable=var, value="Emisor")
rdbtnEmisor["font"] = ft
rdbtnEmisor.place(x=200,y=260)
#Select "emisor" by default
rdbtnEmisor.select()

#Receptor Radio button
rdbtnReceptor = tk.Radiobutton(fConfiguración, text="Receptor", variable=var, value="Receptor")
rdbtnReceptor["font"] = ft
rdbtnReceptor.place(x=300,y=260)

#Fin Section- Emisor o Receptor

lblContInst3=tk.Label(fConfiguración)
ft = tkFont.Font(size=9,weight=tkFont.BOLD)
lblContInst3["font"] = ft
lblContInst3["fg"] = "#333333"
lblContInst3["justify"] = "left"
texto='3. Introducir el rango de fechas del CFDI a recuperar\n\n'
texto+='i.e.: En caso de ser 3 de mayo de 2020, el formato sería de la siguiente manera: 03/05/2020'
lblContInst3["text"] = texto
lblContInst3.place(x=38,y=280,width=540,height=100)

#Section - fechas
#Rango de fechas
#lbl Inicial
posYFechaInicial=370
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
posYFechaFin=400
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

#Fin Section - fechas

#Section - Solicitar CFDI
lblContInst4=tk.Label(fConfiguración)
ft = tkFont.Font(size=9,weight=tkFont.BOLD)
lblContInst4["font"] = ft
lblContInst4["fg"] = "#333333"
lblContInst4["justify"] = "left"
texto='4. Hacer click en el botón "Solicitar CFDI" y sigue los mensajes posteriores\n\n'
lblContInst4["text"] = texto
lblContInst4.place(x=30,y=440,width=470,height=50)

#Btn solicitar
btnSolicitar=tk.Button(fConfiguración,command=preguntaSolicitarCFDI,text='Solicitar CFDI')
btnSolicitar.place(x=250,y=480,width=100,height=25)

#Fin Section - Solicitar CFDI

window.mainloop()


  