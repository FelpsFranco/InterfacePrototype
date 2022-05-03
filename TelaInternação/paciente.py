from BancoDeDados import acessobanco


class Paciente:
    def __init__(self, codigo, nome, cpf, leito, medico, local):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.leito = leito
        self.medico = medico
        self.local = local

    def verifica_novo(self, codigoget):
        self.codigo = codigoget
        resultado = acessobanco.verifica_novo(self.codigo)
        return resultado

    def adiciona_novo(self, codigoget, nomeget, cpfget, leitoget, medicoget, listaget):
        self.codigo = codigoget
        self.nome = nomeget
        self.cpf = cpfget
        self.leito = leitoget
        self.medico = medicoget
        self.local = listaget
        interno = 'Sim'
        acessobanco.insere_novo(self.codigo, self.nome, self.cpf, self.leito, self.medico, self.local, interno)
