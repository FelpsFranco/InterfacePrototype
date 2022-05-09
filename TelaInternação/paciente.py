from BancoDeDados import acessobanco


class Paciente:
    def __init__(self, nome, cpf,  fone, endereco, email):
        self.end = endereco
        self.fone = fone
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def verifica_novo(self, cpfget):
        self.cpf = cpfget
        resultado = acessobanco.verifica_novo(self.cpf)
        return resultado

    def adiciona_novo(self, nomeget, cpfget, foneget, endget, emailget):
        self.fone = foneget
        self.end = endget
        self.nome = nomeget
        self.cpf = cpfget
        self.email = emailget
        interno = 'Não'
        acessobanco.insere_novo(self.nome, self.cpf, self.fone, self.end, self.email, interno)
