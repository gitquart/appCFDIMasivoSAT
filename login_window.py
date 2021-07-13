import tkinter as tk
import tkinter.font as tkFont
import cfdi_quart_excel_version as win_cfdi


register_window=None


def register_user():
    login_window.deiconify()
    register_window.destroy()

def exit():
    login_window.destroy()
    
def login():
    cfdi_excel_window=tk.Toplevel(login_window)
    login_window.withdraw()
    win_cfdi.openWindowCFDI_ExcelVersion(cfdi_excel_window,login_window)
    



def openRegisterWindow(event):
    global register_window
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
    txtNombre=tk.Entry(register_window)
    txtNombre["borderwidth"] = "1px"
    txtNombre["font"] = ft
    txtNombre["fg"] = "#333333"
    txtNombre["justify"] = "left"
    txtNombre.place(x=190,y=heightFirstElement,width=200,height=30)

    #lb Apellido Pat (2nd element)
    lbAP=tk.Label(register_window)
    lbAP["font"] = ft
    lbAP["fg"] = "black"
    lbAP["justify"] = "right"
    lbAP["text"] = "Apellido Paterno :"
    lbAP.place(x=50,y=heightFirstElement+40,width=150,height=35)

    #Caja de texto-Apellido Paterno
    txtAP=tk.Entry(register_window)
    txtAP["borderwidth"] = "1px"
    txtAP["font"] = ft
    txtAP["fg"] = "#333333"
    txtAP["justify"] = "left"
    txtAP.place(x=190,y=heightFirstElement+40,width=200,height=30)

    #lb Apellido Materno (3rd element)
    lbAM=tk.Label(register_window)
    lbAM["font"] = ft
    lbAM["fg"] = "black"
    lbAM["justify"] = "right"
    lbAM["text"] = "Apellido Materno :"
    lbAM.place(x=50,y=heightFirstElement+(2*40),width=150,height=35)

    #Caja de texto-Apellido Materno
    txtAM=tk.Entry(register_window)
    txtAM["borderwidth"] = "1px"
    txtAM["font"] = ft
    txtAM["fg"] = "#333333"
    txtAM["justify"] = "left"
    txtAM.place(x=190,y=heightFirstElement+(2*40),width=200,height=30)

    #lb Empresa (4th element)
    lbEmpresa=tk.Label(register_window)
    lbEmpresa["font"] = ft
    lbEmpresa["fg"] = "black"
    lbEmpresa["justify"] = 'right'
    lbEmpresa["text"] = "Empresa :"
    lbEmpresa.place(x=77,y=heightFirstElement+(3*40),width=150,height=35)

    #Caja de texto-Empresa
    txtEmpresa=tk.Entry(register_window)
    txtEmpresa["borderwidth"] = "1px"
    txtEmpresa["font"] = ft
    txtEmpresa["fg"] = "#333333"
    txtEmpresa["justify"] = "left"
    txtEmpresa.place(x=190,y=heightFirstElement+(3*40),width=200,height=30)

    #lb Correo (5th element)
    lbCorreo=tk.Label(register_window)
    lbCorreo["font"] = ft
    lbCorreo["fg"] = "black"
    lbCorreo["justify"] = 'right'
    lbCorreo["text"] = "Correo :"
    lbCorreo.place(x=82,y=heightFirstElement+(4*40),width=150,height=35)

    #Caja de texto-Correo
    txtCorreo=tk.Entry(register_window)
    txtCorreo["borderwidth"] = "1px"
    txtCorreo["font"] = ft
    txtCorreo["fg"] = "#333333"
    txtCorreo["justify"] = "left"
    txtCorreo.place(x=190,y=heightFirstElement+(4*40),width=200,height=30)

    #lb Pwd (6th element)
    lbPwd=tk.Label(register_window)
    lbPwd["font"] = ft
    lbPwd["fg"] = "black"
    lbPwd["justify"] = 'right'
    lbPwd["text"] = "Contraseña :"
    lbPwd.place(x=69,y=heightFirstElement+(5*40),width=150,height=35)

    #Caja de texto-Pwd
    txtPwd=tk.Entry(register_window)
    txtPwd["borderwidth"] = "1px"
    txtPwd["font"] = ft
    txtPwd["fg"] = "#333333"
    txtPwd["justify"] = "left"
    txtPwd.place(x=190,y=heightFirstElement+(5*40),width=200,height=30)

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


# window window
login_window = tk.Tk()
#geometry=widthxheight
login_window.geometry('400x350')
login_window.resizable(width=False, height=False)
login_window.title('Bienvenido a Quart CFDI - Login')

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