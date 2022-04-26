import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("cadastro.db")
cursor = conn.cursor()


def criaBanco():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cadastro (
                        codigo INTEGER NOT NULL PRIMARY KEY,
                        nome VARCHAR(40) NOT NULL,
                        cpf VARCHAR(14) NOT NULL,
                        leito TEXT NOT NULL,
                        medico TEXT NOT NULL,
                        local TEXT NOT NULL,
                        interno TEXT NOT NULL
                    );
                """)


def grafico():
    cur = conn.cursor()
    cur.execute("""
                            SELECT * FROM cadastro t where t.interno = 'Sim' """)
    rows = cur.fetchall()
    return rows


def verificaNovo(codigo):
    cursor.execute("""
                    SELECT codigo FROM cadastro t where t.codigo = ? """, (codigo,))
    resultado = cursor.fetchall()
    return resultado


def insereNovo(codigo, nome, cpf, leito, medico,tipo, interno):
    cursor.execute("""
                        INSERT INTO cadastro (codigo, nome, cpf, leito, medico, local, interno) VALUES (?, ?, ?, ?, ?, ?, ?)""",(codigo, nome, cpf, leito, medico, tipo, interno))
    conn.commit()


def todosPaciente():
    cur = conn.cursor()
    cur.execute("""
                     SELECT * FROM cadastro;
                     """)
    rows = cur.fetchall()
    return rows


def apresentaLeitos():
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


def filtroTodos():
    cur = conn.cursor()
    cur.execute("""
                     SELECT * FROM cadastro;
                     """)
    rows = cur.fetchall()
    return rows


def filtroCodigo(pega_codigo):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT * FROM cadastro t where t.codigo = ? """, (pega_codigo,))
    rows = cur.fetchall()
    return rows


def filtroMedico(pega_medico):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT * FROM cadastro t where t.medico LIKE ? """, (pega_medico,))
    rows = cur.fetchall()
    return rows

def filtroNome(pega_nome):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT * FROM cadastro t where t.nome = ? """, (pega_nome,))
    rows = cur.fetchall()
    return rows

def filtroCpf(pega_cpf):
    cur = conn.cursor()
    cur.execute("""
                                 SELECT * FROM cadastro t where t.cpf = ? """, (pega_cpf,))
    rows = cur.fetchall()
    return rows
