# Tarefa - ODBC e ORM

Esta tarefa documenta a configuração de um banco de dados PostgreSQL e a criação de scripts Python para acessá-lo usando um driver direto (psycopg2) e um framework ORM (SQLAlchemy).

## Links para os Scripts e Programas Criados

* [Script DDL: Esquema Relacional AtividadesBD (Fonte)](https://github.com/tacianosilva/bsi-tasks/tree/master/database/scripts/AtividadesBD/postgres)
* [Programa 1: Conexão Direta (psycopg2)](./programa_jdbc.py)
* [Programa 2: Conexão com ORM (SQLAlchemy)](./programa_orm.py)

---

## Resumo sobre ODBC (Driver `psycopg2` em Python)

Para esta tarefa, a linguagem escolhida foi Python. Em vez de usar um driver ODBC genérico, utilizei o `psycopg2`, que é o driver de banco de dados PostgreSQL mais popular para Python. Ele implementa a especificação Python DB-API 2.0, que funciona de forma análoga ao JDBC para Java ou ao ODBC para outras linguagens.

**Psycopg2 (Driver/Pacote):**

* **Conexão:** O `psycopg2` permite estabelecer uma conexão direta com o banco de dados PostgreSQL fornecendo parâmetros como host, porta, nome do banco, usuário e senha.
* **Cursor:** Uma vez conectado, criamos um objeto "cursor". É através dele que os comandos SQL são executados.
* **Execução de SQL Bruto:** A principal característica é que escrevemos o SQL manualmente. Usamos métodos do cursor, como `cursor.execute()`, para enviar os comandos `INSERT`, `UPDATE`, `SELECT`, etc., diretamente ao banco.
* **Controle de Transação:** O controle da transação é manual. É necessário chamar `connection.commit()` para salvar permanentemente as alterações ou `connection.rollback()` para descartá-las em caso de erro.

---

## Resumo sobre ORM (SQLAlchemy em Python)

**ORM (Object-Relational Mapping / Mapeamento Objeto-Relacional)** é uma técnica de programação que converte dados entre o sistema de tipos de uma linguagem orientada a objetos (como classes Python) e o modelo de um banco de dados relacional (tabelas e colunas). O objetivo é permitir que o desenvolvedor manipule o banco de dados usando apenas os conceitos da sua linguagem (objetos, atributos, métodos), sem precisar escrever comandos SQL manualmente.

**Framework Utilizado: SQLAlchemy**

O `SQLAlchemy` é o framework ORM mais popular e robusto do ecossistema Python. Ele fornece um conjunto completo de ferramentas para "mapear" classes Python para tabelas do banco de dados.

**Principais Características do SQLAlchemy:**

* **Mapeamento Declarativo:** Criamos classes em Python que herdam de uma `Base` declarativa. O SQLAlchemy entende que cada classe representa uma tabela e que os atributos da classe (definidos com `Column`) representam as colunas.
* **Sessão (Session):** Em vez de um "cursor", o ORM usa uma "Sessão". A Sessão é uma área de trabalho que gerencia o estado dos objetos e a comunicação com o banco. Ela rastreia quais objetos foram alterados, adicionados ou excluídos.
* **Manipulação de Objetos:**
    * Para **inserir** dados, criamos uma instância da classe (ex: `nova_atividade = Atividade(descricao="...")`) e a adicionamos à sessão (`session.add(nova_atividade)`).
    * Para **atualizar**, simplesmente modificamos o atributo do objeto (ex: `projeto.responsavel = 3`).
    * Para **consultar**, usamos métodos da sessão (ex: `session.query(Projeto).get(1)`).
* **Tradução Automática:** Ao chamar `session.commit()`, o SQLAlchemy analisa todas as alterações pendentes na sessão e gera automaticamente os comandos SQL (INSERT, UPDATE, DELETE) otimizados para enviar ao banco de dados, tudo dentro de uma única transação.