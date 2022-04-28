from tkinter import *
import centro
import bancousers

blue_color = (197, 206, 237)


class Login:
    def __init__(self):
        # bancousers.verificaBanco()
        self.janela_login = Tk()
        self.janela_login.attributes('-alpha', 0.0)
        self.janela_login.geometry('400x500')
        centro.Centro(self.janela_login)
        self.janela_login.attributes('-alpha', 1.0)
        self.janela_login.resizable(height=False, width=False)
        self.janela_login.configure(bg=centro.from_rgb(blue_color))
        self.janela_login.title('Inicial')

        # ---------------------------- Texts ---------------------------------------#

        self.loginText = Label(self.janela_login, text='Login', bg=centro.from_rgb(blue_color))
        self.loginText.place(x=50, y=200)

        self.senhaText = Label(self.janela_login, text='Senha', bg=centro.from_rgb(blue_color))
        self.senhaText.place(x=50, y=250)

        # ---------------------------- Input ----------------------------------------#

        self.loginInput = Entry(self.janela_login, font=('Inter', 12), bg='white')
        self.loginInput.place(x=100, y=200, width=200)

        self.senhaInput = Entry(self.janela_login, font=('Inter', 12), bg='white')
        self.senhaInput.place(x=100, y=250, width=200)

        # ---------------------------- Button ----------------------------------------#

        self.entrar = Button(self.janela_login, text='Entrar', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.entrar.place(x=230, y=350, height=18, width=100)

        self.cadastrar = Button(self.janela_login, text='Cadastrar', font=('Inter', 10), bg=centro.from_rgb(blue_color))
        self.cadastrar.place(x=70, y=350, height=18, width=100)

        self.janela_login.mainloop()

    def acessaAmbiente(self):
        getlogin = self.loginInput.get()
        resultado = bancousers.verificaExiste(getlogin)
        if resultado != 0:



Login()
