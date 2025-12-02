import conexao
import create
import read
import update
import delete

def menu():
    conexao.garantir_usuarios_teste()
    
    while True:
        print("\n=== GESTÃO DE ATIVIDADES (MODULAR) ===")
        print("1. Criar Atividade")
        print("2. Listar Atividades")
        print("3. Atualizar Status")
        print("4. Deletar Atividade")
        print("5. Consultas Complexas")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            create.criar_atividade()
        elif opcao == "2":
            read.ler_atividades()
        elif opcao == "3":
            update.atualizar_atividade()
        elif opcao == "4":
            delete.deletar_atividade()
        elif opcao == "5":
            read.consultas_complexas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()