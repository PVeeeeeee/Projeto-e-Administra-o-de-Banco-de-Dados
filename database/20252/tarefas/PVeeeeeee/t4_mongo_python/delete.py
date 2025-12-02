from bson.objectid import ObjectId
from conexao import col_atividades
import read

def deletar_atividade():
    read.ler_atividades()
    id_atv = input("\nDigite o ID da atividade para remover: ")
    
    try:
        res = col_atividades.delete_one({"_id": ObjectId(id_atv)})
        if res.deleted_count > 0:
            print("Atividade removida.")
        else:
            print("Atividade não encontrada.")
    except:
        print("ID inválido.")