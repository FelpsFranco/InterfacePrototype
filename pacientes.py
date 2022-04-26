import centro
from tkinter import *

import tkinter.ttk as ttk
import acessobanco

blue_color = (197, 206, 237)
purple_color = (241, 242, 250)


class Pacientes:

    # ---------------------------- Tela Config ---------------------------------------#

    def __init__(self):
        self.win_pacientes = Toplevel()
        self.win_pacientes.attributes('-alpha', 0.0)
        self.win_pacientes.geometry('1440x1024')
        centro.Centro(self.win_pacientes)
        self.win_pacientes.attributes('-alpha', 1.0)
        self.win_pacientes.resizable(height=False, width=False)
        self.win_pacientes.configure(bg='white')
        self.win_pacientes.title('Inicial')

        # ---------------------------- Imagens ---------------------------------------#

        self.logo = PhotoImage(file='./Imagens/LOGO_HOSP.png')

        # ---------------------------- Painel de Pesquisa Labels ---------------------------------------#

        self.rectangle_logo = Label(self.win_pacientes, bg=centro.from_rgb(blue_color))
        self.rectangle_logo.place(width=1440, height=149)

        self.panel_logo = Label(self.win_pacientes, image=self.logo, bg=centro.from_rgb(blue_color))
        self.panel_logo.place(x=1267, y=10)

        # ---------------------------- Painel de Pesquisa Text---------------------------------------#

        self.name_text = Label(self.win_pacientes, text='Nome', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.name_text.place(x=57, y=32, width=65, height=19)

        self.cpf_text = Label(self.win_pacientes, text='CPF', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.cpf_text.place(x=65, y=93, width=40, height=19)

        self.codigo_text = Label(self.win_pacientes, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.codigo_text.place(x=510, y=34, width=65, height=19)

        self.medico_text = Label(self.win_pacientes, text='Médico', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.medico_text.place(x=510, y=93, width=65, height=19)

        # ---------------------------- Painel de Pesquisa Input ---------------------------------------#

        self.name_input = Entry(self.win_pacientes, font=('Inter', 12), bg='white')
        self.name_input.place(x=120, y=25, width=300, height=30)

        self.cpf_input = Entry(self.win_pacientes, font=('Inter', 12), bg='white')
        self.cpf_input.place(x=120, y=87, width=300, height=30)

        self.codigo_input = Entry(self.win_pacientes, font=('Inter', 12), bg='white')
        self.codigo_input.place(x=579, y=29, width=367, height=30)

        self.medico_input = Entry(self.win_pacientes, font=('Inter', 12), bg='white')
        self.medico_input.place(x=579, y=87, width=367, height=30)

        # ---------------------------- Painel de Pesquisa Button ---------------------------------------#

        self.voltar = Button(self.win_pacientes, bg='white', command=self.win_pacientes.destroy, text='Voltar', anchor=CENTER)
        self.voltar.place(x=1100, y=29, width=100, height=35)

        self.win_pacientes.bind("<Return>", lambda e: self.busca_paciente())

        self.busca_banco = Button(self.win_pacientes, command=self.busca_paciente, bg='white', text='Buscar', anchor=CENTER)
        self.busca_banco.place(x=1100, y=87, width=100, height=35)

        # ---------------------------- Infor List ---------------------------------------#

        self.tree = ttk.Treeview(self.win_pacientes, column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.place(x=0, y=149, width=1440, height=875)
        self.tree.heading("#1", text="Código", anchor='w')
        self.tree.heading("#2", text="Nome", anchor='w')
        self.tree.heading("#3", text="CPF", anchor='w')
        self.tree.heading("#4", text="Leito", anchor='w')
        self.tree.heading("#5", text="Médico", anchor='w')
        self.tree.heading("#6", text="Local", anchor='w')
        self.tree.heading("#7", text="Internado", anchor='w')
        rows = acessobanco.todosPaciente()
        for row in rows:
            self.tree.insert("", END, values=row)
        self.win_pacientes.mainloop()

    def busca_paciente(self):
        pega_codigo = self.codigo_input.get()
        pega_nome = self.name_input.get()
        pega_cpf = self.cpf_input.get()
        pega_medico = self.medico_input.get()

        # ---------------------------- Pesquisa por Geral ---------------------------------------#

        if pega_codigo == '' and pega_nome == '' and pega_cpf == '' and pega_medico == '':

            self.tree_especifica = ttk.Treeview(self.win_pacientes,column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
            scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            self.tree_especifica.place(x=0, y=149, width=1440, height=875)
            self.tree_especifica.heading("#1", text="Código", anchor='w')
            self.tree_especifica.heading("#2", text="Nome", anchor='w')
            self.tree_especifica.heading("#3", text="CPF", anchor='w')
            self.tree_especifica.heading("#4", text="Leito", anchor='w')
            self.tree_especifica.heading("#5", text="Médico", anchor='w')
            self.tree_especifica.heading("#6", text="Local", anchor='w')
            self.tree_especifica.heading("#7", text="Internado", anchor='w')
            rows = acessobanco.filtroTodos()
            for row in rows:
                self.tree_especifica.insert("", END, values=row)
            self.tree = self.tree_especifica

        # ---------------------------- Pesquisa Por Código ---------------------------------------#

        elif pega_codigo != '' and pega_nome == '' and pega_cpf == '' and pega_medico == '':

            self.tree_especifica = ttk.Treeview(self.win_pacientes, column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
            scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            self.tree_especifica.place(x=0, y=149, width=1440, height=875)
            self.tree_especifica.heading("#1", text="Código", anchor='w')
            self.tree_especifica.heading("#2", text="Nome", anchor='w')
            self.tree_especifica.heading("#3", text="CPF", anchor='w')
            self.tree_especifica.heading("#4", text="Leito", anchor='w')
            self.tree_especifica.heading("#5", text="Médico", anchor='w')
            self.tree_especifica.heading("#6", text="Local", anchor='w')
            self.tree_especifica.heading("#7", text="Internado", anchor='w')
            rows = acessobanco.filtroCodigo(pega_codigo)
            for row in rows:
                self.tree_especifica.insert("", END, values=row)
            self.tree = self.tree_especifica

        # ---------------------------- Pesquisa Por Médico ---------------------------------------#

        elif pega_codigo == '' and pega_nome == '' and pega_cpf == '' and pega_medico != '':

            self.tree_especifica = ttk.Treeview(self.win_pacientes, column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
            scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            self.tree_especifica.place(x=0, y=149, width=1440, height=875)
            self.tree_especifica.heading("#1", text="Código", anchor='w')
            self.tree_especifica.heading("#2", text="Nome", anchor='w')
            self.tree_especifica.heading("#3", text="CPF", anchor='w')
            self.tree_especifica.heading("#4", text="Leito", anchor='w')
            self.tree_especifica.heading("#5", text="Médico", anchor='w')
            self.tree_especifica.heading("#6", text="Local", anchor='w')
            self.tree_especifica.heading("#7", text="Internado", anchor='w')
            rows = acessobanco.filtroMedico(pega_medico)
            for row in rows:
                self.tree_especifica.insert("", END, values=row)
            self.tree = self.tree_especifica

        # ---------------------------- Pesquisa Por Nome ---------------------------------------#

        elif pega_codigo == '' and pega_nome != '' and pega_cpf == '' and pega_medico == '':
            self.tree_especifica = ttk.Treeview(self.win_pacientes, column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
            scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            self.tree_especifica.place(x=0, y=149, width=1440, height=875)
            self.tree_especifica.heading("#1", text="Código", anchor='w')
            self.tree_especifica.heading("#2", text="Nome", anchor='w')
            self.tree_especifica.heading("#3", text="CPF", anchor='w')
            self.tree_especifica.heading("#4", text="Leito", anchor='w')
            self.tree_especifica.heading("#5", text="Médico", anchor='w')
            self.tree_especifica.heading("#6", text="Local", anchor='w')
            self.tree_especifica.heading("#7", text="Internado", anchor='w')
            rows = acessobanco.filtroNome(pega_nome)
            for row in rows:
                self.tree_especifica.insert("", END, values=row)
            self.tree = self.tree_especifica

        # ---------------------------- Pesquisa Por CPF ---------------------------------------#

        elif pega_codigo == '' and pega_nome == '' and pega_cpf != '' and pega_medico == '':
            self.tree_especifica = ttk.Treeview(self.win_pacientes, column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
            scrollbar = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            self.tree_especifica.place(x=0, y=149, width=1440, height=875)
            self.tree_especifica.heading("#1", text="Código", anchor='w')
            self.tree_especifica.heading("#2", text="Nome", anchor='w')
            self.tree_especifica.heading("#3", text="CPF", anchor='w')
            self.tree_especifica.heading("#4", text="Leito", anchor='w')
            self.tree_especifica.heading("#5", text="Médico", anchor='w')
            self.tree_especifica.heading("#6", text="Local", anchor='w')
            self.tree_especifica.heading("#7", text="Internado", anchor='w')
            rows = acessobanco.filtroCpf(pega_cpf)
            for row in rows:
                self.tree_especifica.insert("", END, values=row)
            self.tree = self.tree_especifica







