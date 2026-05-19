import sqlite3
import os
import shutil


def apagarPessoa():

    idPessoa = input("ID da pessoa para apagar: ")

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    # Verifica se existe
    cursor.execute(
        "SELECT nome FROM pessoas WHERE id = ?",
        (idPessoa,)
    )

    pessoa = cursor.fetchone()

    if not pessoa:

        print("Pessoa não encontrada!")

        conexao.close()
        return

    nome = pessoa[0]

    confirmacao = input(
        f"Deseja apagar {nome}? (s/n): "
    )

    if confirmacao.lower() != "s":

        print("Operação cancelada.")

        conexao.close()
        return

    # Remove do banco
    cursor.execute(
        "DELETE FROM pessoas WHERE id = ?",
        (idPessoa,)
    )

    conexao.commit()
    conexao.close()

    # Remove pasta de fotos
    pasta = f"fotos/{idPessoa}"

    if os.path.exists(pasta):

        shutil.rmtree(pasta)

        print("Fotos removidas!")

    else:

        print("Pasta de fotos não encontrada.")

    print("Pessoa removida com sucesso!")