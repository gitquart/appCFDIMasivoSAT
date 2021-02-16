import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk,filedialog
import tkinter.messagebox as tkMessageBox
import tkinter as tk
from tkinter import ttk
import utils as tool
import datetime
from InternalControl import cInternalControl

objControl=cInternalControl()


def returnFolder():
    folderSelected=filedialog.askdirectory()
    txtDir.delete(0,tk.END)
    txtDir.insert(0,folderSelected)


def showMessage(title,content):
    tkMessageBox.showinfo(title=title,message=content)

def solicitarCFDI():
    #Dates on txtDates : dd/mm/yyyy
    fechaInicio=txtFechaInicio.get()
    fechaFin=txtFechaFin.get()
    directory=txtDir.get()
    if fechaInicio!='' and fechaFin!='' and directory!='' :
        chunksFI=fechaInicio.split('/')
        chunksFF=fechaFin.split('/')
        fecha_inicial = datetime.datetime(int(chunksFI[2]), int(chunksFI[1]), int(chunksFI[0]))
        fecha_final = datetime.datetime(int(chunksFF[2]),int(chunksFF[1]),int(chunksFF[0]))
        lsvalor=[]
        lsvalor=tool.solicitaDescarga(fecha_inicial,fecha_final,directory)
        res=int(lsvalor[0])
        if res==1:
            if lsvalor[1]!='':
                txtID1.insert(0,lsvalor[1])
            else:
                txtID1.insert(0,'No trae valor')
            if lsvalor[2]!='':
                txtID2.insert(0,lsvalor[2])
            else:
                txtID2.insert(0,'No trae valor') 

            showMessage('Mensaje','Por favor revisa los IDs de solicitud devueltos\nCopia un ID  a la vez en la caja de texto de "Verificar y Descargar CFDI" y haz click en el botón para procesar')     
        else:
            showMessage('Mensaje',lsvalor[1])      
    else:
        showMessage('Mensaje','Por favor, verifica que las fechas o el directorio no estén vacíos')    

def verificarCFDI():
    idSolicitud=txtIDVerificar.get()
    directory=txtDir.get()
    if idSolicitud!='':
        if directory!='':
            res=tool.verificaSolicitudDescarga(idSolicitud,directory)
            showMessage('Mensaje',res[1])
        else:
            showMessage('Mensaje','Debes ingresar un directorio')
    else:    
        showMessage('Mensaje','Por favor, ingresa un ID de Solicitud')

   



# window window
window = tk.Tk()
#geometry=widthxheight
window.geometry('650x600')
window.resizable(width=False, height=False)
window.title('Quart CFDI Wizard')

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
texto="1.Selecciona una carpeta que contenga los siguientes archivos y elígela en el directorio debajo:\n\n"
texto+='A) Archivo *.cer\nB) Archivo *.key\nC) Archivo "datos.txt" donde debes anotar,en dos líneas, RFC y contraseña de FIEL\n'
lblContInst["text"] = texto
lblContInst.place(x=45,y=70,width=550,height=90)
  
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

window.mainloop()


  