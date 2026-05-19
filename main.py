# ==============================
# main.py
# Sistema de Reconhecimento Facial
# ==============================

from cadastrar import cadastrarPessoa
from capturar import capturarFaces
from treinar import treinarModelo
from reconhecer import reconhecerFace


def menu():

    while True:

        print("\n==============================")
        print(" SISTEMA DE RECONHECIMENTO ")
        print("==============================")
        print("1 - Cadastrar Pessoa")
        print("2 - Capturar Faces")
        print("3 - Treinar Modelo")
        print("4 - Reconhecer Face")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        # ==========================
        # CADASTRAR
        # ==========================
        if opcao == "1":

            cadastrarPessoa()

        # ==========================
        # CAPTURAR
        # ==========================
        elif opcao == "2":

            capturarFaces()

        # ==========================
        # TREINAR
        # ==========================
        elif opcao == "3":

            treinarModelo()

        # ==========================
        # RECONHECER
        # ==========================
        elif opcao == "4":

            reconhecerFace()

        # ==========================
        # SAIR
        # ==========================
        elif opcao == "0":

            print("Encerrando sistema...")
            break

        else:

            print("Opção inválida!")


# ==============================
# INICIAR SISTEMA
# ==============================
menu()