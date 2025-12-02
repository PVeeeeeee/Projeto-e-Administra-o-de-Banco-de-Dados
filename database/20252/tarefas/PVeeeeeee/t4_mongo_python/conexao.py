import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tarefa_t4_db"]

col_usuarios = db["usuarios"]
col_atividades = db["atividades"]

def garantir_usuarios_teste():
    if col_usuarios.count_documents({}) == 0:
        col_usuarios.insert_one({"nome": "Carlos Lima", "cargo": "Analista"})
        col_usuarios.insert_one({"nome": "Ana Pereira", "cargo": "Coordenadora"})
        print(">> Usuários de teste criados.")