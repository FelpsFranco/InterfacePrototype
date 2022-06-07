import datetime

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
data_atual = datetime.datetime


def internacoes():
    # ---------------------------- Config --------------------------------------- #

    acessobanco.cria_banco()
    win_internos = Toplevel()
    win_internos.attributes('-alpha', 0.0)
    win_internos.geometry('1300x700')
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
    panel_logo.place(x=1100, y=10)

    titulo = Label(win_internos, text='Intensive Care Unit Control', font=('Bahnschrift Condensed', 24),
                   bg=centro.from_rgb(blue_color))
    titulo.place(x=60, y=50)

    # ---------------------------- Buttons -----------------------------------------#

    internar = Button(win_internos, bg=centro.from_rgb(blue_color), text='Internar',
                      font=('Bahnschrift Condensed', 14), command=lambda: internar_paciente(win_internos),
                      anchor=CENTER, borderwidth=2)
    internar.place(x=23, y=176, width=228, height=35)

    labo = Button(win_internos, bg=centro.from_rgb(blue_color), text='Cadastrar',
                  font=('Bahnschrift Condensed', 14), command=lambda: tela_cria(win_internos),
                  anchor=CENTER, borderwidth=2)
    labo.place(x=381, y=176, width=228, height=35)

    solicita = Button(win_internos, bg=centro.from_rgb(blue_color), text='Leitos Ocupados',
                      font=('Bahnschrift Condensed', 14), command=lambda: mostra_leitos(win_internos),
                      anchor=CENTER, borderwidth=2)
    solicita.place(x=739, y=176, width=228, height=35)

    medicam = Button(win_internos, bg=centro.from_rgb(blue_color), text='Transferência',
                     command=transfere, font=('Bahnschrift Condensed', 14), anchor=CENTER, borderwidth=2)
    medicam.place(x=1066, y=176, width=228, height=35)

    cria_grafico(win_internos)

    rectangle_grafic = Label(win_internos, text='Total Leitos', font=('Bahnschrift Condensed', 20),
                             bg='white', borderwidth=2, fg='black')
    rectangle_grafic.place(x=110, y=280)

    rectangle_grafic = Label(win_internos, text='Leitos UTI', font=('Bahnschrift Condensed', 20),
                             bg='white', borderwidth=2, fg='black')
    rectangle_grafic.place(x=550, y=280)

    rectangle_grafic = Label(win_internos, text='Leitos PS', font=('Bahnschrift Condensed', 20),
                             bg='white', borderwidth=2, fg='black')
    rectangle_grafic.place(x=1000, y=280)

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

    rowsb = acessobanco.graficob()
    uti_total = 15
    internos_uti = 0
    for rowb in rowsb:
        internos_uti = internos_uti + 1
    uti_vazio = uti_total - internos_uti

    figura2 = plt.Figure(figsize=(6, 6), dpi=60)
    ax2 = figura2.add_subplot(111)

    canva2 = FigureCanvasTkAgg(figura2, janela)
    canva2.get_tk_widget().place(x=400, y=350)
    labels1 = 'Leitos Vazio', 'Internos'
    sizes1 = [uti_vazio, internos_uti]
    ax2.pie(sizes1, labels=labels1, autopct='%1.1f%%', shadow=True, startangle=90)
    ax2.axis('equal')

    rowsc = acessobanco.graficoc()
    ps_total = 5
    internos_ps = 0
    for rowc in rowsc:
        internos_ps = internos_ps + 1
    ps_vazio = ps_total - internos_ps

    figura3 = plt.Figure(figsize=(6, 6), dpi=60)
    ax3 = figura3.add_subplot(111)

    canva3 = FigureCanvasTkAgg(figura3, janela)
    canva3.get_tk_widget().place(x=850, y=350)
    labels2 = 'Leitos Vazio', 'Internos'
    sizes2 = [ps_vazio, internos_ps]
    ax3.pie(sizes2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
    ax3.axis('equal')



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
    email = acessobanco.email_info(muda_status)
    nome = acessobanco.nome_info(muda_status)
    envia.libera_paciente(email, nome)
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

    # input_leito = Entry(cadastro, font=('Inter', 12), bg='white')
    # input_leito.place(x=460, y=300, width=300, height=30)

    listas_de_leitos = ['1', '2', '3', '4', '5', '6', '7']
    input_leito = ttk.Combobox(cadastro, values=listas_de_leitos)
    input_leito.set('Leito')
    input_leito.place(x=460, y=300)

    lista_de_leitos = ['UTI', 'EFG', 'PS']
    lista_dos_leitos = ttk.Combobox(cadastro, values=lista_de_leitos)
    lista_dos_leitos.set('Nenhum')
    lista_dos_leitos.place(x=460, y=398)

    # input_medico = Entry(cadastro, font=('Inter', 12), bg='white')
    # input_medico.place(x=80, y=390, width=300, height=30)

    lista_de_medico = ['Dr. Amanda', 'Dr. Josué', 'Dr. Peixoto', 'Dr. Alicia']
    input_medico = ttk.Combobox(cadastro, values=lista_de_medico)
    input_medico.set('Médicos')
    input_medico.place(x=80, y=398)

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
    cadastronovo = Toplevel()
    cadastronovo.attributes('-alpha', 0.0)
    cadastronovo.geometry('1300x700')
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
    panel.place(x=1100, y=10)

    info = Label(cadastronovo, text='CADASTRO DE INTERNO', bg='white', font=('Bahnschrift Condensed', 20))
    info.place(x=170, y=70)

    # ---------------------------- Cadastro Texts ---------------------------------------#

    text_name = Label(cadastronovo, text='Nome', font=('Inter', 10),
                      bg=centro.from_rgb(blue_color))
    text_name.place(x=20, y=200, width=65, height=19)

    text_cpf = Label(cadastronovo, text='CPF', font=('Inter', 10),
                     bg=centro.from_rgb(blue_color))
    text_cpf.place(x=400, y=200, width=65, height=19)

    text_endereco = Label(cadastronovo, text='Endereço', font=('Inter', 10),
                          bg=centro.from_rgb(blue_color))
    text_endereco.place(x=20, y=285, width=65, height=19)

    text_fone = Label(cadastronovo, text='Fone', font=('Inter', 10),
                      bg=centro.from_rgb(blue_color))
    text_fone.place(x=400, y=285, width=65, height=19)

    text_email = Label(cadastronovo, text='Email', font=('Inter', 10),
                       bg=centro.from_rgb(blue_color))
    text_email.place(x=20, y=375, width=65, height=19)

    text_mae = Label(cadastronovo, text='Nome da Mãe', font=('Inter', 10),
                     bg=centro.from_rgb(blue_color))
    text_mae.place(x=780, y=200)

    nasc_data_text = Label(cadastronovo, text='Data de Nasc.', font=('Inter', 10),
                           bg=centro.from_rgb(blue_color))
    nasc_data_text.place(x=780, y=285)

    # ---------------------------- Cadastro Inputs ---------------------------------------#

    input_name = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_name.place(x=80, y=195, width=300, height=30)

    input_cpf = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_cpf.place(x=460, y=195, width=300, height=30)

    input_endereco = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_endereco.place(x=80, y=280, width=300, height=30)

    input_fone = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_fone.place(x=460, y=280, width=300, height=30)

    input_email = Entry(cadastronovo, font=('Inter', 12), bg='white')
    input_email.place(x=80, y=370, width=300, height=30)

    input_mae = Entry(cadastronovo, font=('Inter', 10),
                      bg='white')
    input_mae.place(x=870, y=195, width=300, height=30)

    nasc_data_input = Entry(cadastronovo, font=('Inter', 10),
                            bg='white')
    nasc_data_input.place(x=870, y=280, width=300, height=30)

    # lista_de_leitos = ['UTI', 'EFG', 'PS']
    # lista_dos_leitos = ttk.Combobox(cadastronovo, values=lista_de_leitos)
    # lista_dos_leitos.set('Escolha')
    # lista_dos_leitos.place(x=460, y=349)

    # ---------------------------- Cadastro Buttons ---------------------------------------#

    salvar = Button(cadastronovo, text='Salvar', command=lambda: (
        adiciona_novo(cadastronovo, input_name, input_cpf, input_fone, input_endereco, input_email)),
                    font=('Inter', 12), bg='white')
    salvar.place(x=250, y=500, width=100, height=23)

    cadastronovo.bind("<Return>",
                      lambda e: adiciona_novo(cadastronovo, input_name, input_cpf, input_fone, input_endereco,
                                              input_email))

    cancela = Button(cadastronovo, text='Cancelar', command=lambda: (cancelar(cadastronovo)), font=('Inter', 12),
                     bg='white')
    cancela.place(x=450, y=500, width=100, height=23)

    cadastronovo.protocol("WM_DELETE_WINDOW", lambda: evento_fechar(cadastronovo))
    cadastronovo.mainloop()


def cancelar(janela):
    janela.destroy()
    internacoes()


def adiciona_novo(janela, input_name, input_cpf, input_fone, input_endereco, input_email):
    # ----------------------------- Aciona Classe Pacientes ---------------------------------------#

    pacientes = Paciente(input_name.get(), input_cpf.get(), input_fone.get(), input_endereco.get(), input_email.get())
    resultado = pacientes.verifica_novo(pacientes.cpf)
    if len(resultado) != 0:
        tkinter.messagebox.showwarning('Cadastro', 'Já Existe Cadastro')
    else:
        pacientes.adiciona_novo(pacientes.nome, pacientes.cpf, pacientes.fone, pacientes.end, pacientes.email)
        janela.destroy()
        internacoes()


def internar_paciente(janela):
    janela.destroy()
    win_pacientes = Toplevel()
    win_pacientes.attributes('-alpha', 0.0)
    win_pacientes.geometry('1300x1024')
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
    panel_logo.place(x=1120, y=10)

    # ---------------------------- Painel de Pesquisa Text---------------------------------------#

    name_text = Label(win_pacientes, text='Nome', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    name_text.place(x=57, y=32, width=65, height=19)

    cpf_text = Label(win_pacientes, text='CPF', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    cpf_text.place(x=65, y=93, width=40, height=19)

    codigo_text = Label(win_pacientes, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    codigo_text.place(x=510, y=34, width=65, height=19)

    confirma_text = Label(win_pacientes, text='Confirme o Código', font=('Inter', 10), bg='white')
    confirma_text.place(x=34, y=600)

    lista_de_medico = ['Dr. Amanda', 'Dr. Josué', 'Dr. Peixoto', 'Dr. Alicia']
    lista_dos_medicos = ttk.Combobox(win_pacientes, values=lista_de_medico)
    lista_dos_medicos.set('Médicos')
    lista_dos_medicos.place(x=34, y=700)

    lista_de_leitos = ['1', '2', '3', '4', '5', '6', '7']
    lista_dos_leitos = ttk.Combobox(win_pacientes, values=lista_de_leitos)
    lista_dos_leitos.set('Leito')
    lista_dos_leitos.place(x=326, y=700)

    lista_de_local = ['UTI', 'EFG', 'PS']
    lista_dos_locais = ttk.Combobox(win_pacientes, values=lista_de_local)
    lista_dos_locais.set('Local')
    lista_dos_locais.place(x=180, y=700)

    # ---------------------------- Painel de Pesquisa Input ---------------------------------------#

    name_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    name_input.place(x=120, y=25, width=300, height=30)

    cpf_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    cpf_input.place(x=120, y=87, width=300, height=30)

    codigo_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    codigo_input.place(x=579, y=29, width=367, height=30)

    confirma_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    confirma_input.place(x=150, y=600, width=150, height=30)

    # ---------------------------- Painel de Pesquisa Button ---------------------------------------#

    voltar = Button(win_pacientes, bg='white', command=lambda: cancelar(win_pacientes), text='Voltar',
                    anchor=CENTER)
    voltar.place(x=1000, y=29, width=100, height=35)

    win_pacientes.bind("<Return>",
                       lambda e: busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input))

    busca_banco = Button(win_pacientes,
                         command=lambda: busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input),
                         bg='white', text='Buscar', anchor=CENTER)
    busca_banco.place(x=1000, y=87, width=100, height=35)

    finalizar = Button(win_pacientes, bg='white', command=lambda: (
        interna_paciente(win_pacientes, confirma_input.get(), lista_dos_medicos.get(), lista_dos_locais.get(),
                         lista_dos_leitos.get())), text='Salvar', anchor=CENTER)
    finalizar.place(x=500, y=700, width=100, height=25)

    # ---------------------------- Infor List ---------------------------------------#

    tree = ttk.Treeview(win_pacientes,
                        column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"),
                        show='headings')
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.place(x=0, y=149, width=1300, height=400)
    tree.heading("#1", text="Código", anchor='w')
    tree.heading("#2", text="Nome", anchor='w')
    tree.heading("#3", text="CPF", anchor='w')
    tree.heading("#4", text="Telefone", anchor='w')
    tree.heading("#5", text="Endereço", anchor='w')
    tree.heading("#6", text="E-mail", anchor='w')
    tree.heading("#7", text="Data Cadastro", anchor='w')
    win_pacientes.protocol("WM_DELETE_WINDOW", lambda: evento_fechar(win_pacientes))

    win_pacientes.mainloop()


def interna_paciente(janela, codigoget, medicoget, localget, leitoget):
    codigo = codigoget
    medico = medicoget
    local = localget
    leito = leitoget
    internado = 'Sim'
    # resultado = acessobanco.validacao(codigo)
    # if resultado == 0:
    acessobanco.internando(codigo, medico, local, leito, internado)
    janela.destroy()
    internacoes()
    # elif resultado == 0:
    #     tkinter.messagebox.showwarning('Internação', 'Paciente Não Encontrado')


def busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input):
    pega_codigo = codigo_input.get()
    pega_nome = name_input.get()
    pega_cpf = cpf_input.get()

    # ---------------------------- Pesquisa Por Código ---------------------------------------#

    if pega_codigo != '' and pega_nome == '' and pega_cpf == '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=400)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Telefone", anchor='w')
        tree_especifica.heading("#5", text="Endereço", anchor='w')
        tree_especifica.heading("#6", text="E-mail", anchor='w')
        tree_especifica.heading("#7", text="Cadastro", anchor='w')
        rows = acessobanco.filtro_codigo(pega_codigo)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por Nome ---------------------------------------#

    elif pega_codigo == '' and pega_nome != '' and pega_cpf == '':
        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=400)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Telefone", anchor='w')
        tree_especifica.heading("#5", text="Endereço", anchor='w')
        tree_especifica.heading("#6", text="E-mail", anchor='w')
        tree_especifica.heading("#7", text="Cadastro", anchor='w')
        rows = acessobanco.filtro_nome(pega_nome)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por CPF ---------------------------------------#

    elif pega_codigo == '' and pega_nome == '' and pega_cpf != '':
        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=400)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Telefone", anchor='w')
        tree_especifica.heading("#5", text="Endereço", anchor='w')
        tree_especifica.heading("#6", text="E-mail", anchor='w')
        tree_especifica.heading("#7", text="Cadastro", anchor='w')
        rows = acessobanco.filtro_cpf(pega_cpf)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree
