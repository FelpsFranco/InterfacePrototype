import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk
from Outros import centro
from paciente import Paciente
from BancoDeDados import acessobanco
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Outros import envia

blue_color = (197, 206, 237)
purple_color = (241, 242, 250)


def internacoes():
    # ---------------------------- Config --------------------------------------- #

    acessobanco.cria_banco()
    win_internos = Tk()
    win_internos.attributes('-alpha', 0.0)
    win_internos.geometry('1440x900')
    centro.centralizar(win_internos)
    win_internos.attributes('-alpha', 1.0)
    win_internos.resizable(height=False, width=False)
    win_internos.configure(bg='white')
    win_internos.title('Internação')

    # ---------------------------- Img -----------------------------------------#

    logo = PhotoImage(file='../Imagens/LOGO_HOSP.png')

    # ---------------------------- Labels -----------------------------------------#

    retangulo = Label(win_internos,
                      bg=centro.from_rgb(blue_color))
    retangulo.place(width=1440, height=250)

    panel_logo = Label(win_internos, image=logo,
                       bg=centro.from_rgb(blue_color))
    panel_logo.place(x=1267, y=10)

    titulo = Label(win_internos, text='Intensive Care Unit Control', font=('Bahnschrift Condensed', 24),
                   bg=centro.from_rgb(blue_color))
    titulo.place(x=60, y=50)

    # ---------------------------- Buttons -----------------------------------------#

    histo = Button(win_internos, bg=centro.from_rgb(blue_color), text='Pacientes',
                   font=('Bahnschrift Condensed', 14), command=chama_paciente, anchor=CENTER, borderwidth=2)
    histo.place(x=63, y=176, width=228, height=35)

    labo = Button(win_internos, bg=centro.from_rgb(blue_color), text='Cadastrar',
                  font=('Bahnschrift Condensed', 14), command=lambda: tela_cria(win_internos),
                  anchor=CENTER, borderwidth=2)
    labo.place(x=421, y=176, width=228, height=35)

    solicita = Button(win_internos, bg=centro.from_rgb(blue_color), text='Leitos Ocupados',
                      font=('Bahnschrift Condensed', 14), command=lambda: mostra_leitos(win_internos),
                      anchor=CENTER, borderwidth=2)
    solicita.place(x=779, y=176, width=228, height=35)

    medicam = Button(win_internos, bg=centro.from_rgb(blue_color), text='Transferência',
                     command=transfere, font=('Bahnschrift Condensed', 14), anchor=CENTER, borderwidth=2)
    medicam.place(x=1136, y=176, width=228, height=35)

    cria_grafico(win_internos)

    rectangle_grafic = Label(win_internos, text='Gráfico de Leitos', font=('Bahnschrift Condensed', 20),
                             bg='white', borderwidth=2, fg='black')
    rectangle_grafic.place(x=80, y=280)

    win_internos.mainloop()


def cria_grafico(janela):
    # ----------------------------- Pacientes -----------------------------------------#

    rows = acessobanco.grafico()
    internos = 0
    total_leitos = 20
    for row in rows:
        internos = internos + 1
    leitos_vazios = total_leitos - internos

    # ---------------------------- Atrela ao Tkinter  ---------------------------------#

    figura = plt.Figure(figsize=(6, 6), dpi=60)
    ax1 = figura.add_subplot(111)

    # ----------------------------- Cria Gráfico ---------------------------------------#

    canva = FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().place(x=-20, y=350)
    labels = 'Leitos Vazio', 'Internos'
    sizes = [leitos_vazios, internos]
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')


def mostra_leitos(janela):
    # ----------------------------- Cria Tela ---------------------------------------#

    janela.destroy()
    leitos_ocupados = Tk()
    leitos_ocupados.attributes('-alpha', 0.0)
    leitos_ocupados.geometry('700x400')
    centro.centralizar(leitos_ocupados)
    leitos_ocupados.attributes('-alpha', 1.0)
    leitos_ocupados.resizable(height=False, width=False)
    leitos_ocupados.configure(bg=centro.from_rgb(blue_color))
    leitos_ocupados.focus_force()
    leitos_ocupados.grab_set()
    leitos_ocupados.title('Leitos Ocupados')

    codigo_texto = Label(leitos_ocupados, text='Código', font=('Inter', 10),
                         bg=centro.from_rgb(blue_color))
    codigo_texto.place(x=20, y=350, width=65, height=19)

    codigo_input = Entry(leitos_ocupados, font=('Inter', 12), bg='white')
    codigo_input.place(x=80, y=350, width=200, height=20)

    dar_baixa = Button(leitos_ocupados, command=lambda: (muda_interno(leitos_ocupados, codigo_input)), text='Dar Baixa',
                       bg='white', anchor=CENTER, borderwidth=2)
    dar_baixa.place(x=300, y=348)

    leitos_ocupados.bind("<Return>", lambda e: muda_interno(leitos_ocupados, codigo_input))

    # ----------------------------- Cria árvore ----------------------------------------#

    tree = ttk.Treeview(leitos_ocupados, column=("Column1", "Column2", "Column3", "Column4", "Column5"),
                        show='headings')
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.place(x=0, y=0, width=700, height=250)
    tree.heading("#1", text="Codigo", anchor='w')
    tree.heading("#2", text="Pacientes", anchor='w')
    tree.heading("#3", text="Leito Ocupado", anchor='w')
    tree.heading("#4", text="Tipo", anchor='w')
    tree.heading("#5", text="Médico", anchor='w')
    rows = acessobanco.apresenta_leitos()
    for row in rows:
        tree.insert("", END, values=row)

    leitos_ocupados.protocol("WM_DELETE_WINDOW", lambda: evento_fechar(leitos_ocupados))
    leitos_ocupados.mainloop()


def evento_fechar(janela):
    janela.destroy()
    internacoes()


def muda_interno(leitos_ocupados, codigo_input):
    muda_status = codigo_input.get()
    acessobanco.upd_interno(muda_status)
    envia.libera_paciente()
    leitos_ocupados.destroy()
    internacoes()


def transfere():
    # ---------------------------- Tela Config ---------------------------------------#

    cadastro = Toplevel()
    cadastro.attributes('-alpha', 0.0)
    cadastro.geometry('800x600')
    centro.centralizar(cadastro)
    cadastro.attributes('-alpha', 1.0)
    cadastro.resizable(height=False, width=False)
    cadastro.configure(bg=centro.from_rgb(blue_color))
    cadastro.title('Cadastro')

    # ---------------------------- Imagens ---------------------------------------#

    imagem = PhotoImage(file='../Imagens/LOGO_HOSP.png')

    # ---------------------------- Painel de Pesquisa Labels ---------------------#
    rectangle_logo = Label(cadastro, bg='white')
    rectangle_logo.place(width=1440, height=150)

    panel = Label(cadastro, image=imagem, bg='white')
    panel.place(x=600, y=10)

    info = Label(cadastro, text='TRANSFERÊNCIA DE INTERNO',
                 bg='white', font=('Bahnschrift Condensed', 20))
    info.place(x=170, y=70)

    # ---------------------------- Cadastro Texts ---------------------------------------#

    text_name = Label(cadastro, text='Nome', font=('Inter', 10),
                      bg=centro.from_rgb(blue_color))
    text_name.place(x=20, y=200, width=65, height=19)

    text_cpf = Label(cadastro, text='CPF', font=('Inter', 10),
                     bg=centro.from_rgb(blue_color))
    text_cpf.place(x=400, y=200, width=65, height=19)

    text_codigo = Label(cadastro, text='Código', font=('Inter', 10),
                        bg=centro.from_rgb(blue_color))
    text_codigo.place(x=20, y=300, width=65, height=19)

    text_local = Label(cadastro, text='Local', font=('Inter', 10),
                       bg=centro.from_rgb(blue_color))
    text_local.place(x=400, y=400, width=65, height=19)

    text_leito = Label(cadastro, text='Leito', font=('Inter', 10),
                       bg=centro.from_rgb(blue_color))
    text_leito.place(x=400, y=300, width=65, height=19)

    text_medico = Label(cadastro, text='Médico', font=('Inter', 10),
                        bg=centro.from_rgb(blue_color))
    text_medico.place(x=20, y=400, width=65, height=19)

    # ---------------------------- Cadastro Inputs ---------------------------------------#

    input_name = Entry(cadastro, font=('Inter', 12), bg='white')
    input_name.place(x=80, y=195, width=300, height=30)

    input_cpf = Entry(cadastro, font=('Inter', 12), bg='white')
    input_cpf.place(x=460, y=195, width=300, height=30)

    input_codigo = Entry(cadastro, font=('Inter', 12), bg='white')
    input_codigo.place(x=80, y=295, width=300, height=30)

    input_leito = Entry(cadastro, font=('Inter', 12), bg='white')
    input_leito.place(x=460, y=300, width=300, height=30)

    lista_de_leitos = ['UTI', 'EFG', 'PS']
    lista_dos_leitos = ttk.Combobox(cadastro, values=lista_de_leitos)
    lista_dos_leitos.set('Nenhum')
    lista_dos_leitos.place(x=460, y=399)

    input_medico = Entry(cadastro, font=('Inter', 12), bg='white')
    input_medico.place(x=80, y=390, width=300, height=30)

    # ---------------------------- Cadastro Buttons ---------------------------------------#

    salvar = Button(cadastro, text='Salvar',
                    command=lambda: (
                        transferencia(input_codigo, input_leito, input_medico, lista_dos_leitos, cadastro)),
                    font=('Inter', 12), bg='white')
    salvar.place(x=250, y=500, width=100, height=23)

    cadastro.bind("<Return>",
                  lambda e: transferencia(input_codigo, input_leito, input_medico, lista_dos_leitos, cadastro))

    cancela = Button(cadastro, text='Cancelar', command=cadastro.destroy, font=('Inter', 12), bg='white')
    cancela.place(x=450, y=500, width=100, height=23)

    cadastro.mainloop()


def transferencia(input_codigo, input_leito, input_medico, lista_dos_leitos, janela):
    codigo_transf = input_codigo.get()
    leito_transf = input_leito.get()
    medico_transf = input_medico.get()
    tipo_transf = lista_dos_leitos.get()
    resultado = acessobanco.validacao(codigo_transf)
    if len(resultado) != 0:
        if leito_transf != '':
            acessobanco.updt_leito(leito_transf, codigo_transf)
        if tipo_transf != 0:
            acessobanco.updt_local(tipo_transf, codigo_transf)
        if medico_transf != '':
            acessobanco.updt_medico(medico_transf, codigo_transf)
        janela.destroy()
    else:
        tkinter.messagebox.showwarning('Transferência', 'Paciente não encontrado')


def tela_cria(janela):
    # ---------------------------- Tela Config ---------------------------------------#
    janela.destroy()
    cadastronovo = Tk()
    cadastronovo.attributes('-alpha', 0.0)
    cadastronovo.geometry('800x600')
    centro.centralizar(cadastronovo)
    cadastronovo.attributes('-alpha', 1.0)
    cadastronovo.resizable(height=False, width=False)
    cadastronovo.configure(bg=centro.from_rgb(blue_color))
    cadastronovo.title('Cadastro')

    # ---------------------------- Imagens ---------------------------------------#

    imagem = PhotoImage(file='../Imagens/LOGO_HOSP.png')

    # ---------------------------- Painel de Pesquisa Labels ---------------------------------------#

    rectangle_logo = Label(cadastronovo, bg='white')
    rectangle_logo.place(width=1440, height=150)

    panel = Label(cadastronovo, image=imagem, bg='white')
    panel.place(x=600, y=10)

    info = Label(cadastronovo, text='CADASTRO DE INTERNO', bg='white', font=('Bahnschrift Condensed', 20))
    info.place(x=170, y=70)

    # ---------------------------- Cadastro Texts ---------------------------------------#

    text_name = Label(cadastronovo, text='Nome', font=('Inter', 10),
                      bg=centro.from_rgb(blue_color))
    text_name.place(x=20, y=200, width=65, height=19)

    text_cpf = Label(cadastronovo, text='CPF', font=('Inter', 10),
                     bg=centro.from_rgb(blue_color))
    text_cpf.place(x=400, y=200, width=65, height=19)

    text_codigo = Label(cadastronovo, text='Código', font=('Inter', 10),
                        bg=centro.from_rgb(blue_color))
    text_codigo.place(x=20, y=300, width=65, height=19)

    text_local = Label(cadastronovo, text='Local', font=('Inter', 10),
                       bg=centro.from_rgb(blue_color))
    text_local.place(x=400, y=400, width=65, height=19)

    text_leito = Label(cadastronovo, text='Leito', font=('Inter', 10),
                       bg=centro.from_rgb(blue_color))
    text_leito.place(x=400, y=300, width=65, height=19)

    text_medico = Label(cadastronovo, text='Médico', font=('Inter', 10),
                        bg=centro.from_rgb(blue_color))
    text_medico.place(x=20, y=400, width=65, height=19)

    # ---------------------------- Cadastro Inputs ---------------------------------------#

    input_name = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_name.place(x=80, y=195, width=300, height=30)

    input_cpf = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_cpf.place(x=460, y=195, width=300, height=30)

    input_codigo = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_codigo.place(x=80, y=295, width=300, height=30)

    input_leito = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_leito.place(x=460, y=300, width=300, height=30)

    input_medico = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_medico.place(x=80, y=390, width=300, height=30)

    lista_de_leitos = ['UTI', 'EFG', 'PS']
    lista_dos_leitos = ttk.Combobox(cadastronovo, values=lista_de_leitos)
    lista_dos_leitos.set('Escolha')
    lista_dos_leitos.place(x=460, y=399)

    # ---------------------------- Cadastro Buttons ---------------------------------------#

    salvar = Button(cadastronovo, text='Salvar', command=lambda: (
        adiciona_novo(cadastronovo, input_name, input_cpf, input_codigo, input_leito, input_medico, lista_dos_leitos)),
                    font=('Inter', 12), bg='white')
    salvar.place(x=250, y=500, width=100, height=23)

    cadastronovo.bind("<Return>", lambda e: adiciona_novo(cadastronovo, input_name, input_cpf, input_codigo,
                                                          input_leito, input_medico, lista_dos_leitos))

    cancela = Button(cadastronovo, text='Cancelar', command=lambda: (cancelar(cadastronovo)), font=('Inter', 12),
                     bg='white')
    cancela.place(x=450, y=500, width=100, height=23)

    cadastronovo.protocol("WM_DELETE_WINDOW", lambda: evento_fechar(cadastronovo))
    cadastronovo.mainloop()


def cancelar(janela):
    janela.destroy()
    internacoes()


def adiciona_novo(janela, input_name, input_cpf, input_codigo, input_leito, input_medico, lista_dos_leitos):

    # ----------------------------- Aciona Classe Pacientes ---------------------------------------#

    pacientes = Paciente(input_codigo.get(), input_name.get(), input_cpf.get(), input_leito.get(),
                         input_medico.get(), lista_dos_leitos.get())
    resultado = pacientes.verifica_novo(pacientes.codigo)
    if len(resultado) != 0:
        tkinter.messagebox.showwarning('Cadastro', 'Já Existe Cadastro')
    else:
        pacientes.adiciona_novo(pacientes.codigo, pacientes.nome, pacientes.cpf, pacientes.leito,
                                pacientes.medico, pacientes.local)
        janela.destroy()
        internacoes()


def chama_paciente():
    win_pacientes = Toplevel()
    win_pacientes.attributes('-alpha', 0.0)
    win_pacientes.geometry('1440x1024')
    centro.centralizar(win_pacientes)
    win_pacientes.attributes('-alpha', 1.0)
    win_pacientes.resizable(height=False, width=False)
    win_pacientes.configure(bg='white')
    win_pacientes.title('Inicial')

    # ---------------------------- Imagens ---------------------------------------#

    logo = PhotoImage(file='../Imagens/LOGO_HOSP.png')

    # ---------------------------- Painel de Pesquisa Labels ---------------------------------------#

    rectangle_logo = Label(win_pacientes, bg=centro.from_rgb(blue_color))
    rectangle_logo.place(width=1440, height=149)

    panel_logo = Label(win_pacientes, image=logo, bg=centro.from_rgb(blue_color))
    panel_logo.place(x=1267, y=10)

    # ---------------------------- Painel de Pesquisa Text---------------------------------------#

    name_text = Label(win_pacientes, text='Nome', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    name_text.place(x=57, y=32, width=65, height=19)

    cpf_text = Label(win_pacientes, text='CPF', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    cpf_text.place(x=65, y=93, width=40, height=19)

    codigo_text = Label(win_pacientes, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    codigo_text.place(x=510, y=34, width=65, height=19)

    medico_text = Label(win_pacientes, text='Médico', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    medico_text.place(x=510, y=93, width=65, height=19)

    # ---------------------------- Painel de Pesquisa Input ---------------------------------------#

    name_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    name_input.place(x=120, y=25, width=300, height=30)

    cpf_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    cpf_input.place(x=120, y=87, width=300, height=30)

    codigo_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    codigo_input.place(x=579, y=29, width=367, height=30)

    medico_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    medico_input.place(x=579, y=87, width=367, height=30)

    # ---------------------------- Infor List ---------------------------------------#

    tree = ttk.Treeview(win_pacientes,
                        column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"),
                        show='headings')
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.place(x=0, y=149, width=1440, height=875)
    tree.heading("#1", text="Código", anchor='w')
    tree.heading("#2", text="Nome", anchor='w')
    tree.heading("#3", text="CPF", anchor='w')
    tree.heading("#4", text="Leito", anchor='w')
    tree.heading("#5", text="Médico", anchor='w')
    tree.heading("#6", text="Local", anchor='w')
    tree.heading("#7", text="Internado", anchor='w')
    rows = acessobanco.todos_paciente()
    for row in rows:
        tree.insert("", END, values=row)

    # ---------------------------- Painel de Pesquisa Button ---------------------------------------#

    voltar = Button(win_pacientes, bg='white', command=win_pacientes.destroy, text='Voltar',
                    anchor=CENTER)
    voltar.place(x=1100, y=29, width=100, height=35)

    win_pacientes.bind("<Return>",
                       lambda e: busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input, medico_input))

    busca_banco = Button(win_pacientes,
                         command=lambda: (win_pacientes, tree, codigo_input, name_input, cpf_input, medico_input),
                         bg='white', text='Buscar', anchor=CENTER)
    busca_banco.place(x=1100, y=87, width=100, height=35)
    win_pacientes.mainloop()


def busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input, medico_input):
    pega_codigo = codigo_input.get()
    pega_nome = name_input.get()
    pega_cpf = cpf_input.get()
    pega_medico = medico_input.get()

    # ---------------------------- Pesquisa por Geral ---------------------------------------#

    if pega_codigo == '' and pega_nome == '' and pega_cpf == '' and pega_medico == '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1440, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Leito", anchor='w')
        tree_especifica.heading("#5", text="Médico", anchor='w')
        tree_especifica.heading("#6", text="Local", anchor='w')
        tree_especifica.heading("#7", text="Internado", anchor='w')
        rows = acessobanco.filtro_todos()
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por Código ---------------------------------------#

    elif pega_codigo != '' and pega_nome == '' and pega_cpf == '' and pega_medico == '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1440, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Leito", anchor='w')
        tree_especifica.heading("#5", text="Médico", anchor='w')
        tree_especifica.heading("#6", text="Local", anchor='w')
        tree_especifica.heading("#7", text="Internado", anchor='w')
        rows = acessobanco.filtro_codigo(pega_codigo)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por Médico ---------------------------------------#

    elif pega_codigo == '' and pega_nome == '' and pega_cpf == '' and pega_medico != '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1440, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Leito", anchor='w')
        tree_especifica.heading("#5", text="Médico", anchor='w')
        tree_especifica.heading("#6", text="Local", anchor='w')
        tree_especifica.heading("#7", text="Internado", anchor='w')
        rows = acessobanco.filtro_medico(pega_medico)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por Nome ---------------------------------------#

    elif pega_codigo == '' and pega_nome != '' and pega_cpf == '' and pega_medico == '':
        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1440, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Leito", anchor='w')
        tree_especifica.heading("#5", text="Médico", anchor='w')
        tree_especifica.heading("#6", text="Local", anchor='w')
        tree_especifica.heading("#7", text="Internado", anchor='w')
        rows = acessobanco.filtro_nome(pega_nome)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por CPF ---------------------------------------#

    elif pega_codigo == '' and pega_nome == '' and pega_cpf != '' and pega_medico == '':
        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1440, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Leito", anchor='w')
        tree_especifica.heading("#5", text="Médico", anchor='w')
        tree_especifica.heading("#6", text="Local", anchor='w')
        tree_especifica.heading("#7", text="Internado", anchor='w')
        rows = acessobanco.filtro_cpf(pega_cpf)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree
