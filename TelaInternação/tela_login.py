from tkinter import *
from Outros import centro
# from TelaInternação import tela_interno

blue_color = (197, 206, 237)


def tela_login():

    # bancousers.verificaBanco()

    janela_login = Tk()
    janela_login.attributes('-alpha', 0.0)
    janela_login.geometry('400x500')
    centro.centralizar(janela_login)
    janela_login.attributes('-alpha', 1.0)
    janela_login.resizable(height=False, width=False)
    janela_login.configure(bg=centro.from_rgb(blue_color))
    janela_login.title('Inicial')

    # ---------------------------- Texts ---------------------------------------#

    login_text = Label(janela_login, text='Login', bg=centro.from_rgb(blue_color))
    login_text.place(x=50, y=200)

    senha_text = Label(janela_login, text='Senha', bg=centro.from_rgb(blue_color))
    senha_text.place(x=50, y=250)

    # ---------------------------- Input ----------------------------------------#

    login_input = Entry(janela_login, font=('Inter', 12), bg='white')
    login_input.place(x=100, y=200, width=200)

    senha_input = Entry(janela_login, font=('Inter', 12), bg='white')
    senha_input.place(x=100, y=250, width=200)

    # ---------------------------- Button ----------------------------------------#

    entrar = Button(janela_login, text='Entrar', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    entrar.place(x=230, y=350, height=18, width=100)

    cadastrar = Button(janela_login, text='Cadastrar', font=('Inter', 10), bg=centro.from_rgb(blue_color))
    cadastrar.place(x=70, y=350, height=18, width=100)

    janela_login.mainloop()


tela_login()
