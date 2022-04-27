import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
import centro
import acessobanco
import pacientes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


blue_color = (197, 206, 237)
purple_color = (241, 242, 250)


class Inicial:
    def __init__(self):
        # ---------------------------- Tela Config ---------------------------------------#
        acessobanco.criaBanco()
        self.win_initial = Tk()
        self.win_initial.attributes('-alpha', 0.0)
        self.win_initial.geometry('1440x1024')
        centro.Centro(self.win_initial)
        self.win_initial.attributes('-alpha', 1.0)
        self.win_initial.resizable(height=False, width=False)
        self.win_initial.configure(bg='white')
        self.win_initial.title('Inicial')

        # ---------------------------- Imagens ---------------------------------------#

        self.logo = PhotoImage(file='./Imagens/LOGO_HOSP.png')

        # ---------------------------- Painel de Pesquisa Labels ---------------------------------------#

        self.rectangle_logo = Label(self.win_initial, bg=centro.from_rgb(blue_color))
        self.rectangle_logo.place(width=1440, height=250)

        self.panel_logo = Label(self.win_initial, image=self.logo, bg=centro.from_rgb(blue_color))
        self.panel_logo.place(x=1267, y=10)

        self.titulo = Label(self.win_initial, text='Intensive Care Unit Control', font=('Bahnschrift Condensed', 24), bg=centro.from_rgb(blue_color))
        self.titulo.place(x=60, y=50)

        # ---------------------------- Painel de Informação Buttons ---------------------------------------#

        self.histo = Button(self.win_initial, bg=centro.from_rgb(blue_color), text='Pacientes', font=('Bahnschrift Condensed', 14), command=self.chama_todos, anchor=CENTER, borderwidth=2)
        self.histo.place(x=63, y=176, width=228, height=35)

        self.labo = Button(self.win_initial, bg=centro.from_rgb(blue_color), text='Cadastrar', font=('Bahnschrift Condensed', 14), command=self.telaCria, anchor=CENTER, borderwidth=2)
        self.labo.place(x=421, y=176, width=228, height=35)

        self.solicita = Button(self.win_initial, bg=centro.from_rgb(blue_color), text='Leitos Ocupados', font=('Bahnschrift Condensed', 14), command=self.mostraLeitos, anchor=CENTER, borderwidth=2)
        self.solicita.place(x=779, y=176, width=228, height=35)

        self.medicam = Button(self.win_initial, bg=centro.from_rgb(blue_color), text='Transferência', command=self.transfere, font=('Bahnschrift Condensed', 14), anchor=CENTER, borderwidth=2)
        self.medicam.place(x=1136, y=176, width=228, height=35)

        self.criaGrafico()
        self.rectangle_grafic = Label(self.win_initial, text='Gráfico de Leitos', font=('Bahnschrift Condensed', 20), bg='white', borderwidth=2, fg='black')
        self.rectangle_grafic.place(x=80, y=280)

        self.win_initial.mainloop()

    def chama_todos(self):
        pacientes.Pacientes()

    def criaGrafico(self):
        # ---------------------------- Verifica Paciente ---------------------------------------#

        rows = acessobanco.grafico()
        internos = 0
        total_leitos = 20
        for row in rows:
            internos = internos + 1
        leitos_vazios = total_leitos - internos

        # ---------------------------- Atrela ao Tkinter  ---------------------------------------#

        self.figura = plt.Figure(figsize=(6, 6), dpi=60)
        ax1 = self.figura.add_subplot(111)

        # ---------------------------- Cria Gráfico ---------------------------------------#

        canva = FigureCanvasTkAgg(self.figura, self.win_initial)
        canva.get_tk_widget().place(x=-25, y=350)
        labels = 'Leitos Vazio', 'Internos'
        sizes = [leitos_vazios, internos]
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')

    def mostraLeitos(self):
        self.leitos_ocupados = Tk()
        self.leitos_ocupados.attributes('-alpha', 0.0)
        self.leitos_ocupados.geometry('700x400')
        centro.Centro(self.leitos_ocupados)
        self.leitos_ocupados.attributes('-alpha', 1.0)
        self.leitos_ocupados.resizable(height=False, width=False)
        self.leitos_ocupados.configure(bg=centro.from_rgb(blue_color))
        self.leitos_ocupados.focus_force()
        self.leitos_ocupados.grab_set()
        self.leitos_ocupados.title('Leitos Ocupados')

        self.codigo_texto = Label(self.leitos_ocupados, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.codigo_texto.place(x=20, y=350, width=65, height=19)

        self.codigo_input = Entry(self.leitos_ocupados, font=('Inter', 12), bg='white')
        self.codigo_input.place(x=80, y=350, width=200, height=20)

        self.dar_baixa = Button(self.leitos_ocupados, command=self.muda_interno, text='Dar Baixa', bg='white', anchor=CENTER, borderwidth=2)
        self.dar_baixa.place(x=300, y=348)

        self.leitos_ocupados.bind("<Return>", lambda e: self.muda_interno())

        tree = ttk.Treeview(self.leitos_ocupados, column=("Column1", "Column2", "Column3", "Column4", "Column5"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.place(x=0, y=0, width=700, height=250)
        tree.heading("#1", text="Codigo", anchor='w')
        tree.heading("#2", text="Pacientes", anchor='w')
        tree.heading("#3", text="Leito Ocupado", anchor='w')
        tree.heading("#4", text="Tipo", anchor='w')
        tree.heading("#5", text="Médico", anchor='w')
        rows = acessobanco.apresentaLeitos()
        for row in rows:
            tree.insert("", END, values=row)

        self.leitos_ocupados.mainloop()

    def muda_interno(self):
        muda_status = self.codigo_input.get()
        acessobanco.upd_interno(muda_status)

        self.leitos_ocupados.destroy()

    def transfere(self):
        # ---------------------------- Tela Config ---------------------------------------#

        self.cadastro = Toplevel()
        self.cadastro.attributes('-alpha', 0.0)
        self.cadastro.geometry('800x600')
        centro.Centro(self.cadastro)
        self.cadastro.attributes('-alpha', 1.0)
        self.cadastro.resizable(height=False, width=False)
        self.cadastro.configure(bg=centro.from_rgb(blue_color))
        self.cadastro.title('Cadastro')

        # ---------------------------- Imagens ---------------------------------------#

        self.imagem = PhotoImage(
            file='./Imagens/LOGO_HOSP.png')

        # ---------------------------- Painel de Pesquisa Labels ---------------------------------------#

        self.rectangle_logo = Label(self.cadastro, bg='white')
        self.rectangle_logo.place(width=1440, height=150)

        self.panel = Label(self.cadastro, image=self.imagem, bg='white')
        self.panel.place(x=600, y=10)

        self.info = Label(self.cadastro, text='TRANSFERÊNCIA DE INTERNO', bg='white', font=('Bahnschrift Condensed', 20))
        self.info.place(x=170, y=70)

        # ---------------------------- Cadastro Texts ---------------------------------------#

        self.text_name = Label(self.cadastro, text='Nome', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_name.place(x=20, y=200, width=65, height=19)

        self.text_cpf = Label(self.cadastro, text='CPF', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_cpf.place(x=400, y=200, width=65, height=19)

        self.text_codigo = Label(self.cadastro, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_codigo.place(x=20, y=300, width=65, height=19)

        self.text_local = Label(self.cadastro, text='Local', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_local.place(x=400, y=400, width=65, height=19)

        self.text_leito = Label(self.cadastro, text='Leito', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_leito.place(x=400, y=300, width=65, height=19)

        self.text_medico = Label(self.cadastro, text='Médico', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_medico.place(x=20, y=400, width=65, height=19)

        # ---------------------------- Cadastro Inputs ---------------------------------------#

        self.input_name = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_name.place(x=80, y=195, width=300, height=30)

        self.input_cpf = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_cpf.place(x=460, y=195, width=300, height=30)

        self.input_codigo = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_codigo.place(x=80, y=295, width=300, height=30)

        self.input_leito = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_leito.place(x=460, y=300, width=300, height=30)

        self.lista_de_leitos = ['UTI', 'EFG', 'PS']
        self.lista_dos_leitos = ttk.Combobox(self.cadastro, values=self.lista_de_leitos)
        self.lista_dos_leitos.set('Nenhum')
        self.lista_dos_leitos.place(x=460, y=399)

        self.input_medico = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_medico.place(x=80, y=390, width=300, height=30)

        # ---------------------------- Cadastro Buttons ---------------------------------------#

        self.salvar = Button(self.cadastro, text='Salvar', command=self.transferencia, font=('Inter', 12), bg='white')
        self.salvar.place(x=250, y=500, width=100, height=23)

        self.cadastro.bind("<Return>", lambda e: self.transferencia())

        self.cancela = Button(self.cadastro, text='Cancelar', command=self.cadastro.destroy, font=('Inter', 12), bg='white')
        self.cancela.place(x=450, y=500, width=100, height=23)

        self.cadastro.mainloop()

    def transferencia(self):
        codigo_transf = self.input_codigo.get()
        leito_transf = self.input_leito.get()
        medico_transf = self.input_medico.get()
        tipo_transf = self.lista_dos_leitos.get()

        resultado = acessobanco.validacao(codigo_transf)
        if len(resultado) != 0:
            if leito_transf != '':
                acessobanco.updt_leito(leito_transf, codigo_transf)
            if tipo_transf != 0:
                acessobanco.updt_local(tipo_transf, codigo_transf)
            if medico_transf != '':
                acessobanco.updt_medico(medico_transf, codigo_transf)
            self.cadastro.destroy()
            self.mostraLeitos()
        else:
            tkinter.messagebox.showwarning('Transferência', 'Paciente não encontrado')

    def telaCria(self):
        # ---------------------------- Tela Config ---------------------------------------#
        self.cadastro = Toplevel()
        self.cadastro.attributes('-alpha', 0.0)
        self.cadastro.geometry('800x600')
        centro.Centro(self.cadastro)
        self.cadastro.attributes('-alpha', 1.0)
        self.cadastro.resizable(height=False, width=False)
        self.cadastro.configure(bg=centro.from_rgb(blue_color))
        self.cadastro.title('Cadastro')

        # ---------------------------- Imagens ---------------------------------------#

        self.imagem = PhotoImage(file='./Imagens/LOGO_HOSP.png')

        # ---------------------------- Painel de Pesquisa Labels ---------------------------------------#

        self.rectangle_logo = Label(self.cadastro, bg='white')
        self.rectangle_logo.place(width=1440, height=150)

        self.panel = Label(self.cadastro, image=self.imagem, bg='white')
        self.panel.place(x=600, y=10)

        self.info = Label(self.cadastro, text='CADASTRO DE INTERNO', bg='white', font=('Bahnschrift Condensed', 20))
        self.info.place(x=170, y=70)

        # ---------------------------- Cadastro Texts ---------------------------------------#

        self.text_name = Label(self.cadastro, text='Nome', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_name.place(x=20, y=200, width=65, height=19)

        self.text_cpf = Label(self.cadastro, text='CPF', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_cpf.place(x=400, y=200, width=65, height=19)

        self.text_codigo = Label(self.cadastro, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_codigo.place(x=20, y=300, width=65, height=19)

        self.text_local = Label(self.cadastro, text='Local', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_local.place(x=400, y=400, width=65, height=19)

        self.text_leito = Label(self.cadastro, text='Leito', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_leito.place(x=400, y=300, width=65, height=19)

        self.text_medico = Label(self.cadastro, text='Médico', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.text_medico.place(x=20, y=400, width=65, height=19)

        # ---------------------------- Cadastro Inputs ---------------------------------------#

        self.input_name = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_name.place(x=80, y=195, width=300, height=30)

        self.input_cpf = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_cpf.place(x=460, y=195, width=300, height=30)

        self.input_codigo = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_codigo.place(x=80, y=295, width=300, height=30)

        self.input_leito = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_leito.place(x=460, y=300, width=300, height=30)

        self.lista_de_leitos = ['UTI', 'EFG', 'PS']
        self.lista_dos_leitos = ttk.Combobox(self.cadastro, values=self.lista_de_leitos)
        self.lista_dos_leitos.set('Escolha')
        self.lista_dos_leitos.place(x=460, y=399)

        self.input_medico = Entry(self.cadastro, font=('Inter', 12), bg='white')
        self.input_medico.place(x=80, y=390, width=300, height=30)

        # ---------------------------- Cadastro Buttons ---------------------------------------#

        self.salvar = Button(self.cadastro, text='Salvar', command=self.adicionaNovo, font=('Inter', 12), bg='white')
        self.salvar.place(x=250, y=500, width=100, height=23)

        self.cadastro.bind("<Return>", lambda e: self.adicionaNovo())

        self.cancela = Button(self.cadastro, text='Cancelar', command=self.cadastro.destroy, font=('Inter', 12), bg='white')
        self.cancela.place(x=450, y=500, width=100, height=23)

        self.cadastro.mainloop()

    def adicionaNovo(self):
        nome = self.input_name.get()
        cpf = self.input_cpf.get()
        codigo = self.input_codigo.get()
        leito = self.input_leito.get()
        medico = self.input_medico.get()
        tipo = self.lista_dos_leitos.get()
        interno = 'Sim'
        resultado = acessobanco.verificaNovo(codigo)
        if len(resultado) != 0:
            tkinter.messagebox.showwarning('Cadastro', 'Já Existe Cadastro')
        else:
            acessobanco.insereNovo(codigo, nome, cpf, leito, medico, tipo, interno)
            self.cadastro.destroy()
            self.figura = self.criaGrafico()


Inicial()
