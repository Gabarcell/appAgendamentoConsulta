from tkinter import *
import tkinter.filedialog
import tkinter.messagebox



class Inter():
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.master.title("International Aplication ")
        self.frame.master.geometry("500x400")
        self.frame.master.configure(bg='#2F4F4F')
        self.frame.master.protocol('WM_DELETE_WINDOW', self.sair)
        self.frame.master.protocol('WM_DELETE_WINDOW', self.sair)
        self.btn_logout()
        self.frame.pack()
        menu_bar = Menu(master)
        arq_menu = Menu(menu_bar, tearoff=0)
        aux_menu = Menu(menu_bar, tearoff=0)
        cad_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Arquivo", underline=0, menu=arq_menu)
        menu_bar.add_cascade(label="Cliente", underline=0, menu=aux_menu)
        menu_bar.add_cascade(label="Consulta", underline=0, menu=cad_menu)
        master.config(menu=menu_bar)
        master.config(menu=menu_bar)
        arq_menu.add_command(label='Sobre', compound='left', command=self.info)
        arq_menu.add_separator()
        arq_menu.add_command(label="Sair", accelerator='Alt+F4', compound='left', command=self.sair)
        aux_menu.add_command(label='Cadastrar', compound='left')
        aux_menu.add_command(label='Exibir Clientes', compound='left')
        cad_menu.add_command(label='Agenda', compound='left')
        cad_menu.add_command(label='Exibir Agenda', compound='left')

    def btn_logout(self):
        bt = Button(self.frame.master, width=20, text="LOGOUT", bg="yellow",command= self.sair)
        bt.place(x=170, y=340)

    def info(self):
        inf = "Informações do Sistema"
        newWindow = Tk()
        newWindow.title(inf)
        newWindow.configure(bg='#2F4F4F')
        newWindow.geometry("500x400")
        lb1 = Label(newWindow, text="\n     Cadastramento de Usuários\n"
                                    "\nO sistema foi desenvolvido para armazenar e organizar todos os tipos de informações, \n"
                                    "Sendo possivel incialmente cadastrar clientes e agendar consultas, tudo armazenando em \nbando de dados.")
        lb1['bg'] = '#2F4F4F'
        lb1.pack()
        newWindow.mainloop()

    def sair(self):
        if tkinter.messagebox.askokcancel('Sair', "Deseja realmente sair?"):
            self.frame.master.destroy()


'''

    def printMessage(self):
        print("Wow, worked!")

        self.form = Entry(instancia)
        self.form.pack()

        self.calc = Button(self.frame3, text= "Calcule")
        self.calc.pack()
'''







instancia = Tk()
b = Inter(instancia)
instancia.mainloop()
