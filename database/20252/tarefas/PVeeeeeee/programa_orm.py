from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from datetime import date

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/AtividadesBD"

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(150))
    sexo = Column(String(1))
    dt_nasc = Column(Date)
    salario = Column(Integer)

class Projeto(Base):
    __tablename__ = 'projeto'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(250))
    responsavel = Column(Integer, ForeignKey('funcionario.codigo'))
    data_inicio = Column(Date)
    
    atividades = relationship("Atividade", back_populates="projeto_ref")

class Atividade(Base):
    __tablename__ = 'atividade'
    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(250))
    projeto = Column(Integer, ForeignKey('projeto.codigo'))
    
    projeto_ref = relationship("Projeto", back_populates="atividades")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    return SessionLocal()

def setup_initial_data_orm():
    """Garante que os dados de base (funcionários e projeto 1) existam."""
    print("[Setup ORM] Verificando dados iniciais...")
    session = get_session()
    try:
        func1 = session.query(Funcionario).get(1)
        if not func1:
            session.add_all([
                Funcionario(codigo=1, nome='João Silva', sexo='M', dt_nasc=date(1980, 1, 15), salario=5000),
                Funcionario(codigo=2, nome='Maria Souza', sexo='F', dt_nasc=date(1990, 5, 20), salario=6000),
                Funcionario(codigo=3, nome='Carlos Lima', sexo='M', dt_nasc=date(1985, 11, 2), salario=5500)
            ])

        proj1 = session.query(Projeto).get(1)
        if not proj1:
            session.add(
                Projeto(codigo=1, nome='Projeto Alfa', descricao='Desenvolvimento do novo sistema X', responsavel=1, data_inicio=date(2025, 1, 1))
            )
        
        session.commit()
        print("[Setup ORM] Dados iniciais garantidos.")
    except SQLAlchemyError as e:
        print(f"[Setup ORM] Erro ao inserir dados iniciais: {e}")
        session.rollback()
    finally:
        session.close()

def inserir_atividade_orm(codigo_projeto, descricao):
    """a. Inserir uma atividade em algum projeto"""
    session = get_session()
    try:
        projeto_db = session.query(Projeto).get(codigo_projeto)
        if not projeto_db:
            print(f"[ORM] Projeto com codigo={codigo_projeto} não encontrado.")
            return

        nova_atividade = Atividade(descricao=descricao, projeto=codigo_projeto)
        session.add(nova_atividade)
        session.commit()
        print(f"[ORM] Atividade '{descricao}' inserida no projeto '{projeto_db.nome}'.")

    except SQLAlchemyError as e:
        print(f"[ORM] Erro ao inserir atividade: {e}")
        session.rollback()
    finally:
        session.close()

def atualizar_lider_projeto_orm(codigo_projeto, codigo_novo_responsavel):
    """b. Atualizar o líder de algum projeto"""
    session = get_session()
    try:
        projeto_db = session.query(Projeto).get(codigo_projeto)
        
        if projeto_db:
            projeto_db.responsavel = codigo_novo_responsavel
            session.commit()
            print(f"[ORM] Responsável do projeto '{projeto_db.nome}' atualizado para {codigo_novo_responsavel}.")
        else:
            print(f"[ORM] Projeto com codigo={codigo_projeto} não encontrado.")
    
    except SQLAlchemyError as e:
        print(f"[ORM] Erro ao atualizar líder: {e}")
        session.rollback()
    finally:
        session.close()

def listar_projetos_atividades_orm():
    """c. Listar todos os projetos e suas atividades"""
    session = get_session()
    try:
        projetos = session.query(Projeto).options(joinedload(Projeto.atividades)).all()
        
        if not projetos:
            print("[ORM] Nenhum projeto encontrado.")
            return

        print("\n--- [ORM] Lista de Projetos e Atividades ---")
        for projeto in projetos:
            print(f"\nPROJETO: {projeto.nome} (Responsável ID: {projeto.responsavel})")
            if not projeto.atividades:
                print("  - (Nenhuma atividade)")
            else:
                for atividade in projeto.atividades:
                    print(f"  - Atividade: {atividade.descricao}")
                        
    except SQLAlchemyError as e:
        print(f"[ORM] Erro ao listar projetos: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    
    setup_initial_data_orm()
    
    print("\n--- Executando Passo 6 (ORM) ---")
    
    inserir_atividade_orm(codigo_projeto=1, descricao="Definir escopo (ORM)")
    
    atualizar_lider_projeto_orm(codigo_projeto=1, codigo_novo_responsavel=3)
    
    listar_projetos_atividades_orm()