from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def iniciar_robo():
    # Configura as opções do Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Substitua pelo caminho do Chrome no seu sistema

    # Inicializa o driver do Chrome
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    # Abre o Google
    driver.get('https://www.google.com')

    # Aguarde um tempo para visualizar a janela aberta
    try:
        caixa_de_texto = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"))
        )
        caixa_de_texto.click()
        time.sleep(2)
        caixa_de_texto.send_keys("Bem Vindo ao meu RPA,o robo já começou!!!")   
        time.sleep(4)
    except:
        pass

    driver.get('http://127.0.0.1:5502/index.html')
    time.sleep(1)
    campo_nome = driver.find_element(By.ID, "nome")
    campo_nome.click()
    time.sleep(1)
    campo_nome.send_keys("Maria Pereira da Fonseca")  
    campo_data = driver.find_element(By.ID, "data_nascimento") 
    campo_data.clear()
    time.sleep(1)
    data = "31-12-2023"  # Formato: YYYY-MM-DD
    time.sleep(1)
    campo_data.send_keys(data)

    # Aguarda um tempo para visualizar a data preenchida
    time.sleep(1)
    select_element = driver.find_element(By.ID, "genero")
    select = Select(select_element)
    option_text = "Feminino"  # Substitua pelo texto da opção desejada
    select.select_by_visible_text(option_text)
    time.sleep(1)
    endereco_comp = driver.find_element(By.ID, "endereco")
    endereco_comp.click()
    time.sleep(1)
    endereco_comp.send_keys("Elenco: Os Mariachis, Rubens, Will, Sergio Machado, Dione Dias, Mr. Kan, Marcus Teodoro Lopes, Paloma Albuquerque, Angélica Chosa, Alana Mendes, Patricia Oliveira")  
    time.sleep(1)

    # Fecha o navegador
    

# Chama a função para iniciar o robô
iniciar_robo()
