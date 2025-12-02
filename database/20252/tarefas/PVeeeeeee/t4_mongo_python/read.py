from conexao import col_atividades, col_usuarios

def listar_usuarios():
    """Lista usuários para auxiliar no cadastro"""
    print("\n--- Usuários Disponíveis ---")
    for u in col_usuarios.find():
        print(f"ID: {u['_id']} | Nome: {u['nome']}")
    print("----------------------------")

def ler_atividades():
    """R: Read - Lista todas as atividades"""
    print("\n--- Lista de Atividades ---")
    atividades = list(col_atividades.find())
    if not atividades:
        print("Nenhuma atividade encontrada.")
    for item in atividades:
        print(f"ID: {item['_id']} | Título: {item['titulo']} ({item['status']})")

def consultas_complexas():
    print("\n--- Consultas Avançadas ---")
    print("1. Ver atividades com nome do responsável (Join)")
    print("2. Contagem de atividades por status (Group)")
    op = input("Escolha: ")

    if op == "1":
        pipeline = [
            {"$lookup": {
                "from": "usuarios",
                "localField": "id_usuario",
                "foreignField": "_id",
                "as": "usuario_info"
            }},
            {"$unwind": "$usuario_info"},
            {"$project": {
                "titulo": 1,
                "status": 1,
                "responsavel": "$usuario_info.nome"
            }}
        ]
        resultados = list(col_atividades.aggregate(pipeline))
        for r in resultados:
            print(f"Atividade: {r['titulo']} | Responsável: {r['responsavel']}")
            
    elif op == "2":
        pipeline = [
            {"$group": {
                "_id": "$status",
                "qtd": {"$sum": 1}
            }},
            {"$sort": {"qtd": -1}}
        ]
        resultados = list(col_atividades.aggregate(pipeline))
        for r in resultados:
            print(f"Status '{r['_id']}': {r['qtd']}")