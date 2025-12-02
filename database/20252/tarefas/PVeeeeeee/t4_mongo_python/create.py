from datetime import datetime
from bson.objectid import ObjectId
from conexao import col_atividades
import read 

def criar_atividade():
    print("\n[Nova Atividade]")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    status = input("Status (Pendente/Em andamento/Concluído): ")
    
    read.listar_usuarios()
    id_user_str = input("Copie e cole o ID do usuário responsável acima: ")
    
    try:
        nova = {
            "titulo": titulo,
            "descricao": descricao,
            "status": status,
            "id_usuario": ObjectId(id_user_str),
            "data": datetime.now()
        }
        col_atividades.insert_one(nova)
        print("Atividade cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir: {e}")