from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo


tela = Tk()
tela.title("Exemplo Mongo DB")
tela.geometry("800x600")
tela.resizable(True, True)
tela.configure(background="#ffffff")

largura = 700
altura = 400

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
collection = db["clientes"]

lbl_titulo = Label(tela, text="Cadastro de Clientes", 
                   font=("Arial", 30, "bold"), bg="#ffffff").place(x=200, y=50)


lbl_codigo = Label(tela, text="Código:", bg="#ffffff").place(x=130, y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)

lbl_nome = Label(tela, text="Nome:", bg="#ffffff").place(x=130, y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0, "")

lbl_cpf = Label(tela, text="CPF:", bg="#ffffff").place(x=450, y=170)
txt_cpf = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cpf.place(x=480, y=170)
txt_cpf.insert(0, "")

lbl_idade = Label(tela, text="Idade:", bg="#ffffff").place(x=130, y=200)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=190, y=200)
txt_idade.insert(0, "")

lbl_end = Label(tela, text="Rua:", bg="#ffffff").place(x=450, y=200)
txt_end = Entry(tela, width=25, borderwidth=2, fg="black", bg="white")
txt_end.place(x=480, y=200)
txt_end.insert(0, "")




lbl_bairro = Label(tela, text="Bairro:", bg="#ffffff").place(x= 130, y= 230)
txt_bairro = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_bairro.place(x= 190, y=230)
txt_bairro.insert(0, " ")

lbl_estado = Label(tela, text="Estado:", bg="#ffffff").place(x=330, y=230)
comboestado = ttk.Combobox(tela, 
                            values=[
                                    "São Paulo", 
                                    "Rio de Janeiro",
                                    "Minas Gerais",
                                    "Espírito Santo"],)

comboestado.grid(column=0, row=1)
comboestado.place(x=370 , y=230)

lbl_cidade = Label(tela, text="Cidade:", bg="#ffffff").place(x= 520, y= 230)
txt_cidade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cidade.place(x= 570, y=230)
txt_cidade.insert(0, " ")


def salvar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
   
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()
   
    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
   
    txt_end.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    comboestado.set("")
    txt_cpf.delete(0, tk.END)
 

    cliente = {"código":codigo, "nome": nome, "idade":idade, "endereço": end, "cpf":cpf, 
               "bairro":bairro, "cidade":cidade, "estado": estado}
    collection.insert_one(cliente)


def atualizar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
   
    end = txt_end.get()
    cpf = txt_cpf.get()
   
    bairro = txt_bairro.get()
    cidade = txt_cidade.get()
    estado = comboestado.get()
   
    collection.update_one({"código":codigo}, {"$set": {"código":codigo, "nome": nome, 
                                                       "idade":idade,   "endereço": end, "cpf":cpf, 
                                                       "bairro":bairro, 
                                                       "cidade":cidade, "estado": estado}})

def apagar():
    codigo = txt_codigo.get()
    collection.delete_one({"código": codigo})

def consultar():
    codigo = txt_codigo.get()
    resultado = collection.find_one({"código": codigo})

    if resultado:
        txt_nome.insert(END, f" {resultado['nome']}\n")
        txt_idade.insert(END, f"{resultado['idade']}\n")
        txt_end.insert(END, f" {resultado['endereço']}\n")
        txt_cpf.insert(END, f"{resultado['cpf']}\n")
        txt_bairro.insert(END, f" {resultado['bairro']}\n")
        txt_cidade.insert(END, f"{resultado['cidade']}\n")
        comboestado.insert(END, f" {resultado['estado']}\n")
    else:
       lbl_resultado.config(text="Nenhum resultado encontrado")

lbl_resultado = Label(tela, text="", bg="#ffffff")
lbl_resultado.place(x=490, y=310)

foto_salvar = PhotoImage(file= r"icones\salvar.png")
foto_excluir = PhotoImage(file= r"icones\excluir.png")
foto_alterar = PhotoImage(file= r"icones\alterar.png")
foto_consultar = PhotoImage(file= r"icones\consultar.png")
foto_sair = PhotoImage(file= r"icones\sair.png")

btn_salvar = Button(tela, text="Salvar", image = foto_salvar, width=60, height=60,
                    command=salvar,compound= TOP).place(x=130, y=280)
btn_alterar = Button(tela, text="Alterar",image = foto_alterar, width=60, height=60,
                     command=atualizar,compound= TOP).place(x=220, y=280)
btn_excluir = Button(tela, text="Excluir",width=60, height=60,image = foto_excluir, 
                     command=apagar,compound= TOP).place(x=310, y=280)
btn_consultar = Button(tela, text="Consultar", width=60,height=60, image = foto_consultar,
                       command=consultar,compound= TOP).place(x=400, y=280)
btn_sair = Button(tela, text="Sair",width=60,height=60, image = foto_sair, 
                  command=tela.quit,compound= TOP).place(x=490, y=280)



 
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura, posx,posy))
tela.mainloop()