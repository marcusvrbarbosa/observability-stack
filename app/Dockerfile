# Usa uma imagem Python leve e estável baseada em Bullseye
FROM python:3.9-slim-bullseye

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala as dependências de sistema necessárias para o Playwright rodar Chromium
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
    libpangocairo-1.0-0 \
    libasound2 \
    libxkbcommon0 \
    libx11-xcb1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libdrm2 \
    libatspi2.0-0 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências do Python
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

# Instala o navegador Chromium do Playwright junto com dependências
RUN playwright install --with-deps chromium

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
