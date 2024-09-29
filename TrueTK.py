from tkinter import *
import tkinter as tk
from tkinter import  messagebox
from os import system
import sqlite3 as sql


cnx = sql.connect('TkinterUI.db')
cnx.commit()
cur = cnx.cursor()

cur.execute(
    'CREATE TABLE IF NOT EXISTS Users (Nome, Email, Senha)'
)

def register_check():
    check = 0
    register_email = str(email2.get())
    register_name = str(nome2.get())
    register_password = str(senha2.get())

    if len(senha2.get()) > 8:
        senha2.delete(1, END)

    if register_email == "":
        messagebox.showwarning("Error", "Preencha o campo de e-mail")
    elif "@gmail.com" in register_email:
        print("válido")
        check += 1
    else:
        messagebox.showerror("Email", "E-mail inválido")
    
    if register_name == "":
        messagebox.showwarning("Error", "Preencha o campo de nome")
    else:
        check += 1
    
    if register_password == "":
        messagebox.showwarning("Error", "Preencha o campo de senha")
    else:
        check += 1
    
    if check == 3:
        register_screen.destroy()
        cur.execute(
            f"INSERT INTO Users VALUES ('{register_name}', '{register_email}', '{register_password}')"
        )
        messagebox.showinfo("Register", "Registro completo")

def login_check():
    login_email = str(email.get())
    
    if "@gmail.com" in login_email:
        login_screen.destroy()
        messagebox.showinfo("Login", "Login completo")
    else:
        messagebox.showerror("Email", "E-mail incorreto")

def login_back():
    login_screen.destroy()
    create()

def register_back():
    register_screen.destroy()
    create()

def login():
    global login_screen, email, senha, login_pass_check
    screen.destroy()
    login_screen = Tk()
    login_screen.configure(bg="lavender")
    login_screen.geometry("600x500-500+100")
    login_screen.title("LOGIN")
    
    nome_instrucao = Label(login_screen, text="Nome", bg="lavender")
    nome_instrucao.grid(column=0, row=1)

    nome = Entry(login_screen, width=45)
    nome.grid(column=1, row=1)

    email_instrucao = Label(login_screen, text="E-mail", bg="lavender")
    email_instrucao.grid(column=0, row=2)

    email = Entry(login_screen, width=45)
    email.grid(column=1, row=2)

    senha_instrucao = Label(login_screen, text="Senha", bg="lavender")
    senha_instrucao.grid(column=0, row=3)

    senha = Entry(login_screen, width=45, show="*")
    senha.grid(column=1, row=3)

    login_pass_check = BooleanVar()
    cb = Checkbutton(login_screen, text="Ver senha", bg="lavender",variable=login_pass_check, command=ver_senha_login)
    cb.grid(column=2, row=3)

    bk = Button(login_screen, text="back", command=login_back)
    bk.grid(column=0, row=0)

    confirm_bt = Button(login_screen, text="Confirm", bg="steel blue", command=login_check)
    confirm_bt.grid(column=1, row=4, pady=10)

    login_screen.mainloop()

def ver_senha_login():
        if login_pass_check.get():
            senha.config(show="")
        else:
            senha.config(show="*")

def ver_senha():
        if pass_check.get():
            senha2.config(show="")
        else:
            senha2.config(show="*")

def register():
    global register_screen, email2, senha2, nome2, pass_check
    screen.destroy()
    register_screen = Tk()  
    register_screen.configure(bg="lavender")
    register_screen.geometry("600x500-500+100")
    register_screen.title("REGISTAR")

    nome_instrucao = Label(register_screen, text="Nome", bg="lavender")
    nome_instrucao.grid(column=0, row=1)

    nome2 = Entry(register_screen, width=45)
    nome2.grid(column=1, row=1)

    email2_instrucao = Label(register_screen, text="E-mail", bg="lavender")
    email2_instrucao.grid(column=0, row=2)

    email2 = Entry(register_screen, width=45)
    email2.grid(column=1, row=2)

    senha_instrucao = Label(register_screen, text="Senha", bg="lavender")
    senha_instrucao.grid(column=0, row=3)

    senha2 = Entry(register_screen, width=45, show="*")
    senha2.grid(column=1, row=3)

    pass_check = BooleanVar()

    cb = Checkbutton(register_screen, text="Ver senha", bg="lavender",variable=pass_check, command=ver_senha)
    cb.grid(column=2, row=3)

    bk = Button(register_screen, text="back", command=register_back)
    bk.grid(column=0, row=0)

    confirm_bt = Button(register_screen, text="Confirm", bg="steel blue", command=register_check)
    confirm_bt.grid(column=1, row=4, pady=10)

    register_screen.mainloop()

def create():
    global screen
    screen = Tk()
    screen.configure(bg="misty rose")
    screen.geometry("600x500-500+100")
    screen.title("APP")

    lb1 = Label(screen, text="Seja bem-vindo(a)", width=30, height=5, font=('Times New Roman', 25, 'bold'), bg="misty rose")
    lb1.place(anchor=NW)

    login_bt = Button(screen, text="Login", bg="dodger blue", height= 2, width=15, command=login)
    login_bt.grid(column=0, row=0, padx=100, pady=250)

    register_bt = Button(screen, text="Register", bg="dodger blue", height= 2, width=15, command=register)
    register_bt.grid(column=1, row=0, padx=85)

    screen.mainloop()

create()
consulta = cur.execute(' SELECT * FROM Users').fetchall()
for i in consulta:
    print(i)

cnx.close()