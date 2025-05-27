from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib.parse
import time
import random

# Caminho para o chromedriver
caminho_driver = "chromedriver.exe"
servico = Service(executable_path=caminho_driver)

# Lista de números para envio
numeros = [
    # "+5511987654321" Adicione neste formato
]

# Mensagem 
mensagem = """
Estou testando rodar um script Python para mandar mensagens pelo WhatsApp. Se você recebeu, deu certo.

Você recebeu?

Abraço!
"""

# Inicia o navegador
driver = webdriver.Chrome(service=servico)
driver.get("https://web.whatsapp.com")

# Aguardando o escaneamento do QR Code manualmente
input("Após escanear o QR Code, pressione Enter para continuar...")

# Loop para enviar a mensagem a cada número
for numero in numeros:
    print(f"Enviando para {numero}...")

    # Garante que a mensagem não percca a formatação
    mensagem_encoded = urllib.parse.quote(mensagem)
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_encoded}"
    driver.get(url)

    # Aguarda carregamento da conversa de forma aleatória
    time.sleep(random.uniform(6, 10))

    try:
        # Espera o campo da mensagem aparecer e foca nele
        campo_mensagem = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-tab='10']"))
        )
        campo_mensagem.click()
        time.sleep(1)

        # Tenta enviar com Enter
        campo_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)

        # Tenta clicar no botão de envio, caso o Enter não funcione
        try:
            botao_enviar = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
            )
            botao_enviar.click()
        except:
            pass  # Se não encontrar o botão, ignora

        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar para {numero}: {e}")

print("Todas as mensagens foram processadas.")
driver.quit()