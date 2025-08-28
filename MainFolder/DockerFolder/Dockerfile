FROM python:3.9-slim

WORKDIR /app

# Copiar os arquivos necessários
COPY ../Backend/requirements.txt .
COPY ../Backend/app.py .
COPY ../Backend/templates ./templates

# Criar pasta uploads
RUN mkdir uploads

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que o Flask usa
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]