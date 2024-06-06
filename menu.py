from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess
from PIL import Image, ImageTk

tela = Tk()
tela.title("TELA MENU SISTEMAS")

largura = 1000
altura = 700

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura, posx,posy))
tela.resizable(False,False)

caminho_imagem = "icones\imagem_fundo.jpg"

imagem_pil = Image.open(caminho_imagem)
largura, altura = imagem_pil.size
if largura > 2078:
   proporcao = largura / 2078
   nova_altura = int(altura / proporcao)
   imagem_pil = imagem_pil.resize((1024, nova_altura))
imagem_tk = ImageTk.PhotoImage(imagem_pil)
lbl_imagem = Label(tela, image=imagem_tk)
lbl_imagem.image = imagem_tk
lbl_imagem.place(x=0, y=0)


#definição das funções para chamar as telas
       
def abrir_tela_clientes():
    subprocess.run(["python", "clientes.py"])

def abrir_tela_animais():
    subprocess.run(["python", "animais.py"])

def logout():
    tela.destroy()
    subprocess.run(["python", "login.py"])

#construção do menu

barra_menu = Menu(tela)
opcoes_menu_arquivos = Menu(barra_menu)
opcoes_menu_gestao = Menu(barra_menu)
opcoes_novo = Menu(opcoes_menu_arquivos)

barra_menu.add_cascade(label="Arquivo", menu=opcoes_menu_arquivos)
opcoes_menu_arquivos.add_cascade(label="Novo", menu=opcoes_novo)
opcoes_novo.add_command(label="Cadastrar")

opcoes_menu_arquivos.add_command(label="Abrir")
opcoes_menu_arquivos.add_command(label="Salvar")
opcoes_menu_arquivos.add_separator()
opcoes_menu_arquivos.add_command(label="Sair", command=tela.quit)



barra_menu.add_cascade(label="Gestao", menu=opcoes_menu_gestao)
opcoes_menu_gestao.add_command(label="Animais",command=abrir_tela_animais)
opcoes_menu_gestao.add_command(label="Clientes", command=abrir_tela_clientes)

foto_sair = PhotoImage(file = r"icones/logo.png")
foto_animais = PhotoImage(file = r"icones/logo_animais.png")
foto_usuarios = PhotoImage(file = r"icones/logo_usuarios.png")
foto_servicos = PhotoImage(file = r"icones/logo_servicos.png")
foto_logout = PhotoImage(file = r"icones/logout.png")



foto_sair = PhotoImage(file = r"icones\logo.png")
foto_animais = PhotoImage(file = r"icones\logo_animais.png")
foto_usuarios = PhotoImage(file = r"icones\logo_usuarios.png")
foto_servicos = PhotoImage(file = r"icones\logo_servicos.png")
foto_logout = PhotoImage(file = r"icones\logout.png")

lbl_logo = Label(tela, text="SISTEMA MENU",compound= TOP, image=foto_sair).place(x=900,y=580)
btn_animais= Button(tela, text="Animais", image=foto_animais,compound= TOP, command=abrir_tela_animais).place(x=100,y=200)
btn_clientes= Button(tela, text="Clientes", image=foto_usuarios,compound= TOP, command=abrir_tela_clientes).place(x=350,y=200)
btn_servicos= Button(tela, text="Serviços", image=foto_servicos,compound= TOP).place(x=550,y=200)
btn_logout= Button(tela, text="Logout", image=foto_logout,compound= TOP, command=logout).place(x=800,y=200)


#chama a tela de menu

tela.config(menu=barra_menu)

tela.mainloop()