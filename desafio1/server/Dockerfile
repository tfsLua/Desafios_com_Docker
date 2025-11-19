# Dockerfile para o Servidor Web (Flask)
FROM python:3.9-slim

WORKDIR /app

# Instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app.py .

# Expõe a porta 8080
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]
