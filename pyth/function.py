from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def definir_wait_global(wait_recebida):
    global wait
    wait = wait_recebida

def click(xpath):
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath))).click()

def sendKey(xpath, value):
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath))).send_keys(value)

def clear(xpath):
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).clear()
    
def clickId(id):
    wait.until(EC.visibility_of_element_located((By.ID,id))).click()

def sendKeyId(id,value):
    wait.until(EC.visibility_of_element_located((By.ID,id))).send_keys(value)

def clearId(id):
    wait.until(EC.visibility_of_element_located((By.ID,id))).clear()

def clickClass(className):
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,className))).click()

def clearClass(className):
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,className))).clear()

def clickText(value):
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT,value))).click()

def readTextId(id):
    wait.until(EC.visibility_of_element_located((By.ID,id))).get_attribute('textContent')

def readText(xpath):
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath))).get_attribute('textContent')

def changeFrame(frame):
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,frame)))

