from tkinter import *
import tkinter.ttk as ttk
from Outros import centro
import tela_interno
from BancoDeDados import acessobanco
from paciente import Paciente
import tkinter.messagebox

blue_color = (197, 206, 237)


def interno(janela):
    janela.destroy()
    tela_interno.internacoes()


def busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input, fone_input):
    pega_codigo = codigo_input.get()
    pega_nome = name_input.get()
    pega_cpf = cpf_input.get()
    pega_fone = fone_input.get()

    # ---------------------------- Pesquisa por Geral ---------------------------------------#

    if pega_codigo == '' and pega_nome == '' and pega_cpf == '' and pega_fone == '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Telefone", anchor='w')
        tree_especifica.heading("#5", text="Endereço", anchor='w')
        tree_especifica.heading("#6", text="E-mail", anchor='w')
        tree_especifica.heading("#7", text="Cadastro", anchor='w')
        rows = acessobanco.filtro_todos()
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por Código ---------------------------------------#

    elif pega_codigo != '' and pega_nome == '' and pega_cpf == '' and pega_fone == '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=875)
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

    # ---------------------------- Pesquisa Por Médico ---------------------------------------#

    elif pega_codigo == '' and pega_nome == '' and pega_cpf == '' and pega_fone != '':

        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=875)
        tree_especifica.heading("#1", text="Código", anchor='w')
        tree_especifica.heading("#2", text="Nome", anchor='w')
        tree_especifica.heading("#3", text="CPF", anchor='w')
        tree_especifica.heading("#4", text="Telefone", anchor='w')
        tree_especifica.heading("#5", text="Endereço", anchor='w')
        tree_especifica.heading("#6", text="E-mail", anchor='w')
        tree_especifica.heading("#7", text="Cadastro", anchor='w')
        rows = acessobanco.filtro_fone(pega_fone)
        for row in rows:
            tree_especifica.insert("", END, values=row)
        tree = tree_especifica
        return tree

    # ---------------------------- Pesquisa Por Nome ---------------------------------------#

    elif pega_codigo == '' and pega_nome != '' and pega_cpf == '' and pega_fone == '':
        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=875)
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

    elif pega_codigo == '' and pega_nome == '' and pega_cpf != '' and pega_fone == '':
        tree_especifica = ttk.Treeview(win_pacientes, column=(
            "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show='headings')
        scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree_especifica.place(x=0, y=149, width=1300, height=875)
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


def chama_paciente():
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
    panel_logo.place(x=1150, y=10)

    # ---------------------------- Painel de Pesquisa Text---------------------------------------#

    name_text = Label(win_pacientes, text='Nome', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    name_text.place(x=57, y=32, width=65, height=19)

    cpf_text = Label(win_pacientes, text='CPF', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    cpf_text.place(x=65, y=93, width=40, height=19)

    codigo_text = Label(win_pacientes, text='Código', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    codigo_text.place(x=510, y=34, width=65, height=19)

    fone_text = Label(win_pacientes, text='Telefone', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    fone_text.place(x=510, y=93, width=65, height=19)

    # ---------------------------- Painel de Pesquisa Input ---------------------------------------#

    name_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    name_input.place(x=120, y=25, width=300, height=30)

    cpf_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    cpf_input.place(x=120, y=87, width=300, height=30)

    codigo_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    codigo_input.place(x=579, y=29, width=367, height=30)

    fone_input = Entry(win_pacientes, font=('Inter', 12), bg='white')
    fone_input.place(x=579, y=87, width=367, height=30)

    # ---------------------------- Infor List ---------------------------------------#

    tree = ttk.Treeview(win_pacientes,
                        column=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"),
                        show='headings')
    scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.place(x=0, y=149, width=1300, height=875)
    tree.heading("#1", text="Código", anchor='w')
    tree.heading("#2", text="Nome", anchor='w')
    tree.heading("#3", text="CPF", anchor='w')
    tree.heading("#4", text="Telefone", anchor='w')
    tree.heading("#5", text="Endereço", anchor='w')
    tree.heading("#6", text="E-mail", anchor='w')
    tree.heading("#7", text="Data Cadastro", anchor='w')
    rows = acessobanco.todos_paciente()
    for row in rows:
        tree.insert("", END, values=row)

    # ---------------------------- Painel de Pesquisa Button ---------------------------------------#

    voltar = Button(win_pacientes, bg='white', command=win_pacientes.destroy, text='Voltar',
                    anchor=CENTER)
    voltar.place(x=980, y=29, width=100, height=35)

    win_pacientes.bind("<Return>",
                       lambda e: busca_paciente(win_pacientes, tree, codigo_input, name_input, cpf_input, fone_input))

    busca_banco = Button(win_pacientes,
                         command=lambda: (win_pacientes, tree, codigo_input, name_input, cpf_input, fone_input),
                         bg='white', text='Buscar', anchor=CENTER)
    busca_banco.place(x=980, y=87, width=100, height=35)
    win_pacientes.mainloop()


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

    text_endereco = Label(cadastronovo, text='Endereço', font=('Inter', 10),
                          bg=centro.from_rgb(blue_color))
    text_endereco.place(x=20, y=285, width=65, height=19)

    text_fone = Label(cadastronovo, text='Fone', font=('Inter', 10),
                      bg=centro.from_rgb(blue_color))
    text_fone.place(x=400, y=285, width=65, height=19)

    text_email = Label(cadastronovo, text='Email', font=('Inter', 10),
                       bg=centro.from_rgb(blue_color))
    text_email.place(x=20, y=375, width=65, height=19)

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

    cancela = Button(cadastronovo, text='Cancelar', command=lambda: (evento_fechar(cadastronovo)), font=('Inter', 12),
                     bg='white')
    cancela.place(x=450, y=500, width=100, height=23)

    cadastronovo.protocol("WM_DELETE_WINDOW", lambda: evento_fechar(cadastronovo))
    cadastronovo.mainloop()


def adiciona_novo(janela, input_name, input_cpf, input_fone, input_endereco, input_email):
    # ----------------------------- Aciona Classe Pacientes ---------------------------------------#

    pacientes = Paciente(input_name.get(), input_cpf.get(), input_fone.get(), input_endereco.get(), input_email.get())
    resultado = pacientes.verifica_novo(pacientes.cpf)
    if len(resultado) != 0:
        tkinter.messagebox.showwarning('Cadastro', 'Já Existe Cadastro')
    else:
        pacientes.adiciona_novo(pacientes.nome, pacientes.cpf, pacientes.fone, pacientes.end, pacientes.email)
        janela.destroy()
        tela_login()


def evento_fechar(janela):
    janela.destroy()
    tela_login()


def tela_login():
    janela_inicial = Tk()
    janela_inicial.attributes('-alpha', 0.0)
    janela_inicial.geometry('1300x700')
    centro.centralizar(janela_inicial)
    janela_inicial.attributes('-alpha', 1.0)
    janela_inicial.resizable(height=False, width=False)
    janela_inicial.configure(bg=centro.from_rgb(blue_color))
    janela_inicial.title('Inicial')

    # ---------------------------- Img -----------------------------------------#

    logo = PhotoImage(file='../Imagens/LOGO_HOSP.png')
    doacao = PhotoImage(file='../Imagens/urgencia.png')
    info = PhotoImage(file='../Imagens/info-amamentacao.png')

    # ---------------------------- Labels -----------------------------------------#

    retangulo = Label(janela_inicial,
                      bg=centro.from_rgb(blue_color))
    retangulo.place(width=1440, height=250)

    label_oculta = Label(janela_inicial, bg=centro.from_rgb(blue_color))
    label_oculta.place(x=500, y=200)

    panel_logo = Label(janela_inicial, image=logo,
                       bg=centro.from_rgb(blue_color))
    panel_logo.place(x=1067, y=10)

    titulo = Label(janela_inicial, text='Registration Form', font=('Bahnschrift Condensed', 24),
                   bg=centro.from_rgb(blue_color))
    titulo.place(x=60, y=50)

    interna = Button(janela_inicial, bg=centro.from_rgb(blue_color), text='Internação',
                     font=('Bahnschrift Condensed', 14), command=lambda: interno(janela_inicial), anchor=CENTER,
                     borderwidth=2)
    interna.place(x=63, y=176, width=228, height=35)

    labo = Button(janela_inicial, bg=centro.from_rgb(blue_color), text='Pacientes',
                  font=('Bahnschrift Condensed', 14), command=chama_paciente,
                  anchor=CENTER, borderwidth=2)
    labo.place(x=421, y=176, width=228, height=35)

    cadastro = Button(janela_inicial, bg=centro.from_rgb(blue_color), text='Cadastrar',
                      font=('Bahnschrift Condensed', 14), command=lambda: tela_cria(janela_inicial),
                      anchor=CENTER, borderwidth=2)
    cadastro.place(x=779, y=176, width=228, height=35)

    image_oculta = Button(janela_inicial, bg=centro.from_rgb(blue_color), text='Tipos de Urgência',
                          font=('Bahnschrift Condensed', 14), command=lambda: oculta(label_oculta, doacao))
    image_oculta.place(x=63, y=400, width=228, height=35)
    info_oculta = Button(janela_inicial, bg=centro.from_rgb(blue_color), text='Doação Leite',
                         font=('Bahnschrift Condensed', 14), command=lambda: oculta_info(label_oculta, info))
    info_oculta.place(x=63, y=500, width=228, height=35)
    janela_inicial.mainloop()


def oculta(label, foto):
    label['image'] = foto
    label.place(x=550, y=350)


def oculta_info(label, foto):
    label['image'] = foto
    label.place(x=500, y=250)


tela_login()
