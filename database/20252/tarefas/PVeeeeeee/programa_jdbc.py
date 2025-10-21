import psycopg2
from psycopg2 import sql 

DB_CONFIG = {
    "host": "host.docker.internal",
    "port": 5432,
    "dbname": "AtividadesBD",
    "user": "postgres",
    "password": "1234"
}

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def setup_initial_data():
    """Garante que os dados de base (funcionários e projeto 1) existam."""
    print("[Setup] Verificando dados iniciais...")
    
    sql_funcionarios = """
    INSERT INTO funcionario (codigo, nome, sexo, dt_nasc, salario) VALUES
    (1, 'João Silva', 'M', '1980-01-15', 5000),
    (2, 'Maria Souza', 'F', '1990-05-20', 6000),
    (3, 'Carlos Lima', 'M', '1985-11-02', 5500)
    ON CONFLICT (codigo) DO NOTHING;
    """
    
    sql_projeto = """
    INSERT INTO projeto (codigo, nome, descricao, responsavel, data_inicio) VALUES
    (1, 'Projeto Alfa', 'Desenvolvimento do novo sistema X', 1, '2025-01-01')
    ON CONFLICT (codigo) DO NOTHING;
    """
    
    conn = None
    try:
        conn = get_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_funcionarios)
                cursor.execute(sql_projeto)
                conn.commit()
                print("[Setup] Dados iniciais garantidos.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"[Setup] Erro ao inserir dados iniciais: {error}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def inserir_atividade(codigo_projeto, descricao):
    """a. Inserir uma atividade em algum projeto"""
    sql = "INSERT INTO atividade (descricao, projeto) VALUES (%s, %s)"
    conn = None
    try:
        conn = get_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (descricao, codigo_projeto))
                conn.commit()
                print(f"[JDBC] Atividade '{descricao}' inserida no projeto {codigo_projeto}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"[JDBC] Erro ao inserir atividade: {error}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def atualizar_lider_projeto(codigo_projeto, codigo_novo_responsavel):
    """b. Atualizar o líder de algum projeto"""
    sql = "UPDATE projeto SET responsavel = %s WHERE codigo = %s"
    conn = None
    try:
        conn = get_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (codigo_novo_responsavel, codigo_projeto))
                # Verificar se alguma linha foi realmente atualizada
                if cursor.rowcount == 0:
                    print(f"[JDBC] Nenhum projeto encontrado com codigo={codigo_projeto} para atualizar.")
                else:
                    conn.commit()
                    print(f"[JDBC] Responsável do projeto {codigo_projeto} atualizado para {codigo_novo_responsavel}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"[JDBC] Erro ao atualizar líder: {error}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def listar_projetos_atividades():
    """c. Listar todos os projetos e suas atividades"""
    sql = """
    SELECT p.nome AS projeto_nome, a.descricao AS atividade_descricao
    FROM projeto p
    LEFT JOIN atividade a ON p.codigo = a.projeto
    ORDER BY p.nome, a.descricao
    """
    conn = None
    try:
        conn = get_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                resultados = cursor.fetchall()
                
                if not resultados:
                    print("[JDBC] Nenhum projeto ou atividade encontrado.")
                    return

                print("\n--- [JDBC] Lista de Projetos e Atividades ---")
                projeto_atual = ""
                for row in resultados:
                    if row[0] != projeto_atual:
                        print(f"\nPROJETO: {row[0]}")
                        projeto_atual = row[0]
                    
                    atividade = row[1] if row[1] else " (Nenhuma atividade)"
                    print(f"  - Atividade: {atividade}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"[JDBC] Erro ao listar projetos: {error}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    
    setup_initial_data()
    
    print("\n--- Executando Passo 5 (JDBC/Driver) ---")
    
    inserir_atividade(codigo_projeto=1, descricao="Analisar requisitos (JDBC)")
    
    atualizar_lider_projeto(codigo_projeto=1, codigo_novo_responsavel=2) 
    
    listar_projetos_atividades()