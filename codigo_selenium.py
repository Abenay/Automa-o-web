from selenium import webdriver
import time

#abrir o navegador

navegador = webdriver.Chrome()

#acessa o site
navegador.get("https://www.hashtagtreinamentos.com/")

#abrir o navegador em tela cheia
navegador.maximize_window()

botao_assinatura = navegador.find_element("class name","header__titulo")

botao_assinatura.click()

#selecionar um elemento na tela
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break



#navegar em site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-sql")
navegador.find_element("id", "firstname").send_keys("Lira")
navegador.find_element("id", "email").send_keys("abenayferreira6@gmail.com")
navegador.find_element("id", "phone").send_keys("6140028922")

botao_quero_clicar = navegador.find_element("id", "_form_3397_submit")
#dar scroll ( colocar elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                        botao_quero_clicar)
#espera dinamica
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)
espera.until(EC.element_to_be_clickable(botao_quero_clicar))

botao_quero_clicar.click()
time.sleep(10)