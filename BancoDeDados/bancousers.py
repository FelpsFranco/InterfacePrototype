import sqlite3

conn = sqlite3.connect("../cadastro.db")
cursor = conn.cursor()


def verifica_banco():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuario (
                        id_user INTEGER NOT NULL PRIMARY KEY,
                        login VARCHAR(15) NOT NULL,
                        senha VARCHAR(14) NOT NULL,
                        email VARCHAR(40) NOT NULL
                    );
                """)


def verifica_existe(getlogin):
    cursor.execute("""
                SELECT login FROM usuario t WHERE t.login = ?""", getlogin)
    resultado = cursor.fetchall()
    return resultado

def verifica_senha():
    cursor.execute("""
                    """)
