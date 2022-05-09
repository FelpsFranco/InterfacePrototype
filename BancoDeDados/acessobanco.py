import tkinter.messagebox
import sqlite3
from datetime import date

data_atual = date.today()
conn = sqlite3.connect("../cadastro.db")
cursor = conn.cursor()


def cria_banco():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cadastro (
                        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR(40) NOT NULL,
                        cpf VARCHAR(14) NOT NULL,
                        leito TEXT,
                        medico TEXT,
                        local TEXT,
                        fone VARCHAR(18) NOT NULL,
                        end VARCHAR(40),
                        email VARCHAR(40),
                        interno TEXT NOT NULL,
                        data_cadastro DATETIME,
                        data_interna DATETIME,
                        data_saida DATETIME 
                    );
                """)


def grafico():
    cur = conn.cursor()
    cur.execute("""
                            SELECT * FROM cadastro t where t.interno = 'Sim' """)
    rows = cur.fetchall()
    return rows


def verifica_novo(cpf):
    cursor.execute("""
                    SELECT cpf FROM cadastro t where t.cpf = ? """, (cpf,))
    resultado = cursor.fetchall()
    return resultado


def insere_novo(nome, cpf, fone, endereco, email, interno):
    data = data_atual
    cursor.execute("""
                        INSERT INTO cadastro (nome, cpf, fone, end, email, interno, data_cadastro) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                   (nome, cpf, fone, endereco, email, interno, data))
    conn.commit()


def todos_paciente():
    cur = conn.cursor()
    cur.execute("""
                     SELECT codigo, nome, cpf, fone, end, email, data_cadastro FROM cadastro;
                     """)
    rows = cur.fetchall()
    return rows


def apresenta_leitos():
    cur = conn.cursor()
    cur.execute("""
                        SELECT codigo, nome, leito, local, medico FROM cadastro t where t.interno = 'Sim' """)
    rows = cur.fetchall()
    return rows


def upd_interno(muda_status):
    status = 'Não'
    cursor.execute("""
                    UPDATE cadastro SET interno = ? WHERE codigo = ?""", (status, muda_status))
    conn.commit()


def validacao(codigo_transf):
    if codigo_transf != '':
        valida = cursor.execute("""
                    SELECT codigo FROM cadastro t where t.codigo = ? """, (codigo_transf,))
        result = valida.fetchall()
        return result


def updt_leito(leito_transf, codigo_transf):
    troca_leito = cursor.execute("""
                                SELECT leito FROM cadastro t where t.leito = ? """, (leito_transf,))
    verifica_leito = troca_leito.fetchall()
    if len(verifica_leito) == 0:
        cursor.execute("""
                    UPDATE cadastro SET leito = ? WHERE codigo = ?""", (leito_transf, codigo_transf))
        conn.commit()
    else:
        tkinter.messagebox.showwarning('Transferência', 'Leito Já Existente')


def updt_local(tipo_transf, codigo_transf):
    cursor.execute("""
                    UPDATE cadastro SET local = ? WHERE codigo = ? """, (tipo_transf, codigo_transf))
    conn.commit()


def updt_medico(medico_transf, codigo_transf):
    cursor.execute("""
                    UPDATE cadastro SET medico = ? WHERE codigo = ? """, (medico_transf, codigo_transf))
    conn.commit()


def filtro_todos():
    cur = conn.cursor()
    cur.execute("""
                     SELECT codigo, nome, cpf, fone, end, email, data_cadastro FROM cadastro;
                     """)
    rows = cur.fetchall()
    return rows


def filtro_codigo(pega_codigo):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT codigo, nome, cpf, fone, end, email, data_cadastro FROM cadastro t where t.codigo = ? """, (pega_codigo,))
    rows = cur.fetchall()
    return rows


def filtro_fone(pega_fone):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT codigo, nome, cpf, fone, end, email, data_cadastro FROM cadastro where fone LIKE ? """, (pega_fone + "%",))
    rows = cur.fetchall()
    return rows


def filtro_nome(pega_nome):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT codigo, nome, cpf, fone, end, email, data_cadastro FROM cadastro where nome LIKE  ? """, (pega_nome + "%",))
    rows = cur.fetchall()
    return rows


def filtro_cpf(pega_cpf):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT codigo, nome, cpf, fone, end, email, data_cadastro FROM cadastro t where t.cpf = ? """, (pega_cpf,))
    rows = cur.fetchall()
    return rows

def email_info(pega_codigo):
    cur = conn.cursor()
    cur.execute("""
                SELECT email FROM cadastro t WHERE t.codigo = ? """, (pega_codigo,))
    email = cur.fetchall()
    return email

def nome_info(pega_codigo):
    cur = conn.cursor()
    cur.execute("""
                SELECT nome FROM cadastro t where t.codigo = ? """, (pega_codigo,))
    nome = cur.fetchall()
    return nome

def valida_cod(codigo):
    cur = conn.cursor()
    cur.execute("""
                SELECT cpf FROM cadastro t WHERE t.codigo = ? """, (codigo,))
    resultado = cur.fetchall()
    return resultado

def internando(codigo, medico, local, leito, interno):
    data_interna = data_atual
    cursor.execute("""
                    UPDATE cadastro SET medico = ?, local = ?, leito = ?, interno = ?, data_interna = ? WHERE codigo = ?  """, (medico, local, leito, interno, data_interna, codigo))
