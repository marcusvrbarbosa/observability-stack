from prometheus_client import Counter, Histogram, Gauge, start_http_server
from openpyxl import load_workbook
from playwright.sync_api import sync_playwright, expect
import time

# 📊 Métricas Prometheus
automation_runs = Counter("automation_runs_total", "Número de vezes que a automação foi executada")
automation_errors = Counter("automation_errors_total", "Número de erros na automação")
automation_duration = Histogram("automation_run_duration_seconds", "Duração da execução da automação")
app_uptime = Gauge("app_uptime_seconds", "Tempo em segundos que a aplicação está rodando")

start_time = time.time()

def run_automation():
    """Executa a automação e atualiza métricas Prometheus."""
    with automation_duration.time():  # mede tempo da execução
        try:
            automation_runs.inc()

            wb = load_workbook("contatos.xlsx")
            ws = wb.active

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(
                    base_url="https://docs.google.com/forms/d/17y-FzMD9pU5x2BxBikMlLMlkoRKBtlt7viNBoDY4PN4/preview"
                )
                
                # Carrega a página UMA VEZ antes do loop
                page.goto("https://docs.google.com/forms/d/17y-FzMD9pU5x2BxBikMlLMlkoRKBtlt7viNBoDY4PN4/preview")
                page.wait_for_selector('input[aria-label="Nome"]:not([aria-disabled="true"])')
                
                for j in range(1, ws.max_row + 1):
                    valores = [ws.cell(row=j, column=i).value for i in range(1, ws.max_column + 1)]
                    print(valores)

                    if j != 1:  # pula cabeçalho
                        ws.cell(j, 1).value = "okay"

                        # Use um seletor mais específico e force o preenchimento se necessário
                        page.get_by_label("Nome").fill(str(valores[1]), force=True)
                        page.get_by_label("E-mail").fill(str(valores[2]), force=True)
                        page.get_by_label("Endereço").fill(str(valores[3]), force=True)
                        page.get_by_label("Número de telefone").fill(str(valores[4]), force=True)
                        page.get_by_label("LinkedIn").fill(str(valores[5]), force=True)
                        page.screenshot(path=f"screenshot_{j}.png")
                        
                        # Submete o formulário e recarrega a página para a próxima linha
                        # Exemplo: page.click("text=Enviar")
                        page.goto("https://docs.google.com/forms/d/17y-FzMD9pU5x2BxBikMlLMlkoRKBtlt7viNBoDY4PN4/preview")
                        page.wait_for_selector('input[aria-label="Nome"]:not([aria-disabled="true"])')


            wb.save(filename="contatos.xlsx")

        except Exception as e:
            automation_errors.inc()
            print(f"❌ Erro na automação: {e}")


if __name__ == "__main__":
    # Servidor Prometheus
    start_http_server(8000)
    print("✅ Servidor de métricas rodando em http://localhost:8000/metrics")

    while True:
        run_automation()
        app_uptime.set(time.time() - start_time)
        time.sleep(10)  # intervalo entre execuções