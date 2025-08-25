#  Observability Python + Prometheus + Grafana

Este repositório demonstra um exemplo de observabilidade usando Python e uma stack de ferramentas de observabilidade comumente utilizada por SRE/Devops via Docker Compose.

##  Como rodar

1. Clone este repositório ou baixe o zip.
2. Suba os containers:
   ```bash
   docker-compose up -d --build
   ```

3. Acesse os serviços:
   - Python App (métricas): [http://localhost:8000/metrics](http://localhost:8000/metrics)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - Grafana: [http://localhost:3000](http://localhost:3000)

   > Usuário padrão Grafana: `admin`  
   > Senha padrão Grafana: `admin`

4. Configure o Grafana:
   - Vá em **Connections → Data sources → Add data source**
   - Escolha **Prometheus**
   - Configure a URL: `http://prometheus:9090`

