from bson.objectid import ObjectId
from conexao import col_atividades
import read

def atualizar_atividade():
    read.ler_atividades()
    
    id_atv = input("\nDigite o ID da atividade para atualizar: ")
    novo_status = input("Novo Status: ")
    
    try:
        resultado = col_atividades.update_one(
            {"_id": ObjectId(id_atv)},
            {"$set": {"status": novo_status}}
        )
        if resultado.modified_count > 0:
            print("Status atualizado!")
        else:
            print("Nenhuma alteração feita (ID incorreto ou status igual).")
    except:
        print("ID inválido.")