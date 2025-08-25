# Usa uma imagem Python leve e estável baseada em Bullseye
FROM python:3.9-slim-bullseye

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala as dependências de sistema necessárias para o Playwright
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libexpat1 \
    libxcb1 \
    libxcomposite1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libcairo2 \
    libpango-1.0-0 \
    libasound2 \
    libxkbcommon0 \
    libx11-xcb1 \
    --no-install-recommends

# Copia e instala as dependências do Python
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Instala apenas o navegador Chromium
RUN playwright install chromium

# Copia todo o código da aplicação
COPY . .

# Expõe a porta que a aplicação vai usar
EXPOSE 8000

# Comando para rodar a aplicação quando o contêiner iniciar
CMD ["python", "main.py"]