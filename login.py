from tkinter import *
from tkinter import messagebox
import subprocess


tela = Tk()
tela.title("Acesso ao Sistema")
tela.geometry("400x200")
tela.resizable(False, False)
largura = 400
altura = 200


#definição da função para validar usuario

def validar_acesso(usuario, senha):
    if usuario == "admin" and senha == "123":
        abrir_app()
    else:
        messagebox.showerror("Erro de Login", "Usuario ou senha incorretos")


#definição da funçao para chamar o menu

def abrir_app():
    tela.destroy()
    subprocess.run(["python", "menu.py"])

#definição da função sair
    
def sair():
    resposta = messagebox.askquestion("sair do sistema?", "Você tem certeza que deseja sair?")
    if resposta == "yes":
        tela.destroy()


lbl_usuario = Label(tela, text="Usuário").place(x=50, y=60)
lbl_senha = Label(tela, text="Senha").place(x=50, y=100)
txt_senha = Entry(tela, show='*', width=20).place(x=100, y=100)
txt_usuario = Entry(tela, width=20).place(x=100, y=60)
foto_acesso = PhotoImage(file = r"icones\acesso.png")
foto_sair = PhotoImage(file = r"icones\sair.png")
btn_usuario =  Button(tela, text="Acessar", image= foto_acesso ,compound= TOP, command=abrir_app).place(x=250,y=50)  
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair).place(x=320,y=50)

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura, posx,posy))
tela.mainloop()




