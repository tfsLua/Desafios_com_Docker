# Desafio 3: Docker Compose Orquestrando Serviços

## 🎯 Objetivo
Usar Docker Compose para orquestrar múltiplos serviços dependentes (web, db, cache).

## 💡 Solução, Arquitetura e Decisões Técnicas
*   **Serviços:** A solução orquestra três serviços: `web` (Nginx), `db` (PostgreSQL) e `cache` (Redis).
*   **Orquestração:** O `docker-compose.yml` define os três serviços, suas imagens, variáveis de ambiente e volumes.
*   **Dependência:** O serviço `web` utiliza a diretiva `depends_on` para garantir que `db` e `cache` sejam iniciados antes dele.
*   **Comunicação:** Todos os serviços estão na mesma rede padrão do Compose, permitindo que o serviço `web` se comunique com `db` e `cache` usando seus nomes de serviço como hostname.

## ⚙️ Funcionamento Detalhado
1.  **Inicialização:** Ao executar o `docker-compose up`, o Compose lê o arquivo de configuração.
2.  **Ordem de Início:** Devido ao `depends_on`, o PostgreSQL (`db`) e o Redis (`cache`) são iniciados primeiro.
3.  **Serviço Web:** O Nginx (`web`) é iniciado por último. Embora o Nginx em si não se conecte diretamente, em uma aplicação real, ele usaria as variáveis de ambiente `DB_HOST` e `CACHE_HOST` (definidas no `docker-compose.yml`) para se conectar aos serviços internos.
4.  **Rede:** A rede interna padrão permite que os serviços se encontrem.

## 🚀 Instruções de Execução Passo a Passo

1.  **Navegue até a pasta do desafio:**
    ```bash
    cd desafio3
    ```
2.  **Suba todos os serviços:**
    ```bash
    docker-compose up -d
    ```
3.  **Verifique o status dos containers:**
    ```bash
    docker-compose ps
    ```
    *   Verifique se os três containers (`desafio3_web`, `desafio3_db`, `desafio3_cache`) estão no estado `Up`.
4.  **Teste a comunicação (Exemplo):**
    *   Acesse o shell do container `web`:
        ```bash
        docker exec -it desafio3_web sh
        ```
    *   Tente pingar o banco de dados e o cache (prova de que a rede interna funciona):

**Prova de Comunicação (Saída Esperada do `ping db`):**

```bash
/ # ping db
PING db (172.20.0.2): 56 data bytes
64 bytes from 172.20.0.2: seq=0 ttl=64 time=0.088 ms
64 bytes from 172.20.0.2: seq=1 ttl=64 time=0.081 ms
^C
--- db ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.081/0.084/0.088 ms
```

O sucesso do `ping` comprova que o serviço `web` consegue resolver o nome `db` e se comunicar com ele na rede interna do Docker Compose.
        ```bash
        ping db
        ping cache
        exit
        ```
5.  **Para parar e remover os containers:**
    ```bash
    docker-compose down
    ```
