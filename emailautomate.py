from pandas import pd
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import urllib


contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)
navegador = webdriver.Edge()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(5)


#já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(5)
    navegador.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(keys.ENTER)
    time.sleep(10)
