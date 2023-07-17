import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

chrome_options = Options()
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

driver.get('https://www.linkedin.com/in/pietro-silvaalvino-31a1161a2/')
try:
   
    frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'button'))  
    )
    driver.switch_to.frame(frame)
    elemento = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/button') 
    elemento.click()
    driver.switch_to.default_content()
except:
    print("O frame não foi encontrado ou ocorreu um erro.")

time.sleep(1)
campo_nome = driver.find_element(By.ID, "nome")
campo_nome.click()
time.sleep(1)
campo_nome.send_keys("Maria Pereira da Fonseca")  
campo_data = driver.find_element(By.ID, "data_nascimento") 
campo_data.clear()
time.sleep(1)
data = "31-12-2023"  # Formato: DD-MM-YYYY
time.sleep(1)
campo_data.send_keys(data)

