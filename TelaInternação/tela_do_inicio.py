from tkinter import *
from Outros import centro
import tela_interno

blue_color = (197, 206, 237)


def interno(janela):
    janela.destroy()
    tela_interno.internacoes()


def tela_login():
    janela_inicial = Tk()
    janela_inicial.attributes('-alpha', 0.0)
    janela_inicial.geometry('1440x700')
    centro.centralizar(janela_inicial)
    janela_inicial.attributes('-alpha', 1.0)
    janela_inicial.resizable(height=False, width=False)
    janela_inicial.configure(bg=centro.from_rgb(blue_color))
    janela_inicial.title('Inicial')

    # ---------------------------- Img -----------------------------------------#

    logo = PhotoImage(file='../Imagens/LOGO_HOSP.png')

    # ---------------------------- Labels -----------------------------------------#

    retangulo = Label(janela_inicial,
                      bg=centro.from_rgb(blue_color))
    retangulo.place(width=1440, height=250)

    panel_logo = Label(janela_inicial, image=logo,
                       bg=centro.from_rgb(blue_color))
    panel_logo.place(x=1267, y=10)

    titulo = Label(janela_inicial, text='Intensive Care Unit Control', font=('Bahnschrift Condensed', 24),
                   bg=centro.from_rgb(blue_color))
    titulo.place(x=60, y=50)

    interna = Button(janela_inicial, bg=centro.from_rgb(blue_color), text='Internação',
                     font=('Bahnschrift Condensed', 14), command=lambda: interno(janela_inicial), anchor=CENTER,
                     borderwidth=2)
    interna.place(x=63, y=176, width=228, height=35)

    janela_inicial.mainloop()


tela_login()
