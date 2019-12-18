from tkinter import *
import tkinter as tk
import cliData
from tkinter import messagebox as ms
import tkinter.messagebox


class Cliente:
    def __init__(self,root):
        self.root = root

        self.root.geometry("720x670+0+0")
        self.root.title("Cadastrar Cliente")
        self.root.config(bg="Ghost White")

        Name = StringVar()
        Idade = StringVar()
        Sexo = StringVar()
        Mail = StringVar()
        Fone = StringVar()


        def Sair():
            Sair = tkinter.messagebox.askyesno("Cadastrar Cliente ","Confirma para sair")
            if Sair > 0:
                root.destroy()
                return
        def clearData():
            self.txtName.delete(0,END)
            self.txtdade.delete(0, END)
            self.txtsex.delete(0, END)
            self.txtmail.delete(0, END)
            self.txtfone.delete(0, END)

        #                                            ------FRAMES-------
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial',45,'bold'), text="Cadastro do Usuário", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2,width=720, height=70, padx=10, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1,width=550, height=400, padx=20, pady=20,relief=RIDGE, bg="Ghost White")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=300, height=500, padx=25, relief = RIDGE, bg = "Ghost White",
                                   font=('arial',20,'bold'),text="Informações do Cliente\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=200, height=400, padx=29, pady=5, relief=RIDGE, bg="Ghost White",
                                   font=('arial',20,'bold'),text="Detalhes\n")
        DataFrameRIGHT.pack(side=RIGHT)

#                                            ------LABEL-------
        self.lblName = Label(DataFrameLEFT, font=('arial', 20, 'bold'),text="Nome: ",padx=2,pady=2,bg="Ghost White")
        self.lblName.grid(row=0,column=0,sticky=W)
        self.txtName = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Name,  width=15)
        self.txtName.grid(row=0, column=1)

        self.lbldade = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Idade:  ", padx=2, pady=2,
                             bg="Ghost White")
        self.lbldade.grid(row=1, column=0, sticky=W)
        self.txtdade = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Idade, width=15)
        self.txtdade.grid(row=1, column=1)

        self.lblsex = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Sexo:  ", padx=2, pady=2,
                             bg="Ghost White")
        self.lblsex.grid(row=1, column=0, sticky=W)
        self.txtsex = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Sexo, width=15)
        self.txtsex.grid(row=1, column=1)


        self.lblmail = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Email: ", padx=2, pady=2, bg="Ghost White")
        self.lblmail.grid(row=2, column=0, sticky=W)
        self.txtmail = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mail,  width=15)
        self.txtmail.grid(row=2, column=1)

        self.lblfone = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Telefone: ", padx=2, pady=2,
                             bg="Ghost White")
        self.lblfone.grid(row=3, column=0, sticky=W)
        self.txtfone = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Fone,  width=15)
        self.txtfone.grid(row=3, column=1)
#                                            ------Caia de lista-------


        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1, sticky='ns')

        listacad = Listbox(DataFrameRIGHT,width=25,height=14, font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        listacad.grid(row=0, column=0, padx=8)
        scrollbar.config(command = listacad.yview)


#                                            ------Buttons-------
# adiciona cliente
        self.btnAddDate = Button(ButtonFrame,text="Criar", font=("arial",20,"bold"), height=1, width=7,bd=3)
        self.btnAddDate.grid(row=0,column=0)
#atualiza update
        self.btnUpdateData = Button(ButtonFrame, text="Atualizar", font=("arial", 20, "bold"), height=1, width=7, bd=3)
        self.btnUpdateData.grid(row=0, column=1)
# clear limpa
        self.btnClearData = Button(ButtonFrame, text="Limpa", font=("arial", 20, "bold"), height=1, width=7, bd=3,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnAddDate = Button(ButtonFrame, text="Deletar", font=("arial", 20, "bold"), height=1, width=7, bd=3)
        self.btnAddDate.grid(row=0, column=3)

        self.btnExit = Button(ButtonFrame, text="Sair", font=("arial", 20, "bold"),height=1,width=9,bd=3,bg='red', command=Sair)
        self.btnExit.grid(row=0,column=6)


if __name__ =='__main__':
    root = Tk()
    app = Cliente(root)
    root.mainloop()







'''
    def put_cliente(self):



        # label texto
        self.lblNome = Label(fin, text="Nome:  ", font=('', 12)).grid(row=0, column=0)
        self.lblmail = Label(fin, text="Email:  ", font=('', 12)).grid(row=2, column=0)
        self.lbltelefone = Label(fin, text="Telefone:  ", font=('', 12)).grid(row=3, column=0)
  #      self.lblNome = Label(fin, text="Sexo:  ", font=('', 12)).grid(row=4, column=0)

        
        v = tk.IntVar()
        c = tk.IntVar()
        self.newsexo = Radiobutton(fin, variable=v, value=0, text="Masculino")
        self.newsex = Radiobutton(fin, variable=v, value=1, text="Feminino")
        self.newsexo.grid(row=4, column=1)
        self.newsex.grid(row=4, column=2)
        
        # input
        self.txtNome = Entry(fin).grid(row=0, column=1)
        self.txtmail = Entry(fin).grid(row=2, column=1)
        self.txtfone = Entry(fin).grid(row=3, column=1)
        Button(fin, text='Cadastrar', bg="green", padx=5, pady=5, command=self.insert_bd).grid(row=6, columnspan=5)

    def create_table(self):
        with sqlite3.connect('user.db') as db:
            c = db.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS client ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL , email TEXT NOT NULL ,telefone TEXT NOT NULL );')

        db.commit()
        db.close()
        


    def insert_bd(nome, mail, fone):



        with sqlite3.connect('user.db') as db:
            c = db.cursor()
        # Create New Account

        c.execute("INSERT INTO client VALUES (NULL, ?,?,?)", nome, mail, telefone)
        db.commit()
        db.close()
        """
        c.execute("insert into client (nome, email, telefone) values('" + self.nome + "','" + self.mail + "','" + self.telefone + "')")
        db.commit()
        """



# root.title("Login Form")


'''