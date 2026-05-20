# ==============================
# main.py
# Sistema de Reconhecimento Facial
# ==============================
import time

from cadastrar import cadastrarPessoa
from capturar import capturarFaces
from treinar import treinarModelo
from reconhecer import reconhecerFace
from apagar import  apagarPessoa
from listar import listarPessoas

def menuInterface():

    print("\n=====================================")
    print(" IdFace - SISTEMA DE RECONHECIMENTO ")
    print("=====================================")
    print("1 - Cadastrar Pessoa")
    print("2 - Capturar Faces")
    print("3 - Treinar Modelo")
    print("4 - Reconhecer Face")
    print("5 - Apagar Pessoa ")
    print("6 - Listar Pessoas")
    print("0 - Sair")
    print("==============================")

def menu():

    while True:
        # Exibe o menu
        menuInterface()

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
        # APAGAR
        # ==========================
        elif opcao == "5":
            apagarPessoa()
        # ==========================
        # LISTAR
        # ==========================
        elif opcao == "6":
            
            listarPessoas()
            time.sleep(2)  # Pausa para o usuário ler a lista
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