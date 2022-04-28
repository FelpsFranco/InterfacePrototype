import sqlite3

conn = sqlite3.connect("cadastro.db")
cursor = conn.cursor()


def verificaBanco():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuario (
                        id_user INTEGER NOT NULL PRIMARY KEY,
                        login VARCHAR(15) NOT NULL,
                        senha VARCHAR(14) NOT NULL,
                        email VARCHAR(40) NOT NULL
                    );
                """)


def verificaExiste(getlogin):
    cursor.execute("""
                SELECT login FROM usuario t WHERE t.login = ?""", getlogin)
    resultado = cursor.fetchall()
    return resultado

def verificaSenha():
    cursor.execute("""
                    """)