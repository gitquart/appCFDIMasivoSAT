from InternalControl import cInternalControl
import tkinter.messagebox as tkMessageBox
import tkinter as tk
import tkinter.font as tkFont
import cfdi_quart_excel_version as win_cfdi
import postgresql as bd
import utils as tool
import datetime
import os
import threading
import sys

objControl= cInternalControl()
register_window=None
txtNombreR=None
txtAPR=None
txtAMR=None
txtCorreoR=None
txtPwdR=None
txtEmpresaR=None
formatTimeForPostgreSQL='%Y-%m-%d %H:%M'


def register_user():
    global txtNombreR,txtAPR,txtAMR,txtCorreoR,txtPwdR,txtEmpresa
    name=txtNombreR.get()
    lastNameFather=txtAPR.get()
    lastNameMother=txtAMR.get()
    mail=txtCorreoR.get()
    pwd=txtPwdR.get()
    company =txtEmpresaR.get()
    if name=='' or lastNameFather=='' or lastNameMother=='' or mail=='' or pwd=='' or company=='': 
        tool.showMessage('Mensaje','Verifica que todos los campos estén llenos')
    else:    
        #Check if user exists and if its AUTHORIZED, if it exists then send message saying "User already exists"
        query=f"select id,autorizado from usuario where correo='{mail}' "
        res=None
        res=bd.getQuery(query)
        if not res:
            #Register user
            st=f"insert into usuario (nombre,apellidopaterno,apellidomaterno,empresa,correo,contrasena,fechacompleta,autorizado,softwareversion)"
            st+=f"values ('{name}','{lastNameFather}','{lastNameMother}','{company}','{mail}','{pwd}','{datetime.datetime.now().strftime(formatTimeForPostgreSQL)}',False,'{SOFTWARE_VERSION}')"
            resSt=False
            resSt=bd.executeNonQuery(st)
            if resSt:
                tool.showMessage('Registro exitoso',f'El usuario {mail} ha sido creado exitosamente, en 24 hrs tu cuenta quedará ACTIVADA. \n En un momento serás redirigido a la ventana de logueo.')
                #Send mail- Asynchronous way to send the mail, if it fails it will show a message
                sendMail=threading.Thread(target=tool.sendMail,args=[mail])
                sendMail.start()
                sendMail.join()
                if not sendMail.is_alive():
                    print(f'The mail for {mail} is sent')
                    tool.showMessage('Notificación exitosa','Quart ha recibido la notificación para activar tu cuenta, en un momento serás redirigido a la ventana de logueo')
                   
        else:   
            #User already exists, now see if it is authorized
            auth=None
            auth=res[0][1]
            msj=None
            if auth:
                msj=f'El usuario {mail} ya está registrado y autorizado, favor de acceder a través de Log in'
            else:
                msj=f'El usuario {mail} ya está registrado pero está pendiente de autorización'
            
            tool.showMessage('Mensaje',msj)     

        
        login_window.deiconify()
        register_window.destroy()
        
        

def exit():
    login_window.destroy()
    
def login():
    #Check user and authorization
    mail=txtUser.get()
    strPwd=txtPwd.get()
    if mail=='' or strPwd=='':
        tool.showMessage('Mensaje','Favor de completar los datos de login')
    else:    
        query=f"select id,autorizado,softwareversion from usuario where correo='{mail}' and contrasena='{strPwd}' "
        res=None
        res=bd.getQuery(query)
        if res:
            #Case: User exists
            #Check if it's authorized
            idUser=None
            auth=None
            current_swversion=None
            idUser=int(res[0][0])
            auth=res[0][1]
            current_swversion=float(res[0][2])
            if auth:
                #Check for UPDATES
                #Start of UPDATING SOFTWARE IF EXISTS
                #Start - Check for Updates
                print('Looking for updates...')
                query=f"select swversion from tballsoftwareversion order by fulldate desc;"
                res=None
                res=bd.getQuery(query)
                topswversion=None
                topswversion=float(res[0][0])
                if topswversion > current_swversion:
                    response=None
                    response=tkMessageBox.askyesno(f'Actualización disponible Versión {str(topswversion)}',f'Actualmente tienes el software en la versión {str(current_swversion)}, ¿Deseas actualizar a la versión {str(topswversion)}? ')
                    if response:
                        tool.showMessage('Aviso','La actualización está en proceso de descarga...')
                        os.system('git -C C:/ clone https://github.com/gitquart/cfdi_executable_quart.git')
                        #Update version of software for this user
                        st=f"update usuario set softwareversion='{str(topswversion)}' where id ={str(idUser)} "
                        bd.executeNonQuery(st)
                        tool.showMessage('Descarga exitosa','El nuevo ejecutable se descargó en el directorio C:/cfdi_executable_quart .\n Puedes borrar la versión antigua y abrir la nueva.')
                        sys.exit(0)
                        
                #End - Check for Updates
                #End of UPDATING SOFTWARE IF EXISTS
                #Case: User is authorized
                cfdi_excel_window=tk.Toplevel(login_window)
                login_window.withdraw()
                win_cfdi.openWindowCFDI_ExcelVersion(cfdi_excel_window,login_window)
            else:
                tool.showMessage('Mensaje',f'El usuario {mail} está pendiente de autorización')

        else:
            #Case: User doesn't exist    
            tool.showMessage('Mensaje',f'El usuario {mail} no existe, favor de registrarse')
    

def openRegisterWindow(event):
    global register_window,txtNombreR,txtAPR,txtAMR,txtCorreoR,txtPwdR,txtEmpresaR
    ft = tkFont.Font(size=10)
    register_window=tk.Toplevel(login_window)
    login_window.withdraw()

    #Start : "User registration"
  
    register_window.geometry('500x400')
    register_window.title('Registro de Usuario')

    #Title
    lblTitle=tk.Label(register_window)
    ftTitle = tkFont.Font(size=10,weight=tkFont.BOLD)
    lblTitle["font"] = ftTitle
    lblTitle["fg"] = "black"
    lblTitle["justify"] = "center"
    lblTitle["text"] = "Registro de Usuario"
    lblTitle.place(x=177,y=20,width=150,height=35)

    #*****************BODY************************************
    heightFirstElement=70
    #lb Nombre (1st element)
    lbNombre=tk.Label(register_window)
    lbNombre["font"] = ft
    lbNombre["fg"] = "black"
    lbNombre["justify"] = "right"
    lbNombre["text"] = "Nombre :"
    lbNombre.place(x=78,y=heightFirstElement,width=150,height=35)

    #Caja de texto-User
    txtNombreR=tk.Entry(register_window)
    txtNombreR["borderwidth"] = "1px"
    txtNombreR["font"] = ft
    txtNombreR["fg"] = "#333333"
    txtNombreR["justify"] = "left"
    txtNombreR.place(x=190,y=heightFirstElement,width=200,height=30)

    #lb Apellido Pat (2nd element)
    lbAP=tk.Label(register_window)
    lbAP["font"] = ft
    lbAP["fg"] = "black"
    lbAP["justify"] = "right"
    lbAP["text"] = "Apellido Paterno :"
    lbAP.place(x=50,y=heightFirstElement+40,width=150,height=35)

    #Caja de texto-Apellido Paterno
    txtAPR=tk.Entry(register_window)
    txtAPR["borderwidth"] = "1px"
    txtAPR["font"] = ft
    txtAPR["fg"] = "#333333"
    txtAPR["justify"] = "left"
    txtAPR.place(x=190,y=heightFirstElement+40,width=200,height=30)

    #lb Apellido Materno (3rd element)
    lbAM=tk.Label(register_window)
    lbAM["font"] = ft
    lbAM["fg"] = "black"
    lbAM["justify"] = "right"
    lbAM["text"] = "Apellido Materno :"
    lbAM.place(x=50,y=heightFirstElement+(2*40),width=150,height=35)

    #Caja de texto-Apellido Materno
    txtAMR=tk.Entry(register_window)
    txtAMR["borderwidth"] = "1px"
    txtAMR["font"] = ft
    txtAMR["fg"] = "#333333"
    txtAMR["justify"] = "left"
    txtAMR.place(x=190,y=heightFirstElement+(2*40),width=200,height=30)

    #lb Empresa (4th element)
    lbEmpresa=tk.Label(register_window)
    lbEmpresa["font"] = ft
    lbEmpresa["fg"] = "black"
    lbEmpresa["justify"] = 'right'
    lbEmpresa["text"] = "Empresa :"
    lbEmpresa.place(x=77,y=heightFirstElement+(3*40),width=150,height=35)

    #Caja de texto-Empresa
    txtEmpresaR=tk.Entry(register_window)
    txtEmpresaR["borderwidth"] = "1px"
    txtEmpresaR["font"] = ft
    txtEmpresaR["fg"] = "#333333"
    txtEmpresaR["justify"] = "left"
    txtEmpresaR.place(x=190,y=heightFirstElement+(3*40),width=200,height=30)

    #lb Correo (5th element)
    lbCorreo=tk.Label(register_window)
    lbCorreo["font"] = ft
    lbCorreo["fg"] = "black"
    lbCorreo["justify"] = 'right'
    lbCorreo["text"] = "Correo :"
    lbCorreo.place(x=82,y=heightFirstElement+(4*40),width=150,height=35)

    #Caja de texto-Correo
    txtCorreoR=tk.Entry(register_window)
    txtCorreoR["borderwidth"] = "1px"
    txtCorreoR["font"] = ft
    txtCorreoR["fg"] = "#333333"
    txtCorreoR["justify"] = "left"
    txtCorreoR.place(x=190,y=heightFirstElement+(4*40),width=200,height=30)

    #lb Pwd (6th element)
    lbPwd=tk.Label(register_window)
    lbPwd["font"] = ft
    lbPwd["fg"] = "black"
    lbPwd["justify"] = 'right'
    lbPwd["text"] = "Contraseña :"
    lbPwd.place(x=69,y=heightFirstElement+(5*40),width=150,height=35)

    #Caja de texto-Pwd
    txtPwdR=tk.Entry(register_window)
    txtPwdR["borderwidth"] = "1px"
    txtPwdR["font"] = ft
    txtPwdR["fg"] = "#333333"
    txtPwdR["justify"] = "left"
    txtPwdR["show"]='*'
    txtPwdR.place(x=190,y=heightFirstElement+(5*40),width=200,height=30)

    #*****************FOOTER************************************
    
    heightForFooterBtn=350
    #Btn Register
    btnRegister=tk.Button(register_window,command=register_user,text='Registrarse')
    btnRegister['bg']='#00FF66'
    btnRegister.place(x=135,y=heightForFooterBtn,width=100,height=25)

    #Btn Exit all
    btnExit=tk.Button(register_window,command=exit,text='Salir')
    btnExit['bg']='#FF9966'
    btnExit.place(x=260,y=heightForFooterBtn,width=100,height=25)


    #End : "User registration"

#Start of Login window
login_window = tk.Tk()
#geometry=widthxheight
login_window.geometry('400x350')
login_window.resizable(width=False, height=False)
login_window.title(f'Bienvenido a Quart CFDI v{str(objControl.SOFTWARE_VERSION)} - Login ')

#Title
lblTitle=tk.Label(login_window)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblTitle["font"] = ft
lblTitle["fg"] = "black"
lblTitle["justify"] = "center"
lblTitle["text"] = "Acceder a Quart CFDI"
lblTitle.place(x=125,y=20,width=150,height=35)

#Lb User (Correo)
lblUser=tk.Label(login_window)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblUser["font"] = ft
lblUser["fg"] = "black"
lblUser["justify"] = "right"
lblUser["text"] = "Correo :"
lblUser.place(x=40,y=100,width=100,height=35)

#Caja de texto-User (Correo)
txtUser=tk.Entry(login_window)
txtUser["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtUser["font"] = ft
txtUser["fg"] = "#333333"
txtUser["justify"] = "left"
txtUser.place(x=130,y=100,width=200,height=30)

#Lb Password
lblPwd=tk.Label(login_window)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblPwd["font"] = ft
lblPwd["fg"] = "black"
lblPwd["justify"] = "right"
lblPwd["text"] = "Contraseña :"
lblPwd.place(x=30,y=150,width=100,height=35)

#Caja de texto- Password
txtPwd=tk.Entry(login_window)
txtPwd["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtPwd["font"] = ft
txtPwd["fg"] = "#333333"
txtPwd["justify"] = "left"
txtPwd['show']='*'
txtPwd.place(x=130,y=150,width=200,height=30)

#Btn login
btnLogin=tk.Button(login_window,command=login,text='Entrar')
btnLogin['bg']='#F5FFFA'
btnLogin.place(x=150,y=200,width=100,height=25)

#Lb Register
lblRegister=tk.Label(login_window)
ft = tkFont.Font(size=9,weight=tkFont.BOLD)
lblRegister["font"] = ft
lblRegister["fg"] = "black"
lblRegister["justify"] = "center"
lblRegister["text"] = "Regístrate aquí"
lblRegister.place(x=75,y=240,width=250,height=35)
lblRegister.bind('<1>',openRegisterWindow)


login_window.mainloop()
