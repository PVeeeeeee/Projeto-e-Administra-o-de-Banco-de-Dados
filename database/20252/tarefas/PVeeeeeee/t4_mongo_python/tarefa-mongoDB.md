# T4 - Sistema de Gestão de Atividades (MongoDB)

Este projeto implementa um sistema de CRUD (Create, Read, Update, Delete) para gestão de atividades utilizando **Python** e **MongoDB**.

O código foi refatorado para seguir uma **estrutura modular**, separando as responsabilidades de conexão e operações de banco de dados em arquivos distintos, controlados por um menu principal.

## 🛠 Pré-requisitos

* **Python 3.x** instalado.
* **MongoDB** rodando localmente na porta padrão (`27017`).
* Biblioteca **PyMongo**.

## 🚀 Instalação e Execução

Para rodar o projeto, é necessário navegar até o diretório específico da tarefa dentro do repositório.

1.  **Navegue até a pasta do projeto:**
    ```bash
    cd database/20252/tarefas/PVeeeeeee/t4_mongo_python
    ```

2.  **Instale a dependência do driver:**
    ```bash
    pip install pymongo
    ```

3.  **Execute o sistema:**
    ```bash
    python main.py
    ```

## 📊 Funcionalidades e Consultas

O sistema oferece um menu interativo no terminal com as seguintes opções:

1.  **Criar Atividade**: Vincula uma tarefa a um usuário existente.
2.  **Listar Atividades**: Mostra todas as tarefas cadastradas.
3.  **Atualizar Status**: Altera o estado da tarefa (ex: Pendente -> Concluído).
4.  **Deletar Atividade**: Remove um registro pelo ID.
5.  **Consultas Complexas**:
    * **Join ($lookup)**: Cruza dados das coleções `atividades` e `usuarios` para exibir o nome do responsável.
    * **Agrupamento ($group)**: Conta quantas atividades existem por tipo de status.