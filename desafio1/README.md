# Desafio 1: Containers em Rede

## 🎯 Objetivo
Criar dois containers que se comunicam por uma rede Docker customizada.

## 💡 Solução, Arquitetura e Decisões Técnicas
*   **Servidor (`server`):** Implementado com **Flask em Python**, rodando na porta 8080. O endpoint `/` retorna uma mensagem de "Hello" com o timestamp atual.
*   **Cliente (`client`):** Utiliza a imagem **`alpine/curl`** para executar um script em loop que faz requisições HTTP para o servidor a cada 5 segundos.
*   **Rede:** Foi configurada uma rede Docker customizada chamada `desafio1_network` no `docker-compose.yml`. Esta rede garante que os containers possam se comunicar usando seus nomes de serviço (`server` e `client`) como hostname.
*   **Decisão Técnica:** O uso de uma rede customizada é crucial para o isolamento e para a resolução de nomes interna, que é a forma recomendada de comunicação entre serviços no Docker Compose.

## ⚙️ Funcionamento Detalhado
1.  **Rede:** O `docker-compose.yml` define a rede `desafio1_network`.
2.  **Servidor:** O container `server` é construído a partir do `Dockerfile` em `./server`, instala o Flask e executa `app.py`, ficando acessível internamente pelo nome `server:8080`.
3.  **Cliente:** O container `client` é construído a partir do `Dockerfile` em `./client` e executa o comando `curl -s http://server:8080` em um loop infinito, provando a comunicação.
4.  **Comunicação:** A comunicação é comprovada pelos logs do container `client`, que exibem a resposta do servidor a cada requisição.

## 🚀 Instruções de Execução Passo a Passo

1.  **Navegue até a pasta do desafio:**
    ```bash
    cd desafio1
    ```
2.  **Construa as imagens e suba os containers:**
    ```bash
    docker-compose up --build -d
    ```
3.  **Verifique a comunicação (Logs do Cliente):**
    *   Observe os logs do container `desafio1_client` para ver as requisições sendo enviadas e as respostas do servidor.
    ```bash
    docker logs desafio1_client -f
    ```
    **Exemplo de Saída (Prova de Comunicação):**
    ```
    desafio1_client | Hello from Server! Current time: 2025-11-19 14:30:01
    desafio1_client | Hello from Server! Current time: 2025-11-19 14:30:06
    desafio1_client | Hello from Server! Current time: 2025-11-19 14:30:11
    ```
4.  **Para parar e remover os containers:**
    ```bash
    docker-compose down
    ```
