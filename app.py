from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Caminho do chromedriver.exe
caminho_driver = "chromedriver.exe"
servico = Service(executable_path=caminho_driver)

numeros = [
    # Adicione os números aqui, com o seguinte formato (exemplo):
    # "+5511987654321"
    "+5511974808650"
]

# Mensagem a ser enviada
mensagem = "Estou testando rodar um script Python para mandar mensagens pelo WhatsApp. Se você recebeu, deu certo"

# Inicia o navegador com o Service
driver = webdriver.Chrome(service=servico)
driver.get("https://web.whatsapp.com")

# Espera você escanear o QR Code
input("Após escanear o QR Code, pressione Enter para continuar...")

# Envia para cada número
for numero in numeros:
    print(f"Enviando para {numero}...")
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    driver.get(url)
    
    time.sleep(8)  # Espera a página carregar
    
    try:
        campo = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-tab='10']"))
        )
        campo.send_keys(Keys.ENTER)
        botao_enviar = WebDriverWait(driver, 5).until( # Caso não envie sozinho
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        botao_enviar.click()
        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")
        
print("Mensagens enviadas.")
driver.quit()