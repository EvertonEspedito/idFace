import sqlite3

def listarPessoas():

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, cargo FROM pessoas"
    )

    pessoas = cursor.fetchall()

    if not pessoas:
        print("Nenhuma pessoa cadastrada!")
    else:
        print("Pessoas cadastradas:")
        for pessoa in pessoas:
            print(f"ID: {pessoa[0]}, Nome: {pessoa[1]}, Cargo: {pessoa[2]}")

    conexao.close()