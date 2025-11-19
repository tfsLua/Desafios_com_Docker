# Desafio 4: Microsserviços Independentes

## 🎯 Objetivo
Criar dois microsserviços independentes que se comunicam via HTTP.

## 💡 Solução, Arquitetura e Decisões Técnicas
*   **Microsserviço A (`service_a`):** Implementado em **Flask em Python**, expõe um endpoint `/users` que retorna uma lista de usuários em formato JSON.
*   **Microsserviço B (`service_b`):** Implementado em **Flask em Python**, consome o endpoint `/users` do Serviço A usando a biblioteca `requests` e processa a informação para um formato combinado.
*   **Isolamento:** Cada serviço possui seu próprio `Dockerfile` e é executado em um container isolado.
*   **Comunicação:** A comunicação é direta via HTTP, utilizando o nome de serviço (`service_a`) como hostname, resolvido automaticamente pelo Docker Compose.

## ⚙️ Funcionamento Detalhado
1.  **Serviço A:** Inicia na porta 5000 (interna) e aguarda requisições GET em `/users`.
2.  **Serviço B:** Inicia na porta 5001 (exposta externamente). Quando o endpoint `/combined_info` é acessado, ele faz uma requisição HTTP para `http://service_a:5000/users`.
3.  **Processamento:** O Serviço B recebe a lista de usuários, itera sobre ela e constrói uma nova resposta JSON com a informação combinada.
4.  **Docker Compose:** O `docker-compose.yml` orquestra a subida dos dois serviços e garante que eles estejam na mesma rede para que a comunicação interna funcione.

## 🚀 Instruções de Execução Passo a Passo

1.  **Navegue até a pasta do desafio:**
    ```bash
    cd desafio4
    ```
2.  **Suba os containers:**
    ```bash
    docker-compose up --build
    ```
3.  **Teste o Serviço A (Opcional - Apenas se a porta 5000 estivesse exposta):**
    *   Como a porta 5000 não está exposta, o teste deve ser feito via Serviço B.
4.  **Teste o Serviço B (Comunicação Combinada):**
    *   Acesse o endpoint do Serviço B no seu navegador ou via `curl`:
        ```bash
        curl http://localhost:5001/combined_info
        ```
    *   A resposta deve ser um JSON contendo a informação processada, provando que o Serviço B se comunicou com sucesso com o Serviço A.

**Prova de Comunicação (Saída Esperada):**

```json
{
  "data": [
    "Usuário Alice está active",
    "Usuário Bob está inactive",
    "Usuário Charlie está active"
  ],
  "status": "success"
}
```
5.  **Para parar e remover os containers:**
    ```bash
    docker-compose down
    ```
