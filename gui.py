import tkinter as tk                     
from tkinter import ttk
import tkinter.font as tkFont 
  
  
root = tk.Tk() 
root.geometry('500x500')
root.title("CFDI Wizard") 
tabControl = ttk.Notebook(root) 
  
tabConfiguracion = ttk.Frame(tabControl) 
tabProceso = ttk.Frame(tabControl) 

  
tabControl.add(tabConfiguracion, text ='Configuración') 
tabControl.add(tabProceso, text ='Proceso CFDI') 
tabControl.pack(expand = 1, fill ="both") 

#Elementos de tabConfiguración 


#Elementos de tabProceso  

  
root.mainloop()   