# T4 - Sistema de Gestão de Atividades (Python + MongoDB)

Este projeto consiste na implementação da Tarefa 4. O objetivo é desenvolver um sistema de persistência de dados utilizando **Python** e **MongoDB**, contemplando operações CRUD completas e consultas complexas (Agregação).

O código foi refatorado para uma **arquitetura modular**, separando a conexão, as operações de CRUD e o menu principal em arquivos distintos para melhor organização e manutenção.

## 🛠 Pré-requisitos

* Python 3.x
* MongoDB (Serviço rodando na porta `27017`)
* Driver PyMongo

## 🚀 Como Executar

Para rodar o projeto corretamente, é necessário navegar até o diretório específico da tarefa no repositório:

1.  **Navegue até a pasta do projeto:**
    ```bash
    cd database/20252/tarefas/PVeeeeeee/t4_mongo_python
    ```

2.  **Instale as dependências:**
    ```bash
    pip install pymongo
    ```

3.  **Execute o sistema:**
    ```bash
    python main.py
    ```

## 📊 Funcionalidades Implementadas

O sistema atende a todos os requisitos da tarefa:

1.  **CRUD Completo**:
    * **Create**: Permite criar atividades vinculadas a usuários existentes.
    * **Read**: Listagem de todas as atividades com status.
    * **Update**: Alteração de status da atividade via ID.
    * **Delete**: Remoção física do registro via ID.

2.  **Consultas Complexas (MongoDB Aggregations)**:
    * **Consulta com JOIN (`$lookup`)**: Cruza a coleção de `atividades` com `usuarios` para exibir o nome do responsável pela tarefa.
    * **Consulta com GROUP BY (`$group`)**: Agrupa as atividades pelo status e retorna a contagem total de cada categoria.

## 📝 Evidência de Execução (Log de Saída)

Abaixo, um exemplo de interação com o sistema demonstrando o funcionamento:

```text
>> Conectado ao MongoDB.
>> Usuários de teste verificados/criados.

=== GESTÃO DE ATIVIDADES (MODULAR) ===
1. Criar Atividade
2. Listar Atividades
3. Atualizar Status
4. Deletar Atividade
5. Consultas Complexas
0. Sair
Opção: 2

--- Lista de Atividades ---
ID: 674b... | Título: Implementar Login (Em andamento)
ID: 674b... | Título: Documentar API (Pendente)

=== GESTÃO DE ATIVIDADES (MODULAR) ===
Opção: 5

--- Consultas Avançadas ---
1. Ver atividades com nome do responsável (Join)
2. Contagem de atividades por status (Group)
Escolha: 1

[Resultado Join]
Atividade: Implementar Login | Responsável: Carlos Lima
Atividade: Documentar API | Responsável: Ana Pereira

=== GESTÃO DE ATIVIDADES (MODULAR) ===
Opção: 5
Escolha: 2

[Resultado Group By]
Status 'Em andamento': 1
Status 'Pendente': 1