from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import sqlite3 as db

con = db.connect('usuario.db')
cur = con.cursor()

NOME_APP = "Menu Cadastro"
root = Tk()
root.configure(bg='#2F4F4F')



con = db.connect("usuario.db")
cur.execute("CREATE TABLE IF NOT EXISTS cliente (nome TEXT, email TEXT)")
cur.close()
con.commit()
con.close()


name = StringVar()
email = StringVar()
status = StringVar()

def insert():
    con = db.connect("usuario.db")
    cur = con.cursor()
    cur.execute("INSERT INTO cliente(nome, email) VALUES (?,?)",(name,email))
    cur.close()
    con.commit()
    con.close()



def sair(event=NONE):
    if tkinter.messagebox.askokcancel('Sair', "Deseja realmente sair?"):
        root.destroy()


def showSobre(event=None):
    fram()


def montarMenu():
    menu_bar = Menu(root)
    arq_menu = Menu(menu_bar, tearoff=0)
    aux_menu = Menu(menu_bar, tearoff=0)
    cad_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Arquivo", underline=0, menu=arq_menu)
    menu_bar.add_cascade(label="Cliente", underline=0, menu=aux_menu)
    menu_bar.add_cascade(label="Cidade", underline=0, menu=cad_menu)
    root.config(menu=menu_bar)
    arq_menu.add_command(label='Sobre', compound='left', command=showSobre)
    arq_menu.add_separator()
    arq_menu.add_command(label="Sair", accelerator='Alt+F4', compound='left', command=sair)
    aux_menu.add_command(label='Cliente', compound='left', command=fram_cadCli)
    aux_menu.add_command(label='Exibir Clientes', compound='left', command=fram_listCli)
    cad_menu.add_command(label='Agenda', compound='left', command=fram_cadCid)
    cad_menu.add_command(label='Exibir Agenda', compound='left', command=fram_listCid)


def initial():
    montarMenu()
    root.protocol('WM_DELETE_WINDOW', sair)
    root.protocol('WM_DELETE_WINDOW', sair)
    root.title(NOME_APP)

    root.geometry("500x400")
    btn_exit()
    root.mainloop()


def fram():
    INFO_APP = "Informações do Sistema"
    newWindow = Tk()
    newWindow.title(INFO_APP)
    newWindow.configure(bg='#2F4F4F')
    newWindow.geometry("500x400")
    lb1 = Label(newWindow, text="\n           Cadastramento de Usuários\n"
                                "\nO sistema foi desenvolvido para armazenar e organizar todos os tipos de informações, \n"
                                "Sendo possivel incialmente cadastrar clientes e agendar consultas, tudo armazenando em bando de dados.")
    lb1['bg'] = '#2F4F4F'
    lb1.pack()
    newWindow.mainloop()


# frame cadastramento cliente
def func_tit(titulo):
    newWindow = Tk()
    newWindow.configure(bg='#2F4F4F')
    newWindow.geometry("500x400")
    newWindow.title(titulo)


def fram_cadCli():
    master = Tk()

    master.title("Cadastramento Cliente")

    Label(master, text="Nome:  ").grid(row=0, column=0)
    Label(master, text="Email:  ").grid(row=2, column=0)

    Entry(master,textvariable=name).grid(row=0,column=1)
    Entry(master,textvariable=email).grid(row=2, column=1)

    Button(master, text='Submit', command=insert).grid(row=3,columnspan=2)


# frame lista de cliente
def fram_listCli():
    func_tit("Listar Clientes")
    newWindow.mainloop()


def fram_cadCid():
    func_tit("Cadastrar Cidades")
    newWindow.mainloop()


def fram_listCid():
    func_tit("Listar Cidades")
    newWindow.mainloop()


def btn_exit():
    bt = Button(root, width=20, text="LOGOUT", bg="yellow", command=sair)
    bt.place(x=170, y=340)


"""
	lb= Label(root, text="Teste")
	lb.place(x=100,y=150)
"""
if __name__ == '__main__':
    initial()

