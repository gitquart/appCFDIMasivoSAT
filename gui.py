import tkinter as tk                     
from tkinter import ttk 
  
  
root = tk.Tk() 
root.title("CFDI Wizard") 
tabControl = ttk.Notebook(root) 
  
tabSolicitar = ttk.Frame(tabControl) 
tabVerificar = ttk.Frame(tabControl) 
tabDescargar = ttk.Frame(tabControl)
tabProcesarZip = ttk.Frame(tabControl)
  
tabControl.add(tabSolicitar, text ='Solicitar CFDI') 
tabControl.add(tabVerificar, text ='Verificar CFDI') 
tabControl.add(tabDescargar,text='Descargar paquete')
tabControl.add(tabProcesarZip,text='Procesar ZIP descargado')
tabControl.pack(expand = 1, fill ="both") 
  
ttk.Label(tabSolicitar,  
          text ="Solicitar CFDI").grid(column = 0,  
                               row = 0, 
                               padx = 30, 
                               pady = 30)   
ttk.Label(tabVerificar, 
          text ="Veriicar estado de CFDI").grid(column = 0, 
                                    row = 0,  
                                    padx = 30, 
                                    pady = 30) 
  
root.mainloop()   