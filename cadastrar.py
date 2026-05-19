import sqlite3


def cadastrarPessoa():

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,

        cargo TEXT NOT NULL CHECK(
            cargo IN (
                'Professor',
                'Aluno',
                'TAE',
                'Diretor',
                'Gestor'
            )
        )
    )
    """)

    idPessoa = int(input("Matricula da pessoa: "))
    nomePessoa = input("Nome da pessoa: ")
    cargoPessoa = input(
        "Cargo (Professor/Aluno/TAE/Diretor/Gestor): "
    )

    cursor.execute(
        "INSERT INTO pessoas (id, nome, cargo) VALUES (?, ?, ?)",
        (idPessoa, nomePessoa, cargoPessoa)
    )

    conexao.commit()
    conexao.close()

    print("Pessoa cadastrada!")