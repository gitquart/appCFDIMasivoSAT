import tkinter as tk
import tkinter.font as tkFont

register_window=None

def register_user():
    login_window.deiconify()
    register_window.destroy()

def exit():
    login_window.destroy()
    


def openRegisterWindow(event):
    global register_window
    register_window=tk.Toplevel(login_window)
    login_window.withdraw()

    #Start : "User registration"
  
    register_window.geometry('500x500')
    register_window.title('User Registration')

    #Title
    lblTitle=tk.Label(register_window)
    ft = tkFont.Font(size=10,weight=tkFont.BOLD)
    lblTitle["font"] = ft
    lblTitle["fg"] = "black"
    lblTitle["justify"] = "center"
    lblTitle["text"] = "Registro de Usuario"
    lblTitle.place(x=170,y=20,width=150,height=35)

    #*****************BODY************************************

    #lb Nombre
    lbNombre=tk.Label(register_window)
    ft = tkFont.Font(size=10,weight=tkFont.BOLD)
    lbNombre["font"] = ft
    lbNombre["fg"] = "black"
    lbNombre["justify"] = "center"
    lbNombre["text"] = "Login to Quart CFDI"
    lbNombre.place(x=125,y=20,width=150,height=35)

    #*****************FOOTER************************************

    #Btn Register
    btnRegister=tk.Button(register_window,command=register_user,text='Registrar')
    btnRegister['bg']='#00FF66'
    btnRegister.place(x=135,y=400,width=100,height=25)

    #Btn Exit all
    btnExit=tk.Button(register_window,command=exit,text='Salir')
    btnExit['bg']='#FF9966'
    btnExit.place(x=260,y=400,width=100,height=25)

    

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
lblTitle["text"] = "Login to Quart CFDI"
lblTitle.place(x=125,y=20,width=150,height=35)

#Lb User
lblUser=tk.Label(login_window)
ft = tkFont.Font(size=10,weight=tkFont.BOLD)
lblUser["font"] = ft
lblUser["fg"] = "black"
lblUser["justify"] = "center"
lblUser["text"] = "Usuario :"
lblUser.place(x=40,y=100,width=100,height=35)

#Caja de texto-User
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
lblPwd["justify"] = "center"
lblPwd["text"] = "Contraseña: "
lblPwd.place(x=30,y=150,width=100,height=35)

#Caja de texto-User
txtPwd=tk.Entry(login_window)
txtPwd["borderwidth"] = "1px"
ft = tkFont.Font(size=10)
txtPwd["font"] = ft
txtPwd["fg"] = "#333333"
txtPwd["justify"] = "left"
txtPwd.place(x=130,y=150,width=200,height=30)

#Btn login
btnLogin=tk.Button(login_window,command='',text='Entrar')
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