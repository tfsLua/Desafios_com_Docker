# Desafio 5: Microsserviços com API Gateway

## 🎯 Objetivo
Criar uma arquitetura com API Gateway centralizando o acesso a dois microsserviços.

## 💡 Solução, Arquitetura e Decisões Técnicas
*   **Microsserviços:**
    *   `service_1` (Usuários): Fornece dados de usuários em `/users`.
    *   `service_2` (Pedidos): Fornece dados de pedidos em `/orders`.
*   **API Gateway:** Utilizei o **Nginx** como API Gateway. Ele é o único ponto de entrada exposto externamente.
*   **Roteamento:** O arquivo `nginx.conf` foi configurado para:
    *   Encaminhar requisições para `/users` para o `service_1`.
    *   Encaminhar requisições para `/orders` para o `service_2`.
*   **Orquestração:** O `docker-compose.yml` garante que todos os três serviços sejam iniciados e estejam na mesma rede.

## ⚙️ Funcionamento Detalhado
1.  **Inicialização:** O `docker-compose` sobe os três containers.
2.  **Gateway:** O container `gateway` (Nginx) é iniciado e escuta na porta 80 (mapeada para a porta 80 do host).
3.  **Requisição Externa:** Quando uma requisição chega ao host na porta 80 (ex: `http://localhost/users`), o Nginx a intercepta.
4.  **Proxy Pass:** O Nginx, usando a diretiva `proxy_pass`, roteia a requisição internamente para o endereço do microsserviço correspondente (ex: `http://service_1:5001/users`).
5.  **Isolamento:** Os microsserviços `service_1` e `service_2` não têm suas portas expostas diretamente ao host, garantindo que o acesso seja feito apenas através do Gateway.

## 🚀 Instruções de Execução Passo a Passo

1.  **Navegue até a pasta do desafio:**
    ```bash
    cd desafio5
    ```
2.  **Suba os containers:**
    ```bash
    docker-compose up --build
    ```
3.  **Teste o endpoint de Usuários (via Gateway):**
    *   Acesse o endpoint no seu navegador ou via `curl`:
        ```bash
        curl http://localhost/users
        ```
    *   A resposta deve ser o JSON de usuários fornecido pelo `service_1`.

**Prova de Comunicação (Saída Esperada para `/users`):**

```json
[
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
```
4.  **Teste o endpoint de Pedidos (via Gateway):**
    *   Acesse o endpoint no seu navegador ou via `curl`:
        ```bash
        curl http://localhost/orders
        ```
    *   A resposta deve ser o JSON de pedidos fornecido pelo `service_2`.

**Prova de Comunicação (Saída Esperada para `/orders`):**

```json
[
    {"id": 101, "user_id": 1, "product": "Laptop"},
    {"id": 102, "user_id": 2, "product": "Mouse"}
]
```
5.  **Para parar e remover os containers:**
    ```bash
    docker-compose down
    ```
