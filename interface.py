from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import sqlite3 as db

con = db.connect('usuario.db')
cur = con.cursor()

NOME_APP = "Controle de Agendamentos"
root = Tk()
root.configure(bg='#2F4F4F')


#tabela cliente
con = db.connect("usuario.db")
cur.execute("CREATE TABLE IF NOT EXISTS cliente (nome TEXT, email TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS agenda (nome TEXT,datai TEXT, dataf TEXT)")
cur.close()
con.commit()
con.close()

'''
#tabela de agenda
cur.execute("CREATE TABLE IF NOT EXISTS agenda (nome TEXT,datai TEXT, dataf TEXT)")
con.close()
con.commit()
con.close()

'''


def insert():
    nome = nam1
    email = nam2
    con = db.connect("usuario.db")
    cur = con.cursor()
    #insert = 'INSERT INTO cliente(nome, email) VALUES(?,?)', (nam1,nam2)
    #insert = 'INSERT INTO cliente (nome, email) VALUES(nam1,nam2)'
    insert = 'INSERT INTO cliente(nome, email) VALUES(?,?)'
    cur.execute(insert, [(nome), (email)])
    con.commit()
   
def put():
    nome = nam
    datai = dati
    dataf = datf
    con = db.connect("usuario.db")
    cur = con.cursor()
    insert = 'INSERT INTO agenda(nome, datai, dataf) VALUES(?,?,?)'
    cur.execute(insert, [(nome), (datai), (dataf)])
    con.commit()
def sair(event=NONE):
    if tkinter.messagebox.askokcancel('Sair', "Deseja realmente sair?"):
        root.destroy()
def alert(event=NONE):
    if tkinter.messagebox.askokcancel("Criado com sucesso"):
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
    menu_bar.add_cascade(label="Consulta", underline=0, menu=cad_menu)
    root.config(menu=menu_bar)
    arq_menu.add_command(label='Sobre', compound='left', command=showSobre)
    arq_menu.add_separator()
    arq_menu.add_command(label="Sair", accelerator='Alt+F4', compound='left', command=sair)
    aux_menu.add_command(label='Cadastrar', compound='left', command=fram_cadCli)
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

#frame menu informacoes sistemas
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



def func_tit(titulo):
    newWindow = Tk()
    newWindow.configure(bg='#2F4F4F')
    newWindow.geometry("500x400")
    newWindow.title(titulo)

#frame interface cadastro
def fram_cadCli():
    global nam1, nam2 
    master = Tk()

    master.title("Cadastramento Cliente")

    Label(master, text="Nome:  ").grid(row=0, column=0)
    Label(master, text="Email:  ").grid(row=2, column=0)

    nam1 = Entry(master).grid(row=0,column=1)
    nam2 = Entry(master).grid(row=2, column=1) 
    Button(master, text='Submit', command=insert).grid(row=3,columnspan=2)
    Button(master, text='Submit', command=alert).grid(row=3,columnspan=2)

# frame lista de cliente
def fram_listCli():
    master = Tk()

    master.title("Localizar Cliente")

    Label(master, text="Digite o nome do cliente:  ").grid(row=0, column=0)
    Entry(master).grid(row=0,column=1)
    Button(master, text='Submit').grid(row=3,columnspan=2)

def fram_cadCid():
    global nom, dati, datf
    master = Tk()

    master.title("Marcar Consulta")

    Label(master, text="Nome:  ").grid(row=0, column=0)
    Label(master, text="Data Consulta:  ").grid(row=2, column=0)
    Label(master, text="Data hoje:  ").grid(row=4, column=0)
    
    nom =  Entry(master).grid(row=0,column=1)
    dati = Entry(master).grid(row=2, column=1)
    datf = Entry(master).grid(row=4, column=1)
    Button(master, text='Submit', command=put).grid(row=5,columnspan=2)
    Button(master, text='Submit', command=alert).grid(row=5,columnspan=2)


def fram_listCid():
    master = Tk()

    master.title("Consultas Agendadas")

    Label(master, text="Data Inicio:  ").grid(row=0, column=0)
    Entry(master).grid(row=0,column=1)
    Label(master, text="Data Final:  ").grid(row=4, column=0)
    Entry(master).grid(row=4, column=1)
    Button(master, text='Submit').grid(row=5,columnspan=2)


def btn_exit():
    bt = Button(root, width=20, text="LOGOUT", bg="yellow", command=sair)
    bt.place(x=170, y=340)


"""
	lb= Label(root, text="Teste")
	lb.place(x=100,y=150)
"""
if __name__ == '__main__':
    initial()

