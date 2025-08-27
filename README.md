#  Observability Stack

Este repositório exemplifica como eu faria a observabilidade usando Python e uma stack de ferramentas de observabilidade comumente utilizadas por SRE/Devops via Docker Compose a fim de demonstrar meu conhecimento.

##  Como rodar

1. Clone este repositório ou baixe o zip.
2. Suba os containers:
   ```bash
   docker-compose up -d --build
   ```

3. Acesse os serviços:
   - Python App (métricas): (http://localhost:8000/metrics)
   - Prometheus: (http://localhost:9090)
   - Grafana: (http://localhost:3000)
   - Loki: (http://localhost:3100)

   > Usuário padrão Grafana: `admin`  
   > Senha padrão Grafana: `admin`

4. Configure o Grafana:
   - Vá em **Connections → Data sources → Add data source**
   - Escolha **Prometheus**
   - Configure a URL: `http://prometheus:9090`

