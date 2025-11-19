# Desafio 2: Volumes e Persistência

## 🎯 Objetivo
Demonstrar persistência de dados usando volumes Docker.

## 💡 Solução, Arquitetura e Decisões Técnicas
*   **Banco de Dados:** Utilizei a imagem oficial do **`postgres:13-alpine`** para simular um serviço que armazena dados.
*   **Volume:** Foi configurado um **volume nomeado** chamado `postgres_data` para mapear o diretório de dados do container (`/var/lib/postgresql/data`) para o host Docker.
*   **Persistência:** O uso do volume nomeado garante que os dados do banco de dados permaneçam no host, mesmo que o container seja removido e recriado.

## ⚙️ Funcionamento Detalhado
1.  **Criação do Volume:** O `docker-compose.yml` define o volume `postgres_data`. Na primeira execução, o Docker o cria no host.
2.  **Inicialização do DB:** O container do PostgreSQL é iniciado e armazena seus dados no ponto de montagem do volume.
3.  **Teste de Persistência:** Para provar a persistência, é necessário:
    *   **Passo 1:** Iniciar o container e inserir alguns dados de teste (ex: criar uma tabela e inserir uma linha).
    *   **Passo 2:** Parar e remover o container (`docker-compose down`).
    *   **Passo 3:** Iniciar o container novamente (`docker-compose up`).
    *   **Passo 4:** Conectar-se ao novo container e verificar se os dados inseridos no Passo 1 ainda estão presentes.

## 🚀 Instruções de Execução Passo a Passo

1.  **Navegue até a pasta do desafio:**
    ```bash
    cd desafio2
    ```
2.  **Suba o container (Passo 1):**
    ```bash
    docker-compose up -d
    ```
3.  **Insira dados de teste (Passo 1 - Exemplo):**
    *   Acesse o shell do container:
        ```bash
        docker exec -it desafio2_postgres psql -U user -d persisted_db
        ```
    *   Crie uma tabela e insira um dado:
        ```sql
        CREATE TABLE teste (id INT, nome VARCHAR(50));
        INSERT INTO teste (id, nome) VALUES (1, 'Dado Persistente');
        \q
        ```
4.  **Remova o container (Passo 2):**
    ```bash
    docker-compose down
    ```
5.  **Suba o container novamente (Passo 3):**
    ```bash
    docker-compose up -d
    ```
6.  **Verifique a persistência (Passo 4):**
    *   Acesse o shell do novo container:
        ```bash
        docker exec -it desafio2_postgres psql -U user -d persisted_db
        ```
    *   Verifique se a tabela e o dado ainda existem:
        ```sql
        SELECT * FROM teste;
        \q
        ```
    *   ****Prova de Persistência (Saída Esperada):**

Ao executar `SELECT * FROM teste;` no Passo 6, a saída esperada é:

```
 id |       nome
----+------------------
  1 | Dado Persistente
(1 row)
```

Isso comprova que os dados inseridos no Passo 3 persistiram após a remoção e recriação do container no Passo 4 e 5, graças ao volume nomeado `postgres_data`.**
